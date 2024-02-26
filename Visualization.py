import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import seaborn as sns
import streamlit as st
import os
os.chdir("P:\\PyCharm Selenium Practice\\pythonProject\\Sentiment Analysis\\Final Project")

@st.cache_data
def count_plot(df):
    fig = plt.figure(figsize=(5, 5))
    sns.countplot(x='sentiment', data=df, palette="Set1", edgecolor="black")
    st.pyplot(fig)

@st.cache_data
def pie_chart(df):
    fig = plt.figure(figsize=(7, 7))
    colors = ("yellowgreen", "gold", "red")
    wp = {'linewidth': 2, 'edgecolor': "black"}
    tags = df['sentiment'].value_counts()
    explode = (0.1, 0.1, 0.1)
    tags.plot(kind='pie', autopct='%1.1f%%', shadow=True, colors=colors, startangle=90, wedgeprops=wp, explode=explode,
              label='')
    plt.title('Distribution of Sentiments')
    st.pyplot(fig)

@st.cache_data
def freq_pos_words(df):
    pos_tweets = df[df.sentiment == "Positive"]
    text = ' '.join([word for word in pos_tweets['text']])
    plt.figure(figsize=(20, 15), facecolor='None')
    wordcloud = WordCloud(max_words=500, width=1600, height=800).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.title("Most Frequent Words in Positive Tweets", fontsize=30)
    st.pyplot()

@st.cache_data
def freq_neu_words(df):
    neu_tweets = df[df.sentiment == "Neutral"]
    text = ' '.join([word for word in neu_tweets['text']])
    plt.figure(figsize=(20, 15), facecolor='None')
    wordcloud = WordCloud(max_words=500, width=1600, height=800).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.title("Most Frequent Words in Neutral Tweets", fontsize=30)
    st.pyplot()

@st.cache_data
def freq_neg_words(df):
    neg_tweets = df[df.sentiment == "Negative"]
    text = ' '.join([word for word in neg_tweets['text']])
    plt.figure(figsize=(20, 15), facecolor='None')
    wordcloud = WordCloud(max_words=500, width=1600, height=800).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.title("Most Frequent Words in Negative Tweets", fontsize=30)
    st.pyplot()


def visual():
    with st.expander("Visualize the dataset 😀"):
        user_data_frame = st.file_uploader(label="Upload your dataset:")
        if user_data_frame:
            data_frame = pd.read_csv(user_data_frame)
            menu = ["Count Plot", "Pie-Chart", "Frequent Positive Words", "Frequent Neutral Words",
                    "Frequent Negative Words"]
            choice = st.selectbox("Select the type of visual you need: ", menu, index=None, placeholder="Select one", )

            if choice == 'Count Plot':
                count_plot(data_frame)
                st.success('Here is your Count Plot 🙌')

            elif choice == 'Pie-Chart':
                pie_chart(data_frame)
                st.success('Here is your Pie-Chart 🙌')

            elif choice == 'Frequent Positive Words':
                freq_pos_words(data_frame)
                st.success('Here is your Frequent Positive Words 🙌')

            elif choice == 'Frequent Neutral Words':
                freq_neu_words(data_frame)
                st.success('Here is your Frequent Neutral Words 🙌')

            elif choice == 'Frequent Negative Words':
                freq_neg_words(data_frame)
                st.success('Here is your Frequent Negative Words 🙌')