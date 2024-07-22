#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[12]:


data=pd.read_csv((r"C:\Users\alamm\Downloads\apple_products.csv"))


# In[13]:


data


# In[14]:


print(data.isnull().sum())


# In[15]:


print(data.describe())


# # i phone sales analysis in India

# In[16]:


highest_rated=data.sort_values(by=["Star Rating"],ascending =False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])


# # lets have a look at the number of ratings of the highest rated i phone on flipkart

# In[22]:


iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated,x=labels,y=counts,title="Number of ratings of highest rated i phones")
figure.show()


# In[23]:


iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated,x=labels,y=counts,title="Number of ratings of highest rated i phones")
figure.show()


# In[25]:


figure=px.scatter(data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",title="Relationship between sale price and number of rating")
figure.show()


# In[28]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",title="Relationship between discount Percentage and number of rating")
figure.show()


# In[ ]:




