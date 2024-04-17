#!/usr/bin/env python
# coding: utf-8

# # Zomato Dataset Exploratory Data Analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


zd=pd.read_csv(r"C:\Users\ASUS\Desktop\Data science\DS-Python\DS-Python Projects\Zomatodatset\zomato.csv",encoding='latin')
zd.head()


# In[3]:


zd.columns


# In[4]:


zd.info()


# In[5]:


zd.describe()


# In[6]:


zd.isnull().sum()


# In[7]:


[features for features in zd.columns if zd[features].isnull().sum()>0]


# In[8]:


zd_country=pd.read_excel(r"C:\Users\ASUS\Desktop\Data science\DS-Python\DS-Python Projects\Zomatodatset\Country-Code.xlsx")
zd_country.head()


# In[9]:


final_df=pd.merge(zd,zd_country,on='Country Code', how='left')


# In[10]:


final_df.head(2)


# In[11]:


final_df.dtypes


# In[12]:


country_name=final_df.Country.value_counts().index
country_name


# In[13]:


country_value=final_df.Country.value_counts().values


# In[14]:


# Pie Chart for top 3 country 
plt.pie(country_value[:3],labels=country_name[:3] , autopct="%1.2f%%")


# Observation: Zomato maximum records or transaction are from india after that USA and then UK

# In[15]:


final_df.columns


# In[16]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})
ratings


# # Observation:
#     - when rating is between 4.5 to 4.9----> Excellent
#     - when rating is between 4.0 to 4.4----> Very Good
#     - when rating is between 3.5 to 3.9----> Good
#     - when rating is between 2.5 to 3.4----> Average
#     - when rating is between 1.8 to 2.4----> Poor

# In[17]:


plt.figure(figsize=(7,7))
sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color',data=ratings)


# ### Obeservation:
# - 1) Not Rated count is very high
# - 2) maximum number of rating are between 2.5 to 3.4

# In[18]:


## count plot 
sns.countplot(x='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[19]:


# Country name that has given 0 rating
final_df[final_df['Aggregate rating']==0].groupby('Country').size().reset_index()


# Observation:
# maximum number of 0 ratings are form indian customer

# In[20]:


final_df.columns


# In[21]:


# which currency is use by which country
final_df.groupby(['Country','Currency']).size().reset_index()


# In[22]:


# country having online delivery
final_df[final_df['Has Online delivery']=='Yes'].groupby(['Country']).size().reset_index()


# Observation:
#     online delivery are available in India and UAE

# In[23]:


cities_name=final_df['City'].value_counts().index
cities_name


# In[24]:


cities_value=final_df['City'].value_counts().values
cities_value


# In[26]:


plt.pie(x=cities_value[:5], labels=cities_name[:5],data=final_df,autopct="%1.2f%%")


# Obervation:
#     New Delhi has highest number of transaction then Gurgaon then Noida and then Ghaziabad Faridabad

# In[30]:


# top 10 cuisines
cuisines_name=final_df.Cuisines.value_counts().index
cuisines_name


# In[33]:


cuisines_value=final_df.Cuisines.value_counts().values
cuisines_value


# In[36]:


plt.pie(x=cuisines_value[:10],labels=cuisines_name[:10],data=final_df,autopct="%1.2f%%")


# In[ ]:




