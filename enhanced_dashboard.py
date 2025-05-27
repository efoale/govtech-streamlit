
import streamlit as st
import pandas as pd
import plotly.express as px

# Load classified repository data
df = pd.read_csv("classified_repositories.csv")

# ---------------------- Page Configuration ----------------------
st.set_page_config(page_title="i.AI Opportunities Scanner", layout="wide")
st.markdown("## 🔍 i.AI Opportunities Scan Dashboard")
st.markdown("Prototype dashboard to explore international GovTech repositories, classify projects, and simulate AI-driven insight discovery.")
st.markdown("### 🌍 Mission: Scanning the horizon for AI tools, capabilities and opportunities")

# ---------------------- Category Schema ----------------------
with st.expander("ℹ️ View Category Schema"):
    st.markdown("""
- **AI/ML:** Projects involving artificial intelligence or machine learning (e.g. chatbots, predictive analytics).
- **Citizen-Facing Service:** Services built for direct public or end-user interaction.
- **Developer Tool / API:** SDKs, APIs, and libraries for other services or teams.
- **Infrastructure / DevOps:** Cloud infra, automation, configuration.
- **Data / Open Data:** Repos publishing datasets or tools for data use.
- **Other:** Experimental or uncategorized repositories.
""")

# ---------------------- Sidebar Filters ----------------------
st.sidebar.header("🔧 Filter Repositories")
category = st.sidebar.selectbox("Select category", ["All"] + sorted(df["category"].dropna().unique().tolist()))
min_stars = st.sidebar.slider("Minimum stars", 0, int(df["stars"].max()), 0)

filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]
filtered_df = filtered_df[filtered_df["stars"] >= min_stars]

# ---------------------- Main Display ----------------------
st.markdown(f"### 📊 Showing {len(filtered_df)} repositories")

st.dataframe(filtered_df[["name", "description", "stars", "language", "category"]], use_container_width=True)

# ---------------------- Visualisations ----------------------
st.markdown("### 📈 Repository Category Distribution")
cat_count = df["category"].value_counts().reset_index()
cat_count.columns = ["Category", "Count"]
fig_pie = px.pie(cat_count, names="Category", values="Count", title="Repository Categories")
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### ⭐ Top Repositories by Stars")
top_repos = df.sort_values(by="stars", ascending=False).head(10)
fig_bar = px.bar(top_repos, x="name", y="stars", color="category", title="Top 10 Repositories")
st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------- "What's New" Section ----------------------
st.markdown("### 🆕 What's New Since Last Scan")
st.info("This section is mocked for demo purposes.\n\n- `AI-Gov-Monitor` (Canada) – Added March 2025\n- `PlanningAI UK` – Updated April 2025\n- `EnergySimSG` – Added May 2025")

# ---------------------- Strategic Q&A ----------------------
st.markdown("### 🧠 Strategic Q&A (Simulated LLM Output)")
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

# ---------------------- Idea Engine ----------------------
st.markdown("### 🤖 LLM Idea Engine (Mocked Output)")
st.success("**Idea:** Unified AI FAQ Chatbot across Departments\n**Desirability:** High\n**Feasibility:** Medium\n**Viability:** High")

st.success("**Idea:** PlanningDoc Summariser using AI for Local Gov\n**Desirability:** High\n**Feasibility:** Low\n**Viability:** Medium")

# ---------------------- Mission Mapping ----------------------
st.markdown("### 🎯 Mapping to UK Government Missions")
st.markdown("""
- **Strong Foundations:** Cybersecurity, infra, and data sharing.
- **Kickstarting Economic Growth:** Open data and SME-accessible APIs.
- **NHS Fit for the Future:** PlanningDoc AI, healthcare data tools.
- **Safer Streets:** Predictive analytics for public safety (future).
- **Break Down Barriers to Opportunity:** Accessibility projects (e.g., a11y).
- **Clean Energy Superpower:** AI tools for energy queue optimization.
""")

# Footer
st.caption("© 2025 i.AI – Dashboard prototype by Edward Foale")
