import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# Load the data
courses_list = pickle.load(open('courses.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(course):
    try:
        index = courses_list[courses_list['course_name'] == course].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_course_names = []
        recommended_course_urls = []
        for i in distances[1:7]:
            course_name = courses_list.iloc[i[0]].course_name
            course_url = courses_list.iloc[i[0]]['Course URL']
            recommended_course_names.append(course_name)
            recommended_course_urls.append(course_url)
        return recommended_course_names, recommended_course_urls
    except IndexError:
        return [], []

st.markdown("<h2 style='text-align: center; color: blue;'>Coursera Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Web App created by Saathi</h4>", unsafe_allow_html=True)

course_list = courses_list['course_name'].values
selected_course = st.selectbox("Type or select a course you like:", course_list)

if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your interests are:")
    recommended_course_names, recommended_course_urls = recommend(selected_course)
    if recommended_course_names:
        for name, url in zip(recommended_course_names, recommended_course_urls):
            st.markdown(f"[{name}]({url})")
    else:
        st.write("No recommendations found for the selected course.")
    st.text(" ")
    st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>", unsafe_allow_html=True)
