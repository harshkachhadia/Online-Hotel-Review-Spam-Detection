# -*- coding: utf-8 -*-
"""ALDA Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bKao6OZPplh0LAEjI8jxsm3YdnP_3SXD

#Importing Libraries
"""

import numpy as np 
import pandas as pd 
from textblob import TextBlob
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

"""#Get Data"""

df_original=pd.read_csv('deceptive-opinion.csv')
df_yelp=pd.read_csv('yelp_hotel_reviews.csv')
df_trip=pd.read_csv('TripAdvisor_hotel_reviews.csv')
df_expedia=pd.read_csv('reviews.csv')

"""# Merge Data"""

frames = [df_trip,df_expedia,df_yelp]
dataset = pd.concat(frames)
dataset = dataset.reset_index(drop=True)

dataset['Hotel'] = dataset['Hotel'].replace(['Bellagio Hotel','Bellagio Las Vegas'],'The Bellagio Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['The Palazzo','The Palazzo at The Venetian'],'The Palazzo Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['The Venetian Resort'],'The Venetian Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['The Nobu Hotel'],'Nobu Hotel at Caesars Palace')
dataset['Hotel'] = dataset['Hotel'].replace(['M Resort Spa Casino'],'M Resort Spa Casino Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['Red Rock Casino Resort And Spa'],'Red Rock Casino Resort & Spa')
dataset['Hotel'] = dataset['Hotel'].replace(['Aria Sky Suites'],'ARIA Sky Suites')
dataset['Hotel'] = dataset['Hotel'].replace(['Vdara Hotel & Spa'],'Vdara Hotel & Spa at ARIA Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['Encore At Wynn Las Vegas','Encore'],'Encore at Wynn Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['NoMad Las Vegas'],'The NoMad Hotel Las Vegas')
dataset['Hotel'] = dataset['Hotel'].replace(['Skyloft at MGM Grand'],'Skylofts at MGM Grand')
dataset['Hotel'] = dataset['Hotel'].replace(['The Cosmopolitan of Las Vegas, Autograph Collection'],'The Cosmopolitan of Las Vegas')

"""#Data Preprocessing - Cleaning the data"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import re
import string

stop_words = set(stopwords.words('english'))

def input_clean(text):

    #to lowercase
    text = text.lower()
    #removes text in square brackets
    text = re.sub('\[.*?\]', '', text)
    #removes non-alphanumeric characters
    text = re.sub("\\W"," ",text)
    #removes links 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    #removes special characters
    text = re.sub('<.*?>+', '', text)
    #removes punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    #removes new line characters
    text = re.sub('\n', '', text)
    #removes digits
    text = re.sub('\w*\d\w*', '', text)
    #removes extra space between words
    text = text.replace("  "," ")
    #removes front or trailing spaces
    text = text.strip()
    #removes stopwords
    text = ' '.join(w for w in text.split() if w not in stop_words)
    
    return text

df_original['text']=df_original['text'].apply(input_clean)
dataset['Text']=dataset['Text'].apply(input_clean)

"""#Encoding non-numeric class labels to numeric class labels"""

class_labels = df_original['deceptive']

from sklearn.preprocessing import LabelEncoder

encoder=LabelEncoder()
class_labels=encoder.fit_transform(class_labels)

training_data = df_original['text']
to_be_labelled_data=dataset['Text']

"""#Training Model on existing data & predicting on new data"""

sgd = Pipeline([('tfidf_vect', TfidfVectorizer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(training_data, class_labels)
y_pred_sgd = sgd.predict(to_be_labelled_data)

dataset['Labels'] = encoder.inverse_transform(y_pred_sgd)

"""# Adding Polarity Column"""

text_blob_objs = []

for i in list(to_be_labelled_data):
  text_blob_objs.append(TextBlob(i))

polarity_list=[]

for i in text_blob_objs:
  if i.sentiment.polarity<0:
    polarity_list.append("positive")
  elif i.sentiment.polarity>0:
    polarity_list.append("negative")
  elif i.sentiment.polarity==0:
    polarity_list.append("neutral")     

dataset['Polarity'] = polarity_list

"""# Generating Final Dataset"""

dataset.to_csv("hotel_review_spam_detection.csv",index=False)

"""# Dataset Statistics"""

dataset['Labels'].value_counts()

dataset['Polarity'].value_counts()

dataset['Hotel'].value_counts()

dataset['Source'].value_counts()