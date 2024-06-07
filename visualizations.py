import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from corpus_reader import text_deb_1, text_deb_2, text_deb_3
 
#TODO create visualizations per debate, per candidate and in general

text_deb_gen = text_deb_1 + text_deb_2 + text_deb_3

def wordclouds(texts):
    for text in texts:
        wordcloud = WordCloud(width = 1600, height = 800,
                        background_color ='white',
                        min_font_size = 10,
                        colormap = "bone",
                        collocations = False
                        ).generate(text)
        # plot the WordCloud image                       
        plt.figure(figsize = (16, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        
        plt.show()

wordclouds([text_deb_gen])




