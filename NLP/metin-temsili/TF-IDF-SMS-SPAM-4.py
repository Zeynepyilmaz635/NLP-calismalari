# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 03:40:38 2025

@author: pc
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# veri setini yğkke
df = pd.read_csv("spam.csv", encoding="latin1")  # veya encoding="ISO-8859-1"

# VERİ TEMZLMEE BLOĞU YAZILMALI


# tfidf
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df.text)



# kelime kümesini incele
feature_names = vectorizer.get_feature_names_out()
tfidf_score = X.mean(axis=0).A1 # her kelimenin tfidf değerleri
# tfidf skorlarını içeren bir df olştur
df_tfidf = pd.DataFrame({"word" : feature_names , "tfidf_score":tfidf_score})

# skorları sırala ve sonçlaarı incele
df_tfidf_sorted = df_tfidf.sort_values(by="tfidf_score",ascending=False)
print(df_tfidf_sorted.head(10))
































