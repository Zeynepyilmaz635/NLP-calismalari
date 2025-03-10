# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 00:46:18 2025

@author: pc
"""

"""
# metinlerde bulunan fazla boşlkları ortadan kaldır
# büyük -> küçük harf çevrimi
# noktlama işaretlerini kaldır
# özl karakterleri kaldır
# yazım hatalarını düzlt
# html url etiketlerini kaldır
"""


# metinlerde bulunan fazla boşlkları ortadan kaldır
text="Hello,    WOrLd!     2035   "
cleaned_text1=" ".join(text.split())
print("boşukların temizlendiği text : " ,cleaned_text1)


# büyük -> küçük harf çevrimi
cleaned_text2=cleaned_text1.lower()
print("büyük harflerin küçük harflere çevrilmiş hali : " ,cleaned_text2)



# noktlama işaretlerini kaldır
import string
cleaned_text3=cleaned_text2.translate(str.maketrans("","",string.punctuation))
print("noktalama işaretlerinin kaldıırlmş hali : ",cleaned_text3)


# özl karakterleri kaldır : % @ / * & .............
import re
text2="hello, World! 2035 ^ %"
cleaned_text4=re.sub(r"[^A-Za-z0-9\s]","",text2)
# A dan Z e ye kadr a dan z e ye kadr 0 dan 9 a kadr olanların (^) haricindekileri kaldır
print("özl karakterleri kaldırlmş hali : ",cleaned_text4)


# yazım hatalarını düzlt
from textblob import TextBlob # metn analizlerinde kullanılan bir kütüphane
text3="Hellio, Wirld! 2035"
cleand_text5=TextBlob(text3).correct()
# correct : yazım hatalarını düzltir textblob : metni işler
print("yazım hatalarını düzltilmş hali : ",cleand_text5)


# html url etiketlerini kaldır
from bs4 import BeautifulSoup

html_text="<div>Hello, World! 2035 </div>"
cleaned_text6=BeautifulSoup(html_text,"html.parser").get_text()
# beatifulsoup :html yapısını  parse et  , get_text ile text kısmını çek
print("html url temzlnmş hali : " ,cleaned_text6)












































































































