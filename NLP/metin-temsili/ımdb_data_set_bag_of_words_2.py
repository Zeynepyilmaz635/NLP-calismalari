# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 02:21:34 2025

@author: pc
"""


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter

# veri setinin içeri aktarılması
df = pd.read_csv("IMDB Dataset.csv")

# metn verilerini alalım
documents= df["review"]
labels=df["sentiment"] # pozitif veya negatif


# metin temizleme
def clean_text(text):
    # büyğk küçük harf çevrimi
    text=text.lower()
    # rakamları temzleme
    text=re.sub(r"/d+" ,"",text)
    # özl karakterlerin kaldırılması
    text=re.sub(r"[^\w\s]","",text)
    # kısa kelimelerin temzlnmesi : in 
    text=" ".join([word for word in text.split() if len(word)>2])
    
    return text # tzmlenmş texti return et

cleaned_doc=[clean_text(row) for row in documents] # dökümandaki her bir atırı temilzedik





# bag of words




# vectorizer tanmlma
vectorizer=CountVectorizer()


# metnleri sayısal hale getir
X=vectorizer.fit_transform(cleaned_doc[:75])


# kelime kümesi göster
feature_names = vectorizer.get_feature_names_out()


# vektör temsilini göster
vektor_temsili2 = X.toarray()
print("vektör temsili : ", vektor_temsili2)
def_bow = pd.DataFrame(vektor_temsili2 , columns= feature_names)

# kelime frekanslarını göster
word_counts = X.sum(axis=0).A1
word_freq = dict(zip(feature_names , word_counts))


# ilk 5 kelme
most_common_5_words = Counter(word_counts).most_common(5)
print("ilk 5 : ", most_common_5_words)

















