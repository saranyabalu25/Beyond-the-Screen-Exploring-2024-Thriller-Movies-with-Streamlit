

🙋‍♀️** About the Author**
Saranya
Senior Operation Analyst | Data Science Enthusiast
Skilled in SQL, Python, and data visualization, passionate about blending tech and storytelling through data.

# Beyond-the-Screen-Exploring-2024-Thriller-Movies-with-Streamlit
This project extracts, stores, and visualizes IMDb's 2024 thriller movie data. It involves scraping key details like ratings, genres, votes, and durations, storing them in a MySQL database, and building an interactive Stream lit dashboard for exploration, filtering, and data-driven insights.
# 🎬 IMDb 2024 Movie Insights Dashboard

Welcome to the **IMDb 2024 Movie Insights Dashboard**, an interactive, visually rich dashboard developed by **Saranya**. This project brings together data science, web development, and movie analytics using **Streamlit**, powered by a **TiDB Cloud (MySQL)** database to explore and visualize the 2024 IMDb thriller movie dataset.

---

## 📌 Table of Contents
- 🎯 Project Overview  
- ✨ Features  
- 🖼️ Dashboard Screens  
- 📊 Tech Stack  
- 🔧 Setup Instructions  
- 🛠️ Project Structure  
- 🗃️ Database Schema  
- 🚀 Future Improvements  

---

## 🎯 Project Overview

This project extracts IMDb thriller movie data for 2024 using Selenium and organizes it into genre-specific CSV files before consolidating into a TiDB Cloud MySQL database (`test.imdb_2024` table). The Streamlit dashboard connects live to the database and allows users to filter, explore, and visualize key insights—ratings, votes, durations, and genre breakdowns—with custom-styled UI components.

---

## ✨ Features

- ✔️ Real-time database querying via SQLAlchemy  
- ✔️ Custom CSS theming for a modern, intuitive UI  
- ✔️ Dynamic filters: rating, votes, duration, genre  
- ✔️ Interactive charts: histograms, scatterplots, pie charts, heatmaps  
- ✔️ Tab-based navigation with Streamlit Option Menu  
- ✔️ CSV download of filtered results  

---

## 🖼️ Dashboard Screens

| Tab               | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **Overview**      | Top 10 movies by rating & votes, rating distribution histogram              |
| **Genre Analysis**| Genre counts, average duration by genre, top-rated per genre, heatmap      |
| **Voting**        | Average & total votes by genre, pie chart of vote distribution              |
| **Durations**     | Metrics on shortest and longest movies                                       |
| **Correlations**  | Scatterplot of Ratings vs Votes for deeper insights                         |

---

## 📊 Tech Stack

| Layer                    | Technologies                           |
|--------------------------|----------------------------------------|
| **Dashboard (Frontend)** | Streamlit, Plotly, Matplotlib, Seaborn |
| **Database (Backend)**   | TiDB Cloud (MySQL), SQLAlchemy, PyMySQL|
| **Data Wrangling**       | Pandas, NumPy                          |
| **Scraping**             | Selenium                               |

---

## 🔧 Setup Instructions

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/imdb-2024-dashboard.git
   cd imdb-2024-dashboard

2.**(Optional) Create & activate a virtual environment**
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS/Linux

3.**Install dependencies**
pip install -r requirements.txt

4.**Configure database connection**
In streamlit.py, update the get_connection() function with your TiDB Cloud credentials:

host     = "YOUR_HOST"
user     = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
port     = "YOUR_PORT"
database = "YOUR_DATABASE"
ssl_ca   = "C:/Users/HP/Downloads/ca.pem"

5.**Run the dashboard**
streamlit run streamlit.py
Your browser will open at http://localhost:8501.

**🛠️ Project Structure**

├── streamlit.py            # Main Streamlit dashboard script
├── imdb_scraper.py         # (Optional) Selenium scraper script
├── thriller_2024.csv       # Raw/cleaned thriller movie data
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation


**🗃️ Database Schema**
Table: test.imdb_2024
Column	Type	Description
Title	VARCHAR	Movie title
Genre	VARCHAR	Primary genre
Rating	FLOAT	IMDb rating
Votes	INT	Number of votes
duration_minutes	INT	Duration in minutes

**🚀 Future Improvements**
🎥 Add movie posters and trailers

🤖 Integrate sentiment analysis on user reviews

🌍 Map-based visualization of production countries

📱 Improve mobile responsiveness

☁️ Deploy on Streamlit Cloud or Docker/Kubernetes


**🙌 Acknowledgements**
Data courtesy of IMDb

Powered by Streamlit, Selenium, TiDB Cloud, and open-source libraries

Built with ❤️ by Saranya , Data scientist
