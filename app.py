import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Image"

def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distance = similarity[index]
        distances = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])

        recommended_movies = []
        recommended_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_posters

# Load data
movie_dict = pickle.load(open('moive_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie you like',
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    if recommended_movie_names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(recommended_movie_posters[i])
                st.markdown(f"**{recommended_movie_names[i]}**", unsafe_allow_html=True)
