# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 02:56:41 2025

@author: pc
"""
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # farklı dillerde en çok kullanılan stop words içern veri seti



# ing stop word analizi (with nltk)
stop_words_eng=set(stopwords.words("english"))

# örnk ing metn
text="There are some examples of handling stop words from some texts"
text_list = text.split() #  tokenlaştırdık
filtered_words=[word for word in text_list if word.lower() not in stop_words_eng]




# türkçe stop word analizi (with nltk)
stop_words_turk=set(stopwords.words("turkish"))
text2="Bu örneği ben kendim yapıyorum ve umarım yapabilirim"
text_list2=text2.split()
filtered_list2=[word2 for word2 in text_list2 if word2.lower() not in stop_words_turk]













# kütüphanesiz stop words çıkarımı veyahut filtrelenmesi

stop_word_list=["zey","özel","mi","bu","şu","şey","için","ile","o","veya","ve"]
metin="Bu bir denemedir. Amcımız bu metinde bulunan özel karakterleri elemek mi acaba"

filtred=[word for  word in metin.split() if word.lower() not in stop_word_list ]
# stop wordleri tespit etk istersek not in yerine sadece in yazarız


















