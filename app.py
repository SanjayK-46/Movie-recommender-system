import streamlit as st
import pickle

# Load model and data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System")
st.write("Get movie recommendations based on your favorite!")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = similarity[index]
        movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        return [movies.iloc[i[0]].title for i in movie_indices]
    except IndexError:
        return ["❌ Movie not found. Try another."]

if st.button("Recommend"):
    st.subheader("🎥 Recommended Movies:")
    for rec in recommend(selected_movie):
        st.write(f"👉 {rec}")
