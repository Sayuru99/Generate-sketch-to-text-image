import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

text = open(r'text.txt',
            mode = 'r', encoding = 'utf-8').read() 
 
# The Image shape in which you wanna convert it to.
mask = np.array(Image.open(
                r'test.jpg'))

def one_color_func(word=None, font_size=None, 
                   position=None, orientation=None, 
                   font_path=None, random_state=None):
    h = 0 # 0 - 360
    s = 0 # 0 - 100
    l = 0 # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, l)


wc = WordCloud(stopwords = STOPWORDS,
               mask = mask,
               background_color = "white",
               collocations=False,
               max_words = 2000,
               max_font_size = 18,
               random_state = 42,
               color_func=one_color_func,
               width = mask.shape[1],
               height = mask.shape[0])


wc.generate(text) 
plt.imshow(wc, interpolation = "None")
 
# Off the x and y axis
plt.axis('off') 
 
# Now show the output cloud
plt.show()