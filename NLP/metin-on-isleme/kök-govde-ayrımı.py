# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:29:38 2025

@author: pc
"""

import nltk
nltk.download("wordnet") # wordnet: lemmatization işlemi için gerklli
from nltk.stem import PorterStemmer # stemming için fonk

# porter stemmer nesnesini oluştur
stemmer=PorterStemmer()
words=["running","ran","runs","better","go","went"]

# kelimelerin stemlerini buluyorz,bunu yaparken de poter stemmerin stem() fonk kullanılyorz
stems=[stemmer.stem(w) for w in words]





# lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

lemmas=[lemmatizer.lemmatize(w) for w in words]