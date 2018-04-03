import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from nltk.corpus import stopwords

# set stopwords
stop = stopwords.words('english')

# load csv file
df = pd.read_csv('sample_text.csv')

# generate text data
txt = ' '.join(df['headline_text'])

# generate wordcloud with stopwords
wc = WordCloud(stopwords=stop).generate(txt)

# save figure
plt.imshow(wc)
plt.axis("off")
plt.savefig('wordcloud.png')
