import streamlit as st
import pickle
import pandas as pd
import requests

# created a fn to fetch the poster
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=51495b031bd843a8251ec063ec2d3639&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


# created a fucntion to get input movie and return 5 movies
def recommend(movie_input):
    recommended_movies_list = []
    recommended_movies_poster_list = []
    movie_index = movies_data[movies_data['title'] == movie_input].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        recommended_movies_list.append(movies_data.iloc[i[0]].title)
        poster = fetch_poster(movies_data.iloc[i[0]].id)
        recommended_movies_poster_list.append(poster)


    return recommended_movies_list,recommended_movies_poster_list



movies = pickle.load(open('movies.pkl','rb'))
movies_data = pd.DataFrame(movies)            # orginal data name

similarity = pickle.load(open('similarity.pkl','rb'))

# fetching the movies from the dataset
st.title('Movie Recommender System \n Designed By: NOORAIN RAZA')   # page title
selected_movie_name = st.selectbox('Enter Movie name:',  # getting selected movie name
                      movies_data['title'].values)

# creating a button to get the selected movie name
if st.button('Recommended'):
    recommended_movie,recommended_movie_poster = recommend(selected_movie_name)   # passing the selected movie name
    # recommend fn return movies name and their posters


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_poster[0])

    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_poster[2])

    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_poster[3])

    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_poster[4])

