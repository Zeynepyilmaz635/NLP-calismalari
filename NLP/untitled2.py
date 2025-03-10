# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:51:08 2025

@author: pc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('spam.csv' , encoding='latin-1',usecols=['v1','v2'])
df.columns=["labels","message"]
df.head()

df.groupby('label').desribe()


sns.countplot(data=df , x='label')

import string
from nltk.corpus import stopwords
from nltk import PorterStemmer as Stemmer

def process(text):
    text=text.lower()
     
    text="".join((t for t in text if t not in string.puncuation)) # noktalama işaretlerini değştirme
    text=[t for t in text.split() if t not in stopwords.words('english')]

    st=Stemmer()
    text= [st.stem(t) for t in text]   
    return text

df['message'][:10].apply(process)
    

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(analyzer=process)
data=tfidf.fit_transform(df['message'])


sample_message = df.iloc[2]['message'] 
print(sample_message)

print(tfidf.transform([sample_message]))



from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

spam_filter_model=Pipeline([
    ('vectorizer',TfidfVectorizer(analyzer = process)),
    ('classifier' , MultinomialNB)
    ])


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(df["message"],df["label"],test_size=0.2,random_state=21)

spam_filter_model.fit(X_train,y_train)

predictions=spam_filter_model.predict(X_test)
print(predictions)

count=0
for i in range(len(y_test)):
    if y_test.iloc[i]!=predictions[i]:
        count+=1
        
        
print("toplam test örmeği ",len(y_test))
print("yanlış tahmin sayısı : " , count)


from sklearn.metrics import classification_report

print(classification_report(predictions,y_test))


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    