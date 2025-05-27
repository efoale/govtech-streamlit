
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ---------------------- Load Data ----------------------
df = pd.read_csv("classified_repositories.csv")
df['Last Updated'] = datetime.now().strftime('%Y-%m-%d')

# ---------------------- Page Config ----------------------
st.set_page_config(page_title="i.AI Opportunities Scanner", layout="wide")
st.markdown("""
<style>
    .header {
        background-color: #000000;
        color: white;
        padding: 10px;
        position: sticky;
        top: 0;
        z-index: 9999;
    }
    .disclaimer {
        font-size: 0.9em;
        background-color: #ffe9e9;
        padding: 10px;
        border-left: 5px solid red;
    }
</style>
<div class="header">
    <h2>i.AI Opportunities Scan Dashboard</h2>
    <p>TEST TEST – not government policy</p>
</div>
<div class="disclaimer">
    <strong>Note:</strong> This prototype dashboard is for demonstration purposes only and does not represent UK government policy.
</div>
""", unsafe_allow_html=True)

st.markdown("### 🌍 Scanning the horizon for AI tools, capabilities and opportunities")

# ---------------------- Section 1: Strategic Insights ----------------------
with st.expander("🆕 What's New Since Last Scan (hover for explanation)", expanded=True):
    st.markdown("*Mocked updates for demo purposes:*")
    st.markdown("""
    - `AI-Gov-Monitor` (Canada) – Added March 2025  
    - `PlanningAI UK` – Updated April 2025  
    - `EnergySimSG` – Added May 2025  
    *(In a live system, these would be pulled automatically from GitHub’s API.)*
    """)

with st.expander("🧠 Strategic Q&A (Simulated LLM Output)", expanded=True):
    st.markdown("""
- **With whom might i.AI achieve synergies?**  
  *GovTech Singapore, Canadian Digital Service, UK AlphaGov — aligned projects and modular infra.*

- **Where is there most duplication?**  
  *Citizen chatbot projects and open data dashboards across 4+ governments.*

- **Where could i.AI be a trailblazer?**  
  *Generative AI for internal workflows and planning document digitisation.*

- **What are barriers to spotting duplication?**  
  *Inconsistent naming, fragmented orgs, no common tagging standard.*
""")

with st.expander("🤖 LLM Idea Engine (Mocked Output)", expanded=True):
    st.success("**Idea:** Unified AI FAQ Chatbot across Departments\n**Desirability:** High\n**Feasibility:** Medium\n**Viability:** High")
    st.success("**Idea:** PlanningDoc Summariser using AI for Local Gov\n**Desirability:** High\n**Feasibility:** Low\n**Viability:** Medium")

with st.expander("🎯 Mapping to UK Government Missions", expanded=True):
    st.markdown("""
- **Strong Foundations:** Cybersecurity, infra, and data sharing.  
- **Kickstarting Economic Growth:** Open data and SME-accessible APIs.  
- **NHS Fit for the Future:** PlanningDoc AI, healthcare data tools.  
- **Safer Streets:** Predictive analytics for public safety (future).  
- **Break Down Barriers to Opportunity:** Accessibility projects (e.g., a11y).  
- **Clean Energy Superpower:** AI tools for energy queue optimization.  
""")

# ---------------------- Section 2: Filters ----------------------
st.sidebar.header("🔧 Filter Repositories")
category = st.sidebar.selectbox("Select category", ["All"] + sorted(df["category"].dropna().unique().tolist()))
min_stars = st.sidebar.slider("Minimum stars", 0, int(df["stars"].max()), 0)
search_term = st.sidebar.text_input("Search repository descriptions")

filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]
filtered_df = filtered_df[filtered_df["stars"] >= min_stars]
if search_term:
    filtered_df = filtered_df[filtered_df["description"].str.contains(search_term, case=False, na=False)]

# ---------------------- Data Export ----------------------
st.sidebar.markdown("### 📥 Export Filtered Data")
st.sidebar.download_button("Download CSV", filtered_df.to_csv(index=False), "filtered_repos.csv", "text/csv")

# ---------------------- Main Display ----------------------
st.markdown(f"### 📊 Showing {len(filtered_df)} Repositories")
st.dataframe(filtered_df[["name", "description", "stars", "language", "category", "Last Updated"]], use_container_width=True)

# ---------------------- Charts ----------------------
st.markdown("### 📈 Repository Category Distribution")
cat_count = df["category"].value_counts().reset_index()
cat_count.columns = ["Category", "Count"]
fig_pie = px.pie(cat_count, names="Category", values="Count", title="Repository Categories")
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### ⭐ Top Repositories by Stars")
top_repos = df.sort_values(by="stars", ascending=False).head(10)
fig_bar = px.bar(top_repos, x="name", y="stars", color="category", title="Top 10 Repositories")
st.plotly_chart(fig_bar, use_container_width=True)
