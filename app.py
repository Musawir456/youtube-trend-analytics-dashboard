#1) app.py base code
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")

# ------------ DATA LOAD ------------

@st.cache_data
def load_data():
    df = pd.read_csv("youtube_data.csv")
    # Column names adjust karo agar different hon:
    # yahan assume: views, likes, dislikes, comment_count, category, publish_time
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['publish_date'] = df['publish_time'].dt.date
    df['publish_hour'] = df['publish_time'].dt.hour
    df['publish_weekday'] = df['publish_time'].dt.day_name()
    return df

df = load_data()

st.title("YouTube Videos Trend & Analytics Dashboard")

st.markdown("Dataset: YouTube videos data for trend analysis and simple ML experiments.")

# ------------ SIDEBAR FILTERS ------------

st.sidebar.header("Filters")

# Category filter (optional)
if 'category' in df.columns:
    categories = ["All"] + sorted(df['category'].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Category", categories)
else:
    selected_category = "All"

# Weekday filter
weekdays = ["All","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
selected_weekday = st.sidebar.selectbox("Publish weekday", weekdays)

# Apply filters
filtered_df = df.copy()

if selected_category != "All" and 'category' in df.columns:
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

if selected_weekday != "All":
    filtered_df = filtered_df[filtered_df['publish_weekday'] == selected_weekday]

st.write(f"Total videos after filters: {len(filtered_df)}")


# 2) Top videos & category chart section
# ------------ TOP 10 VIDEOS BY VIEWS ------------

st.subheader("Top 10 videos by views")

top_videos = filtered_df.sort_values('views', ascending=False).head(10)

st.dataframe(
    top_videos[['title','channel_title','views','likes','comment_count']].reset_index(drop=True)
)

fig1, ax1 = plt.subplots(figsize=(10,5))
sns.barplot(x='views', y='title', data=top_videos, ax=ax1)
ax1.set_title("Top 10 videos by views")
ax1.set_xlabel("Views")
ax1.set_ylabel("Title")
st.pyplot(fig1)


# ------------ CATEGORY-WISE AVERAGE VIEWS ------------

if 'category' in filtered_df.columns:
    st.subheader("Average views by category")

    cat_views = (
        filtered_df.groupby('category')['views']
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    fig2, ax2 = plt.subplots(figsize=(10,5))
    cat_views.plot(kind='bar', ax=ax2)
    ax2.set_ylabel("Average views")
    ax2.set_title("Average views by category (top 10)")
    st.pyplot(fig2)
#3) Weekday trend chart + stats
# ------------ WEEKDAY TREND ------------

st.subheader("Average views by publish weekday")

weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

weekday_views = (
    df.groupby('publish_weekday')['views']
      .mean()
      .reindex(weekday_order)
)

fig3, ax3 = plt.subplots(figsize=(8,4))
weekday_views.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Average views")
ax3.set_title("Average views by publish weekday (overall)")
st.pyplot(fig3)

# Simple insight text
best_day = weekday_views.idxmax()
best_day_views = int(weekday_views.max())
st.markdown(f"**Best day to upload (by average views):** {best_day} (~{best_day_views} views).")
