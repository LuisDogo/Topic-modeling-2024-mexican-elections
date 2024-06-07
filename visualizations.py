import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from corpus_reader import text_deb_1, text_deb_2, text_deb_3
 
#TODO create visualizations per debate, per candidate and in general

general_text = text_deb_1 + text_deb_2 + text_deb_3

wordcloud = WordCloud(width = 1600, height = 800,
                background_color ='white',
                min_font_size = 10,
                colormap = "bone",
                collocations = False
                ).generate(general_text)
 
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()




