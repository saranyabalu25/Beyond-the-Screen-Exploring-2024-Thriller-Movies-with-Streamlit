**Used Streamlit for interacting the real time data analysis

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine
from streamlit_option_menu import option_menu

# -----------------------------
# MySQL Connection Function
# -----------------------------
def get_connection():
    user = '4TMDeET5hb2Bj8r.root'
    password = '5rkxQxG1OohjStR2'
    host = 'gateway01.us-west-2.prod.aws.tidbcloud.com'
    port = '4000'
    database = 'test'
    conn_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(conn_str, connect_args={"ssl": {"ca": "C:/Users/HP/Downloads/ca.pem"}})

# -----------------------------
# Load and Preprocess Data
# -----------------------------
def load_data():
    engine = get_connection()
    query = "SELECT * FROM thriller_2024"
    df = pd.read_sql(query, engine)
    df["Votes"] = df["Votes"].replace(r"[KM]", "", regex=True).astype(float)
    df.loc[df["Votes"].astype(str).str.contains("K"), "Votes"] *= 1_000
    df.loc[df["Votes"].astype(str).str.contains("M"), "Votes"] *= 1_000_000
    df["Votes"] = df["Votes"].astype(int)
    df["Duration"] = df["duration_minutes"] if "duration_minutes" in df else df["Duration"].str.replace("m", "", regex=False).astype(int)
    return df

# -----------------------------
# Streamlit Setup
# -----------------------------
st.set_page_config(page_title="2024 Thriller Movie Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stSidebar {
        background-color: #1e293b;
        color: white;
    }
    h1, h2, h3 {
        color: #1a202c;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton button {
        background-color: #ef4444;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #dc2626;
    }
    .stSelectbox select, .stSlider input {
        border-radius: 6px;
        border: 1px solid #cbd5e0;
    }
    .css-1cpxqw2 {
        padding-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
with st.sidebar:
    st.title("🎬 Filter Options")
    min_rating, max_rating = st.slider("Rating Range", 0.0, 10.0, (0.0, 10.0), 0.1)
    min_votes, max_votes = st.slider("Votes Range", int(df["Votes"].min()), int(df["Votes"].max()), (int(df["Votes"].min()), int(df["Votes"].max())))
    selected_genres = st.multiselect("Genres", options=df["Genre"].unique(), default=df["Genre"].unique())
    min_duration, max_duration = st.slider("Duration (minutes)", int(df["Duration"].min()), int(df["Duration"].max()), (int(df["Duration"].min()), int(df["Duration"].max())))

# -----------------------------
# Apply Filters
# -----------------------------
filtered = df[
    (df["Rating"].between(min_rating, max_rating)) &
    (df["Votes"].between(min_votes, max_votes)) &
    (df["Genre"].isin(selected_genres)) &
    (df["Duration"].between(min_duration, max_duration))
]

# -----------------------------
# Tabs Menu
# -----------------------------
selected = option_menu(
    menu_title=None,
    options=["Overview", "Genres", "Ratings", "Votes", "Durations"],
    icons=["bar-chart", "layers", "star", "hand-thumbs-up", "clock"],
    orientation="horizontal",
    styles={
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"font-size": "16px", "background-color": "#1e293b", "color": "#ffffff", "border-radius": "8px"},
        "nav-link-selected": {"background-color": "#ef4444", "color": "white"},
    }
)

# -----------------------------
# Overview Tab
# -----------------------------
if selected == "Overview":
    st.title("Top Thriller Movies of 2024")
    top10 = filtered.sort_values(by=["Rating", "Votes"], ascending=[False, False]).head(10)
    st.dataframe(top10[["Title", "Genre", "Rating", "Votes", "Duration"]], use_container_width=True)

# -----------------------------
# Genres Tab
# -----------------------------
elif selected == "Genres":
    st.title("Genre Distribution")
    genre_count = filtered["Genre"].value_counts().reset_index()
    genre_count.columns = ["Genre", "Count"]
    st.bar_chart(genre_count.set_index("Genre"))

    st.title("Top Movie by Genre")
    top_by_genre = filtered.loc[filtered.groupby("Genre")["Rating"].idxmax()][["Genre", "Title", "Rating"]]
    st.dataframe(top_by_genre.sort_values(by="Rating", ascending=False), use_container_width=True)

# -----------------------------
# Ratings Tab
# -----------------------------
elif selected == "Ratings":
    st.title("Rating Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered["Rating"], bins=10, kde=True, ax=ax1)
    st.pyplot(fig1)

# -----------------------------
# Votes Tab
# -----------------------------
elif selected == "Votes":
    st.title("Votes vs Rating")
    fig2 = px.scatter(filtered, x="Votes", y="Rating", color="Genre", hover_data=["Title"])
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Durations Tab
# -----------------------------
elif selected == "Durations":
    st.title("Movie Durations")
    col1, col2 = st.columns(2)
    shortest = filtered.loc[filtered["Duration"].idxmin()][["Title", "Duration"]]
    longest = filtered.loc[filtered["Duration"].idxmax()][["Title", "Duration"]]
    col1.metric("Shortest Movie", shortest["Title"], f"{shortest['Duration']} mins")
    col2.metric("Longest Movie", longest["Title"], f"{longest['Duration']} mins")
