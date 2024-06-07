from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('spanish'))

with open("corpus/primer_debate.txt", "r") as file1:
  deb_1 = file1.read()

with open("corpus/segundo_debate.txt", "r") as file2:
  deb_2 = file2.read()

with open("corpus/tercer_debate.txt", "r") as file3:
  deb_3 = file3.read()

claudia = "Claudia Sheinbaum Pardo:"
maynez = "Jorge Álvarez Máynez:"
xochitl = "Bertha Xóchitl Gálvez Ruiz:"

deb_1_tokens = word_tokenize(deb_1.lower())
filtered_text = [word for word in deb_1_tokens if not word in stop_words]
print(filtered_text)


