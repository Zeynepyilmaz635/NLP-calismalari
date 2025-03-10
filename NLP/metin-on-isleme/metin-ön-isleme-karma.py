# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 03:22:50 2025

@author: pc
"""

text="This is a test. My name is @Zeynep. I am currently doing text preprocessing, let's see the result. How will it be?"
# boşlkları temzledik
cleaned_text=" ".join(text.split())

# büyük -> küçük harf
cleaned_text=cleaned_text.lower()

# noktalama işaretlerini kaldır
import string 
cleaned_text=cleaned_text.translate(str.maketrans("","",string.punctuation))

#  yazım hatası düzltme
from textblob import TextBlob
cleaned_text = str(TextBlob(cleaned_text).correct()) 



#  TOKENİZASYON
import nltk
nltk.download('punkt') 
nltk.download('punkt_tab')

word_tokenize=nltk.word_tokenize(cleaned_text)



# KÖK GÖVDE AYRIMI
nltk.download("wordnet")
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
stems=[stemmer.stem(w) for w in word_tokenize]


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmas=[lemmatizer.lemmatize(w,pos="v") for w in word_tokenize]




#  STOP WORDS
from nltk.corpus import stopwords
nltk.download("stopwords")

stop_words_eng=set(stopwords.words("english"))
filtreed_word=[w for w in word_tokenize if w not in stop_words_eng]


























