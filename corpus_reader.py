from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def add_stopwords(structure):

    with open("stopwords.txt", 'r') as f:
        words = f.readlines()

    words = [word.strip() for word in words]

    for word in words:
        structure.add(word)


stop_words = set(stopwords.words('spanish'))
add_stopwords(stop_words)

#TODO creating a filtered corpus per candidate

with open("corpus/primer_debate.txt", "r") as file1:
  deb_1 = file1.read()

with open("corpus/segundo_debate.txt", "r") as file2:
  deb_2 = file2.read()

with open("corpus/tercer_debate.txt", "r") as file3:
  deb_3 = file3.read()

mods_1 = ["moderadora, denise maerker:", "moderador, manuel lópez san martín:"]
mods_2 = ["moderadora, adriana pérez cañedo:", "moderador, alejandro cacho:"]
mods_3 = ["moderadora, carmen elena arcila solís:", "moderador, javier solórzano zinser:"]
claudia = "Claudia Sheinbaum Pardo:"
maynez = "Jorge Álvarez Máynez:"
xochitl = "Bertha Xóchitl Gálvez Ruiz:"

deb_1_tokens = word_tokenize(deb_1.lower())
deb_2_tokens = word_tokenize(deb_2.lower())
deb_3_tokens = word_tokenize(deb_3.lower())

filtered_deb1 = [word for word in deb_1_tokens if not word in stop_words]
text_deb_1 = ' '.join(filtered_deb1)

filtered_deb2 = [word for word in deb_2_tokens if not word in stop_words]
text_deb_2 = ' '.join(filtered_deb2)

filtered_deb3 = [word for word in deb_3_tokens if not word in stop_words]
text_deb_3 = ' '.join(filtered_deb3)

