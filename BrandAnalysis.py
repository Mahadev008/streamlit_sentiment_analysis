import pickle
import streamlit as st
from textblob import TextBlob
import pandas as pd
import cleantext
import os
os.chdir("P:\\PyCharm Selenium Practice\\pythonProject\\Sentiment Analysis\\Final Project")


# Loading the saved model
scraper = pickle.load(open('./initialized_scraper.pkl', 'rb'))

# @st.cache_data(experimental_allow_widgets=True)
def brand_analysis(title="Brand Analysis"):
    with st.expander("Analyse User"):

        def data_processing(t):
            cleaned_text = cleantext.clean(t, clean_all=False, extra_spaces=True, stopwords=True,
                                           lowercase=True, numbers=True, punct=True, stemming=True, )
            return cleaned_text

        def score(x):
            blob2 = TextBlob(x)
            return blob2.sentiment.polarity

        def sentiment(x):
            if x >= 0.5:
                return "Positive"
            elif x <= -0.5:
                return "Negative"
            else:
                return "Neutral"

        def emoji(x):
            if x == "Positive":
                return "🙂"
            elif x == "Negative":
                return "☹️"
            elif x == "Neutral":
                return "😐"

        username = st.text_input("User name: ")
        # No_of_tweets = st.number_input("Number of tweets: ")
        No_of_tweets = st.number_input("Number of tweets: ", 0, 1000, "min", 1)
        if username and No_of_tweets:
            tweets = scraper.get_tweets(username, mode="user", number=No_of_tweets)
            data = {
                'link': [],
                'text': [],
                'user': [],
                'likes': [],
                'quotes': [],
                'retweets': [],
                'comments': []
            }

            for tweet in tweets['tweets']:
                data['link'].append(tweet['link'])
                data['text'].append(tweet['text'])
                data['user'].append(tweet['user']['name'])
                data['likes'].append(tweet['stats']['likes'])
                data['quotes'].append(tweet['stats']['quotes'])
                data['retweets'].append(tweet['stats']['retweets'])
                data['comments'].append(tweet['stats']['comments'])
            df = pd.DataFrame(data)
            st.write(df.head())

            st.success(f'{No_of_tweets} tweets from {username} has acquired successfully:thumbsup:')
            if st.button('Clean Dataset'):
                clean_df = df.drop(['link', 'user', 'likes', 'quotes', 'retweets', 'comments'], axis=1)
                clean_df.text = clean_df['text'].apply(data_processing)
                clean_df['score'] = clean_df['text'].apply(score)
                clean_df['sentiment'] = clean_df['score'].apply(sentiment)
                clean_df['emoji'] = clean_df['sentiment'].apply(emoji)
                st.write(clean_df.head(10))
                csv = clean_df.to_csv().encode('utf-8')
                if st.download_button(label="Download CSV", data=csv, file_name=f'{username}_tweets.csv',
                                      mime='text/csv'):
                    st.success('CSV Downloaded Successfully:thumbsup:')

