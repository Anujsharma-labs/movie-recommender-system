# 🎬 MovieFlix - Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Streamlit, and Machine Learning**. The application recommends movies similar to the one selected by the user and fetches high-quality movie posters using the **TMDB API**.

---

## 🚀 Live Demo

🔗 https://movieflix-anuj.streamlit.app

---

## 📌 Features

- 🎥 Recommend 5 similar movies
- 🖼️ Fetch movie posters using TMDB API
- ⚡ Fast recommendations using a precomputed similarity matrix
- 🌙 Clean and responsive Streamlit UI
- ☁️ Deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TMDB API
- Pickle
- Git & GitHub

---

## 🧠 Machine Learning Technique

This project uses **Content-Based Filtering**.

Movies are recommended based on their content, including:

- Genres
- Keywords
- Cast
- Crew
- Overview

The metadata is converted into feature vectors, and **Cosine Similarity** is used to find movies that are most similar to the selected movie.

---

## 📂 Project Structure

```text
MovieFlix/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Anujsharma-labs/movie-recommender-system.git
```

Move into the project folder

```bash
cd movie-recommender-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 TMDB API

This project uses **The Movie Database (TMDB) API** to fetch movie posters.

Create your own API key from:

https://www.themoviedb.org/settings/api

---

## 📈 Future Improvements

- Genre-based recommendations
- IMDb rating integration
- Movie trailers
- User authentication
- Hybrid recommendation system

---

## 👨‍💻 Developer

**Anuj Sharma**

GitHub: https://github.com/Anujsharma-labs
LinkedIn: https://www.linkedin.com/in/anuj-sharma-362063333

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
