# Movie-recommender-system

This project is a **Content-Based Movie Recommender System** built using machine learning and natural language processing (NLP). It suggests similar movies based on a selected title using information like genres, keywords, cast, and director.

> Built with ❤️ using Python, Scikit-learn, NLTK, and deployed via Streamlit on Google Colab.

---

## 📌 Features

- ✅ Intelligent movie recommendations using content similarity
- 🎭 Uses real-world metadata from the TMDB 5000 Movies Dataset
- 🧠 NLP preprocessing with stemming and tokenization
- 🚀 Simple, elegant UI with [Streamlit](https://streamlit.io/)
- ☁️ Deployable from [Google Colab](https://colab.research.google.com/) with Ngrok

---

## 📁 Dataset

This project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which contains:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🧠 How It Works

1. **Data Loading & Merging**
   - Merges movies and credits data on title.

2. **Feature Extraction**
   - Extracts `overview`, `genres`, `keywords`, `cast`, and `crew` (only director).

3. **Text Processing**
   - Combines all features into one text string.
   - Applies stemming using `PorterStemmer`.

4. **Vectorization & Similarity**
   - Transforms text into vectors using `CountVectorizer`.
   - Computes cosine similarity between all movies.

5. **Recommendation**
   - Based on selected movie, returns top 5 similar titles.

---

## 🖥️ Demo

Launch the app using Streamlit + Ngrok in Google Colab:

```bash
!pip install streamlit pyngrok
!ngrok config add-authtoken <YOUR_NGROK_AUTH_TOKEN>

!streamlit run app.py &
from pyngrok import ngrok
public_url = ngrok.connect("http://localhost:8501")
print(public_url)
