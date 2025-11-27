import streamlit as st
import pickle
import pandas as pd
import requests


movie_list=pickle.load(open('movies_dict1.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_list)



def fetch_poster(movie_id):
   response=requests.get(api_value,format(movie_id))
   data=response.json()
   return "https://image.tmdb.org/t/p/original/"+data['poster_path']
   


def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  recommended_poster=[]
  for i in movie_list:
    movie_id=movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    #fetch poster from api
    recommended_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_poster






st.title("Movie Recommendation System")

option=st.selectbox("Select a movie which u like , we will recommend it basis of that one: ",movies['title'])
api_value=st.sidebar.text_input("Enter the API ",type="password")

if st.button('Recommend') and api_value:


    names,posters=recommend(option)
    with st.container():
    
        st.caption(names[0])
        st.image(posters[0], width=150)


        st.caption(names[1])
        st.image(posters[1], width=150)


        st.caption(names[2])
        st.image(posters[2], width=150)

        st.caption(names[3])
        st.image(posters[3], width=150)

        st.caption(names[4])
        st.image(posters[4], width=150)

elif api_value=="":
   st.warning("API Key is not entered")


    
    