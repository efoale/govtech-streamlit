
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("classified_repositories.csv")

# Page config
st.set_page_config(page_title="GovTech Repo Explorer", layout="wide")

st.title("🌐 International GovTech Repository Explorer")

# Filters
with st.sidebar:
    st.header("🔍 Filter Repositories")
    category = st.selectbox("Select Category", ["All"] + sorted(df["category"].dropna().unique().tolist()))
    min_stars = st.slider("Minimum Stars", 0, int(df["stars"].max()), 0)

# Filter logic
filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]
filtered_df = filtered_df[filtered_df["stars"] >= min_stars]

# Display results
st.markdown(f"### Showing {len(filtered_df)} Repositories")
st.dataframe(filtered_df[["name", "description", "stars", "language", "category"]], use_container_width=True)

# Footer
st.caption("Built for the i.AI Technical Assessment by Edward Foale.")
