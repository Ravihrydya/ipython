#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy
import requests
from bs4 import BeautifulSoup


# In[10]:


url="https://www.flipkart.com/search?q=hp+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=hp+laptop%7CLaptops&requestId=49067afc-5202-4240-8b32-923f91310a97&as-searchtext=hp%20"


# In[11]:


url_data=requests.get(url)


# In[12]:


url_data.content


# In[13]:


soup=BeautifulSoup(url_data.content,"html.parser")


# In[14]:


soup.prettify()


# In[8]:


product_name=[]


# In[15]:


for x in range(6):
    for item in soup.find_all("div",class_="_4rR01T"):
        product_name.append(item.text)


# In[20]:


print(product_name)


# In[17]:


product_price=[]


# In[18]:


for x in range(6):
    for item in soup.find_all("div",class_="_30jeq3 _1_WHN1"):
        product_price.append(item.text)
        


# In[19]:


print(product_price)


# In[25]:


laptopdata=pd.DataFrame({"Laptop_Name":product_name,"Price":product_price})


# In[26]:


laptopdata


# In[28]:


laptopdata.to_excel('Hp_laptop.xlsx')


# In[ ]:




