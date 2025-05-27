
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load Data
df = pd.read_csv("classified_repositories.csv")
df['Last Updated'] = datetime.now().strftime('%Y-%m-%d')

# Header and Disclaimer
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

# Strategic Sections with Toggleable ⓘ Info
st.markdown("## 🆕 What's New Since Last Scan")
st.markdown("Latest additions and updates since the last GitHub scan.")
st.markdown("""
- `AI-Gov-Monitor` (Canada) – Added March 2025  
- `PlanningAI UK` – Updated April 2025  
- `EnergySimSG` – Added May 2025
""")
st.markdown("""
<details>
<summary>ⓘ Info</summary>
This section simulates a live feed of recent activity across government GitHub repositories. In a production system, this would use GitHub's API to compare timestamps and fetch any new or updated repositories, enabling real-time horizon scanning. You would be able to track project momentum, emerging tools, or sudden surges in development activity. Think of it as a changelog for global GovTech.
</details>
""", unsafe_allow_html=True)

st.markdown("## 🧠 Strategic Q&A (Simulated LLM Output)")
st.markdown("""
- **With whom might i.AI achieve synergies?**  
  GovTech Singapore, Canadian Digital Service, UK AlphaGov.

- **Where is there most duplication?**  
  Chatbots and open data dashboards across jurisdictions.

- **Where could i.AI be a trailblazer?**  
  Generative AI for internal government workflows.

- **What are barriers to spotting duplication?**  
  Inconsistent naming, no global taxonomy, fragmented data.
""")
st.markdown("""
<details>
<summary>ⓘ Info</summary>
These answers simulate what a real large language model (LLM) might generate based on analysis of repository metadata and content. Each answer reflects a strategic pattern observed in public code: common project types, collaborative opportunities, and inefficiencies. When operational, this would enable policy teams to ask high-level questions and get synthesised, evidence-backed summaries to guide decisions.
</details>
""", unsafe_allow_html=True)

st.markdown("## 🤖 LLM Idea Engine (Mocked Output)")
st.success("**Idea:** Unified AI FAQ Chatbot across Departments\nDesirability: High | Feasibility: Medium | Viability: High")
st.success("**Idea:** PlanningDoc Summariser using AI for Local Gov\nDesirability: High | Feasibility: Low | Viability: Medium")
st.markdown("""
<details>
<summary>ⓘ Info</summary>
This simulated idea generator shows what a GPT-based tool might suggest if asked: “Based on the available repositories and government priorities, what AI projects should we explore?” Each idea is scored on:
- **Desirability:** Does it solve a real citizen/government need?
- **Feasibility:** Could it realistically be built with current data/tech/resources?
- **Viability:** Would it work economically and at scale?
In a live system, ideas could be re-ranked by impact, mission alignment, or novelty.
</details>
""", unsafe_allow_html=True)

st.markdown("## 🎯 Mapping to UK Government Missions")
st.markdown("""
- **Strong Foundations:** Infra/security repos.
- **Economic Growth:** SME-friendly APIs and platforms.
- **NHS Future:** AI for planning and patient data.
- **Safer Streets:** Crime analytics (future).
- **Breaking Barriers:** Accessibility tools.
- **Clean Energy:** Energy grid optimisation tools.
""")
st.markdown("""
<details>
<summary>ⓘ Info</summary>
This section maps repository categories to the six UK strategic missions. It provides a top-down view of where government codebases align with broader public policy goals. In future versions, this could be interactive – e.g., selecting a mission to auto-highlight linked projects, or exposing coverage gaps that need exploration.
</details>
""", unsafe_allow_html=True)

# Sidebar Filters
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

# Download
st.sidebar.markdown("### 📥 Export Filtered Data")
st.sidebar.download_button("Download CSV", filtered_df.to_csv(index=False), "filtered_repos.csv", "text/csv")

# Table
st.markdown(f"### 📊 Showing {len(filtered_df)} Repositories")
st.dataframe(filtered_df[["name", "description", "stars", "language", "category", "Last Updated"]], use_container_width=True)

# Charts
st.markdown("### 📈 Repository Category Distribution")
cat_count = df["category"].value_counts().reset_index()
cat_count.columns = ["Category", "Count"]
fig_pie = px.pie(cat_count, names="Category", values="Count", title="Repository Categories")
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### ⭐ Top Repositories by Stars")
top_repos = df.sort_values(by="stars", ascending=False).head(10)
fig_bar = px.bar(top_repos, x="name", y="stars", color="category", title="Top 10 Repositories")
st.plotly_chart(fig_bar, use_container_width=True)
