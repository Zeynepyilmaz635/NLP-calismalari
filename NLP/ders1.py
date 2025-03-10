
"""
# ONE HOT ENCODİNG
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

kelimeler = [["kedi"], ["köpek"], ["kuş"], ["balık"]]

encoder = OneHotEncoder(sparse_output=False)  # Hata burada düzeltilmiş

one_hot_encoded = encoder.fit_transform(kelimeler)

print("kelime listem : ", encoder.categories_)
print("one hot encoded matrisi : ")
print(one_hot_encoded)

for kelime, vektor in zip(kelimeler, one_hot_encoded):
    print(f"Kelime : {kelime} one-hot-encoded vektörü : {vektor}")
"""


"""
# LABEL ENCODİNG
from sklearn.preprocessing import LabelEncoder
kelimeler2 = ["kedi", "köpek", "kuş","balık"]
encoder_label=LabelEncoder()
encoded=encoder_label.fit_transform(kelimeler2)
print("orjinal kelimeler : " , kelimeler2)
print("sayısal etiketleri : " , encoded)
print(dict(zip(kelimeler2,encoded.tolist())))
"""



"""
# BAG OF WORDS
from sklearn.feature_extraction.text import CountVectorizer
corpus=[
        "kedi fareyi yedi",
        "köpek kediye baktı",
        "kedi ve köpek arkadaş oldu"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out()) # kelime listesini verir
print(X.toarray())

"""

"""
# TF - İDF 
from sklearn.feature_extraction.text import TfidfVectorizer
corpus=[
        "kedi fareyi yedi",
        "köpek kediye baktı",
        "kedi ve köpek arkadaş oldu"
]

vectorizer=TfidfVectorizer()
X = vectorizer.fit_transform(corpus) 
print("kelime listesi : " , vectorizer.get_feature_names_out())
print("tf - idf matrisi : ")
print(X.toarray())
"""

# ANLAMSAL İFADELER
"""
# Word2Vec
import numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

corpus=[
        ["kedi","süt","içti"],
        ["köpek","havladı"],
        ["kuş","uçtu"],
        ["kedi","miyavladı"],
        ["köpek","kemik","yedi"],
        ["kuş","kanat","çırptı"],
        ["kedi","fare","yakaladı"],
        ["köpek","havladı","ve","sahibini","gördü"]
        ]

model = Word2Vec(sentences=corpus , vector_size=50 , window=3 , min_count=1 , sg=1) #skip gram kullandk

print("Kedinin vektörü : ")
print(model.wv["kedi"])

print("kediye en yakın kelimeler : ")
print(model.wv.most_similar("kedi"))

"""

# FASTTEXT
import nltk
nltk.download("punkt")
from gensim.models import FastText
from nltk.tokenize import word_tokenize

sentences=[
    "fasttext embeddings handle subword information.",
    "it is effective for various languages."
    
    ]

tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
model = FastText(sentences=tokenized_sentences , vector_size=100,window=5,min_count=1,workers=4)
word_embeddings=model.wv
print(word_embeddings['subword'])













