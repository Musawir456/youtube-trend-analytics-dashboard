# YouTube Trend Analytics Dashboard

## 1. Overview

This project analyzes a YouTube videos dataset and visualizes trends using
an interactive Streamlit dashboard. The goal is to understand which
categories and publish times perform better, and to identify top
trending videos based on views, likes, and comments. [file:117]

## 2. Dataset

- File: `youtube_data.csv`
- Example columns:
  - `title` – video title
  - `channel_title` – channel name
  - `views`, `likes`, `dislikes`, `comment_count`
  - `category` – content category (if available)
  - `publish_time` / `publishedAt` – upload time (converted to date, hour, weekday) [file:117]

## 3. Tech stack

- Python 3.x
- Pandas – data loading and preprocessing
- Matplotlib / Seaborn – visualizations
- Streamlit – interactive dashboard UI [file:117]

## 4. Dashboard features

- Filter videos by **category** and **publish weekday** using the sidebar.
- View **Top 10 videos by views** (table + bar chart).
- See **average views by category** to understand which content performs best.
- See **average views by publish weekday** to estimate the best day to upload.
- Designed to be extended later with simple machine learning models
  (e.g., high vs low performing videos). [file:117]

## 5. Project structure
PROJECT_3/
├── app.py # Streamlit dashboard
├── youtube_data.csv # YouTube videos dataset
├── youtube_videos_data_for_ml_andtrend_analysis.ipynb # Notebook for EDA/ML (optional)
└── README.md # Project documentation

## 6. How to run

1. Install Python 3.x.
2. Clone this repository and open a terminal in the project folder.
3. Install requirements:
## 7. Author

- Name: Abdul Musawir
- Program: BS IT / Computer Science
- University: [Superior University Lahore]
