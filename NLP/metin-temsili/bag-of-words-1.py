# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 01:55:22 2025

@author: pc
"""
from sklearn.feature_extraction.text import CountVectorizer




# veri seti olştur

documents={
    "kedi bahçede",
    "kedi evde"}




# vectorizer tanımla
vectorizer=CountVectorizer()


# metni sayısal vektörlere çevir
X = vectorizer.fit_transform(documents)

# kelime kümesi olşturma
feature_name = vectorizer.get_feature_names_out() #  kelime kümesini olşturma
print(f"kelime kümesi : {feature_name}")


#  vectör temsili
vector_temsili = X.toarray()
print(f"vectör_temsili : {vector_temsili}")



























