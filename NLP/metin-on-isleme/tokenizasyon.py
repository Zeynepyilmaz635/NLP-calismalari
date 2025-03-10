# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:18:53 2025

@author: pc
"""
import nltk # natural language toolkit
nltk.download("punkt") # metni kelime ve cümle bazında tokenlara ayırabilmek için gerekli

text="Hllo, World! How are you? Hello , hi ..."

# kelime tokenizasyonu : word_tokenize : metni kelimelere ayırır
# noktalama işaretleri be boşluklar ayrı birer token olarak elde edşlecektşr
word_tokens=nltk.word_tokenize(text) 

# cümle tokenizasyonu : sent_tokenize :  metni cümlelere ayırır. her bir cümle birer token olur
sentence_tokens=nltk.sent_tokenize(text)
