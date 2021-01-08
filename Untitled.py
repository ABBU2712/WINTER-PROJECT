#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


Genres=pd.read_csv("genres_v2.csv",
)


# In[4]:


Genres.head()


# In[5]:


Features=Genres


# In[6]:


import re


# In[7]:


Features.replace(' ', '_' , regex = True, inplace = True)


# In[8]:


Features.head()


# In[9]:


Genres.replace(' ', '_' , regex = True, inplace = True)


# In[10]:


Genres.head()


# In[17]:


Features.head()


# In[18]:


Features.drop(['type','title','Unnamed: 0'],axis=1,inplace=True)


# In[19]:


Features.head()


# ## NORMALIZATION / STANDARDIZATION
# 

# In[23]:


from sklearn.preprocessing import MinMaxScaler


# In[24]:


scaler = MinMaxScaler()


# In[25]:


df_norm = pd.DataFrame(scaler.fit_transform(Features), columns=Features.columns)


# In[26]:


Feat_2=Features


# In[27]:


Feat_2.drop(['genre'],axis=1,inplace=True)


# In[28]:


Feat_2.head()


# In[29]:


df_norm = pd.DataFrame(scaler.fit_transform(Feat_2), columns=Feat_2.columns)


# In[30]:


df_norm.head()


# In[50]:


NewGen=pd.read_csv("genres_v2.csv",)
NewGen.head()
Join=NewGen['genre']
Join.head()


# ## BIVARIATE ANALYSIS
# 

# In[59]:


sns.FacetGrid(df_norm,hue="genre",size=10).map(plt.scatter,"danceability","energy").add_legend()


# ## MULTIVARIATE ANALYSIS

# In[61]:


sns.pairplot(df_norm,hue="genre",size=5)


# In[ ]:




