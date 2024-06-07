import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("escuchar, escuchó, escucha, estuche, estuchera, camina, caminar, camino, caminaría, caminé")
for token in doc:
    print(token.text, "->", token.lemma_)