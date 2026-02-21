# 📺 YouTube Trend Analytics Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Explore YouTube video trends with an interactive, filterable analytics dashboard.**

*Discover top-performing categories, best upload times, and trending videos — all in one place.*

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Dashboard Features](#-dashboard-features)
- [Getting Started](#-getting-started)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🧠 Overview

YouTube generates billions of views every day — but what actually makes a video trend? This project digs into a real YouTube videos dataset and surfaces actionable insights through an **interactive Streamlit dashboard**.

**Key questions answered:**
- 📊 Which content categories get the most views?
- 📅 What day of the week is best to upload a video?
- 🏆 Which videos are currently topping the trending charts?

The dashboard is fully filterable by category and publish weekday, making it easy to slice and explore the data interactively.

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.x |
| **Dashboard UI** | Streamlit |
| **Data Handling** | pandas |
| **Visualization** | matplotlib, seaborn |
| **Environment** | Jupyter Notebook, VS Code |

---

## 📂 Dataset

**File:** `youtube_data.csv`

| Column | Description |
|---|---|
| `title` | Video title |
| `channel_title` | Channel name |
| `views` | Total view count |
| `likes` | Total like count |
| `dislikes` | Total dislike count |
| `comment_count` | Number of comments |
| `category` | Content category |
| `publish_time` / `publishedAt` | Upload timestamp → converted to date, hour & weekday |

---

## 🗂 Project Structure

```
PROJECT_3/
│
├── 🚀 app.py                                              # Streamlit dashboard (main app)
├── 📊 youtube_data.csv                                    # YouTube videos dataset
├── 📓 youtube_videos_data_for_ml_andtrend_analysis.ipynb # EDA & ML notebook (optional)
└── 📄 README.md                                           # Project documentation
```

---

## ✨ Dashboard Features

### 🎛️ Sidebar Filters
- Filter videos by **content category**
- Filter by **publish weekday** to isolate specific days

### 🏆 Top 10 Videos by Views
- Ranked table of the 10 most-viewed trending videos
- Bar chart visualization for quick comparison

### 📊 Average Views by Category
- Identify which content categories consistently perform best
- Useful for content strategy and niche selection

### 📅 Average Views by Publish Weekday
- Discover the best day of the week to upload for maximum reach
- Bar chart showing Mon–Sun performance breakdown

### 🔮 Extendable with ML
- Dashboard is designed to plug in ML models (e.g., classify videos as high vs low performing) in future iterations

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Musawir456/youtube-trend-analytics-dashboard.git
cd youtube-trend-analytics-dashboard
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
matplotlib
seaborn
streamlit
```

### 4. Run the Dashboard

```bash
streamlit run app.py
```

### 5. Open in Browser

```
http://localhost:8501
```

---

## 🔮 Future Improvements

- 🤖 **ML Classification** — Predict whether a video will be high or low performing based on metadata
- 📈 **Time-Series Trends** — Track category performance over months and years
- 🔎 **Search & Filter** — Add keyword search to find specific videos or channels
- ☁️ **Cloud Deployment** — Deploy to Streamlit Community Cloud for public access
- 🌐 **Multi-Region Support** — Extend analysis to trending data from multiple countries

---

## 👨‍💻 Author

<div align="center">

**Abdul Musawir**
*BS IT / Computer Science*
*AI/ML Engineer & Data Scientist*
🎓 Superior University, Lahore
📍 Lahore, Pakistan

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdul-musawir-a9713a20b/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Musawir456)
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/abmusawir)

</div>

---

<div align="center">

⭐ **If you found this project useful, please give it a star!** ⭐

*Made with ❤️ by Abdul Musawir — Superior University, Lahore*

</div>
