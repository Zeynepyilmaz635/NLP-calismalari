

text="Cumhurbaşkanı Recep Tayyip Erdoğan, dün Ankara'da düzenlenen toplantıda yaptığı konuşmada, Türk Hava Yolları'nın yeni uçak alımlarını duyurdu. İstanbul Büyükşehir Belediyesi'nin yeni metro hattı için Avrupa Yatırım Bankası'ndan kredi alacağı açıklandı. Toplantı 15 Şubat 2024 tarihinde yapıldı."
# boşlkları temzledik
cleaned_text=" ".join(text.split())

# büyük -> küçük harf
cleaned_text=cleaned_text.lower()

# noktalama işaretlerini kaldır
import string 
cleaned_text=cleaned_text.translate(str.maketrans("","",string.punctuation))

#  yazım hatası düzltme
"""
from textblob import TextBlob
cleaned_text = str(TextBlob(cleaned_text).correct()) 
"""


#  TOKENİZASYON
import nltk
nltk.download('punkt') 
nltk.download('punkt_tab')

word_tokenize=nltk.word_tokenize(cleaned_text)






#  STOP WORDS
from nltk.corpus import stopwords
nltk.download("stopwords")

stop_words_tr=set(stopwords.words("turkish"))
filtred_word=[w for w in word_tokenize if w not in stop_words_tr]





new_text=" ".join(filtred_word)





from transformers import pipeline

# Türkçe için hazır Named Entity Recognition (NER) modeli
ner_pipeline = pipeline("ner", model="savasy/bert-base-turkish-ner-cased")
ner_results = ner_pipeline(text)

entities = {"Kişi": [], "Organizasyon": [], "Şehir": []}
entity_labels = {"B-PER": "Kişi", "I-PER": "Kişi", "B-ORG": "Organizasyon", "I-ORG": "Organizasyon", "B-LOC": "Şehir", "I-LOC": "Şehir"}



for entity in ner_results:
    label = entity_labels.get(entity["entity"], None)
    if label:
        entities[label].append(entity["word"])

# Çıkarılan bilgileri ekrana yazdırma
for category, names in entities.items():
    print(f"{category}: {', '.join(set(names))}")



















