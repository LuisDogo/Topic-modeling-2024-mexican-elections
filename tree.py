from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('spanish'))
texto = "Hola, ¿Cómo estás?"
texto_2 = "El gato es negro y el perro es blanco"
tokens = word_tokenize(texto_2.lower())
# print(tokens)
filtered_text = [word for word in tokens if not word in stop_words]
print(filtered_text)


