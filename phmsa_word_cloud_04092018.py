
# coding: utf-8

# Internet page with example for doing wordcloud in python:
# 
# https://www.kaggle.com/adiljadoon/word-cloud-with-python

# In[1]:


import pandas as pd
df1 = pd.read_csv('https://query.data.world/s/dv2xwja6ue6tmbcqbst5dnilexrip4')
# dataset is at kaggle - https://data.world/webmadster/phmsa-hazardous-liquid-accident-data-since-2010


# In[2]:


df1.head()


# In[3]:


df1.columns


# In[4]:


df1['NARRATIVE'].head(3)


# In[5]:


df1['NARRATIVE'].iloc[1:10]


# In[6]:


narr = []
for text in df1['NARRATIVE']:
    narr.append(text)


# In[7]:


narr[0]


# In[9]:


get_ipython().system('pip install wordcloud')


# In[10]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS


# In[11]:


get_ipython().system('pip install wordcloud')


# In[12]:


mpl.rcParams['font.size']=12                
mpl.rcParams['savefig.dpi']=100             
mpl.rcParams['figure.subplot.bottom']=.1


# In[13]:


stopwords = set(STOPWORDS)


# In[14]:


data = pd.DataFrame(narr)


# In[15]:


data[0]


# In[16]:


wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(str(data[0]))


# In[17]:


print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=900)

