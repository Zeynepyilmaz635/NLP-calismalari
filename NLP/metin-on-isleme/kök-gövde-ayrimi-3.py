# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 02:28:23 2025

@author: pc
"""
import nltk
nltk.download("wordnet") # lematization işlemi için gerkli veri tabanı

from nltk.stem import PorterStemmer # stemming için fonk


# porter stemmer nesnesini olşturalm
stemmer=PorterStemmer()
words=["running","runner","ran","runs","better","go","went"]
# eklimlerin stemlerini yani köklerini buluyorz
stems = [stemmer.stem(w) for w in words ]
print(stems)


# lematization ile kelimlerin anlamı köklerini bulalım
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmas=[lemmatizer.lemmatize(w,pos="v") for w in words]
#  pos=verb yaptık yani verb tipinde yap lemmatize
print(lemmas)