
import nltk
nltk.download('punkt') 
nltk.download('punkt_tab')
# Örnek bir metin
text = "Hello, World! How are you? Hello, hi ..."

# Kelime tokenizasyonu (word_tokenize): Metni kelmelere ayırır
word_tokens = nltk.word_tokenize(text)

# Cümle tokenizasyonu (sent_tokenize): Metni cümlelere ayırır
sentence_tokens = nltk.sent_tokenize(text)

# Kelime tokenleri
print("Kelime Tokenleri:")
print(word_tokens)

# Cümle tokenleri
print("\nCümle Tokenleri:")
print(sentence_tokens)
