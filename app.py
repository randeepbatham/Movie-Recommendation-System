import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies = pickle.load(open('movie_list.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.header('🎥 Movie Recommender System')
st.text("Welcome! This app recommends movies based on your favorite film.")

selected_movie_name = st.selectbox(
    'What Would You to be Watched?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col = st.columns(5)

    with col[0]:
        st.image(posters[0])
        st.text(names[0])

    with col[1]:
        st.image(posters[1])
        st.text(names[1])

    with col[2]:
        st.image(posters[2])
        st.text(names[2])

    with col[3]:
        st.image(posters[3])
        st.text(names[3])

    with col[4]:
        st.image(posters[4])
        st.text(names[4])
