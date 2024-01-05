#Importing Important Libraries
import pandas as pd
import pickle
import streamlit as st

#Loading the Neccesary Classes from the .ipynb file 
cosine_sim = pickle.load(open('SimilarityClass.pkl', 'rb'))
indexes = pickle.load(open('Indexes.pkl','rb'))
movies = pickle.load(open('movies.pkl', 'rb'))


st.title('Movie Recommendation Engine')
st.balloons()
title = st.text_input('Enter Movie Title')

def Recommend(title, cosine_sim = cosine_sim):

    try: #firstly get the index of the movie
        idx = indexes[title.lower()]
        Score = list(enumerate(cosine_sim[idx]))

        #Get the score of the top 10 similar ones in descending form
        recommendations = sorted(Score, key = lambda x: x[1], reverse = True)
        Scores = recommendations[1:11]

        #Get movies indices
        titleIndex = [i[0] for i in Scores]
        st.write(f'You enjoyed {title}! check these out ')
        return movies['title'].iloc[titleIndex]


    except KeyError:
        return 'Enter another movie'
        
if st.button('Recommend'):
    movies = Recommend(title)
    st.write(movies)
    
    
    