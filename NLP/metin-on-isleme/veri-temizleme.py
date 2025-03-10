# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:29:08 2025

@author: pc
"""

# metinlerde bulunan fazla boslukları ortadan kaldır
text="Hello,    World!       2035"

cleaned_text1=" ".join(text.split())
print("cleaned_text1 : " ,cleaned_text1)


# buyuk -> kucuk harf cevirisi
text2="Hello,xt World! 2035"
cleaned_text2=text2.lower()


# noktalama işaretlerini kaldır
import string
text3="Hello, World! 2035"
cleaned_text3=text3.translate(str.maketrans("","",string.punctuation))


# özel karakterleri kaldırma
import re
text4="He/llo, %world & "
cleaned_text4=re.sub(r"[^Z-Za-z0-9\s]" , "" ,text4)
print(cleaned_text4)


# yazim hatalarını düzelt
from textblob import TextBlob # metin analizlerinde kullanılan bir kütüphane
text5="Hellıo, Wirld! 2035"
cleaned_text5=TextBlob(text5).correct() # correct : yazım hatalarını düzltir


# html ya da url etiketlerini kaldır
from bs4 import BeautifulSoup
html_text="<div>Hello,World 2035 </div>"
# beatiful soup ile html yapısını parse et , get-text ile text kısmını çek
cleaned_text6=BeautifulSoup(html_text,"html.parser").get_text()



















