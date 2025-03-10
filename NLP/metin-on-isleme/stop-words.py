# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:36:31 2025

@author: pc
"""
import nltk
from nltk.corpus import stopwords 
nltk.download("stopwords") # farklı dillerde en ok kullanılan stop words veri seti



# ingilizce stop words analzii -nltk with
stop_words_eng=set(stopwords.word("english"))

# örnk ing metn
text="there are same examples of handling stop words from some texts. "
text_list=text.split()
# eğer word ing stop words listesinde (stop_words_eng) yoksa, bu kelimeyi filtrelenmş listeye ekliyorz
filtered_words=[word for word in text_list if word.lower() not in stop_words_eng]

# türkçe stop words analizi
stop_words_tr=set(stopwords.words("turkish"))
metn="mwrhaba arkadaşlar çok güzel bir ders işliyoruz"
metin_list2=metn.split()
filtered_words_tr=[word for word in metin_list2 if word.lower() not in stop_words_tr]


# kütüphanesiz stop words çıkarımı
# top words listesi olşturlm kndmz
tr_stopwords=["için","bu","ile","mu","mi","özel"]
mtn="bu bir denemedir amacımız bu metinde bulunan özel karakterleri elemek mi acaba"
filtred_words=[word for word in mtn.split() if word.lower() not in tr_stopwords]