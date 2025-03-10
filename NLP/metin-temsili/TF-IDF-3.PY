# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 03:25:59 2025

@author: pc
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# örnk belge olştur
documents=[
    "Köpek çok tatlı bir hayvandır",
    "Köpek ve kuşlar çok tatlı hayvanlardır.",
    "Inekler süt üretirler."]

# vektörizer tanmla
tfidf_vectorizer= TfidfVectorizer()

# metnleri sayısal hale çevirme
X=tfidf_vectorizer.fit_transform(documents)

# kelime kümesini incele
feature_names = tfidf_vectorizer.get_feature_names_out()

# vektör temsilini incele
vektor_temsili= X.toarray()
print("vektör temsili : ",vektor_temsili)
df_tfidf=pd.DataFrame(vektor_temsili,columns=feature_names)


# ortalama tf-idf değerlerine bakalm
tf_idf = df_tfidf.mean(axis=0)
# tf idf deeğri yüksk ise documnda fazla geçiyor

























