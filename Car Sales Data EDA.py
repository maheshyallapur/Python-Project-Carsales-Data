#!/usr/bin/env python
# coding: utf-8

# ## Table of Contents ##
# 
# 1. Problem Statement
#     - 1.1 [Introduction]
#     - 1.2 [Data source and data set]
# 2. Load the Packages and Data
# 3. Data Profiling
#     - 3.1 [Understanding the Dataset]
#     - 3.2 [Preprocessing]
#     - 3.3 [Post Profiling]
# 4. Questions
#     - 4.1 [Which type of cars are sold maximum?]
#     - 4.2 [What is the co-relation between price and mileage?]
#     - 4.3 [How many cars are registered?]
#     - 4.4 [Price distribution between registered and non-registered cars.]
#     - 4.5 [What is the car price distribution based on Engine Value?]
#     - 4.6 [Which Engine Type of cars users preferred maximum?]
#     - 4.7 [Establish corelation between all features using heatmap.]
#     - 4.8 [Distribution of Price]   
# 5. [Conclusions]

# ### 1. Problem Statement ##
# 
# "This dataset contains data for more than 9.5K cars sale in Ukraine.Most of them are used cars so it opens the possibility to analyze features related to car operation. This is a subset of all car data in Ukraine. Using this We will analyze the various parameters of used car sales in Ukraine."
# 
# ### 1.1. Introduction ##
# This Exploratory Data Analysis is to practice Python skills learned  on a structured data set including loading, inspecting, wrangling, exploring, and drawing conclusions from data. The notebook has observations with each step in order to explain thoroughly how to approach the data set. Based on the observation some questions also are answered in the notebook for the reference though not all of them are explored in the analysis. 
# 
# 
# ### 1.2. Data source and dataset
# 
# __a__. How was it collected? 
# 
# - __Name__: "Car Sales"
# - __Sponsoring Organization__: Don't know
# - __Year__: 2022 
# - __Description__: "This is a case study of more than 9.5K cars sale in Ukraine."  
# 
# __b__. Is it a sample? If yes, was it properly sampled?
# - Yes, it is a sample. We don't have official information about the data collection method, but it appears *not* to be a random sample, so we can assume that it is not representative.

# ### 2.  Load the Packages and Data ##

# Importing Packages

# In[3]:


import numpy as np                                                 # Implemennts milti-dimensional array and matrices
import pandas as pd                                                # For data manipulation and analysis
import matplotlib.pyplot as plt                                    # Plotting library for Python programming language and it's numerical mathematics extension NumPy
import seaborn as sns                                              # Provides a high level interface for drawing attractive and informative statistical graphics
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()
from subprocess import check_output 


# Loading Dataset 

# In[4]:


carsales_data=pd.read_excel(r"D:\10th Jan FSDA(EDA)\EDA\Car_Sales.xlsx")


# In[6]:


carsales_data.shape


# In[7]:


carsales_data.head()


# In[8]:


carsales_data_copy=carsales_data.copy()


# In[9]:


carsales_data_copy.head()


#  ### 3. Data Profiling

#  3.1 Understanding the Dataset

# In[12]:


carsales_data_copy.shape


# In[13]:


carsales_data_copy.columns


# In[14]:


carsales_data_copy.describe()


# In[15]:


carsales_data_copy.describe(include="all")


# In[16]:


carsales_data_copy.sort_values(by=['price'],ascending=False).head()


# In[17]:


carsales_data.groupby('car')['price'].count().sort_values(ascending=False)


# In[18]:


carsales_data['car'].value_counts().head()


# In[20]:


carsales_data['car'].value_counts(normalize=True) * 100


# ## Insight ##
# 
# It has been observed that top 3 selling cars are: Volkswagen,Mercedes-Benz and BMW                     
# 

# In[21]:


carsales_data.corr()


# In[22]:


plt.subplots(figsize=(10,20))
sns.heatmap(carsales_data.corr(),annot=True)


# In[24]:


sns.boxplot(data=carsales_data.engV)


# In[25]:


carsales_data.info()


# In[26]:


carsales_data.isnull().sum()


# From the above output we can see that engV and drive contains maximum null values

# ### 3.2 Preprocessing

# In[ ]:


1. Fill missing and Null Values
2.Filling of Null and missing values
3.Dealing with duplicate rows
    - Find number of duplicate rows in the dataset.
    - Print the duplicate entries and analyze.
    - Drop the duplicate entries from the dataset.


# Finding Null Values

# In[28]:


miss1=carsales_data.isnull().sum()
miss=(carsales_data.isnull().sum()/len(carsales_data))*100
missing_data=pd.concat([miss1,miss],axis=1,keys=['Total','%'])
print(missing_data)


# Finding Duplicate Values

# In[30]:


carsales_data.duplicated().sum()


# In[31]:


carsales_data.loc[carsales_data.duplicated(),:]


# Removing Duplicates

# In[32]:


carsales_data.drop_duplicates(inplace=True)


# In[33]:


carsales_data.loc[carsales_data.duplicated(),:]


# Duplicate entries are removed now.

#  Filling Missing Values

# In[34]:


b=carsales_data['drive'].mode()
b


# In[35]:


carsales_data['drive']=carsales_data['drive'].fillna("front")


# In[36]:


carsales_data.isnull().sum()


# In[37]:


carsales_data.loc[carsales_data.duplicated(keep=False),:]


# In[39]:


carsales_data.drop_duplicates(keep='first').shape ## keeps first occuring data


# In[43]:


carsales_data['engV'] = carsales_data.groupby(['car', 'body'])['engV'].transform(lambda x: x.fillna(x.median()))


# In[ ]:


- Dealing with missing values
    - __434__ missing entries of __engV.__ Replace it with __median__ value of engV from the same Car and body group of cars.
    - __511__ missing entries of __drive.__ Replace it with __most common__ value of drive from the same Car and body group of cars.
    - Drop entries having __price__ is 0 or less than 0.


# In[44]:


carsales_data.isnull().sum()


# In[45]:


carsales_data[carsales_data.engV.isnull()]


# In[47]:


carsales_data.dropna(subset=['engV'],inplace=True)


# In[48]:


carsales_data.isnull().sum()


# In[59]:


carsales_data=carsales_data.drop(carsales_data[carsales_data.price<=0].index)


# In[60]:


carsales_data.price[carsales_data.price ==0].count()


# In[61]:


b = carsales_data["mileage"].median()
carsales_data["mileage"]=carsales_data["mileage"].replace(0,b)


# In[62]:


carsales_data[carsales_data.mileage==0]


#  ## Questions
#  
# 

# ## Which type of cars are sold maximum? 

# In[63]:


carsales_data.groupby('car')['price'].count().sort_values(ascending=False)


# In[64]:


carsales_data['car'].value_counts()


#  It has been observed that top 3 selling cars are Volkswagen,Mercedes_Benz and BMW

# ## What is the co-relation between price and mileage?

# In[65]:


sns.regplot(x='mileage',y='price',data=carsales_data)


# Insights
# 
# * It Seems that Majority of car price is below 150000 and gives mileage in the range of 0 to 400

# ## How many cars are registered? ##
# 

# In[66]:


sns.countplot('registration',data=carsales_data).set_title('Car Registration Status')


# In[67]:


carsales_data['registration'].value_counts()


# In[ ]:


Insights

* 8000+ cars are registered and very few not registered


# ## Price distribution between registered and non-registered cars ##
# 

# In[68]:


carsales_data.groupby(['registration','body'])['price'].mean()


# In[69]:


sns.boxplot(x='registration',y='price',data=carsales_data)


# In[ ]:


Insights

* Majority of the Cars were Registered and Price of those cars are bewlow 300000
* Non-Registered cars were cheaper in cost


# In[70]:


sns.displot(data=carsales_data,x='registration',y='price')


# ## What is the car price distribution based on Engine Value?
# 

# In[71]:


sns.regplot(x='engV',y='price',data=carsales_data)


# Insights
# 
# * Except few outliers , it is clearly observed that the range of car price is between 0 to 150000 having the
# range of engine Value between 0 to 6

# In[72]:


sns.scatterplot(x='engV',y='price',data=carsales_data,hue='body')


# In[73]:


sns.relplot(x='engV',y='price',data=carsales_data)


# In[ ]:


Insights

* Except few outliers , it is clearly observed that the range of car price is between 0 to 150000 having the
range of engine Value between 0 to 6


# ## Which Engine Type of cars users preferred maximum?   
# 

# In[74]:


sns.countplot(carsales_data['engType'])


# In[ ]:


Insights
* Petrol cars are more preferred and followed by Diesel,Gas and Others


# In[75]:


carsales_data.groupby('engType')['price'].count().sort_values(ascending=False)


#  ## Establish corelation between all features using heatmap
# 

# In[77]:


corr_sales=carsales_data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_sales,vmax=0.8,linewidth=0.01,square=True,cmap='coolwarm_r',linecolor='black')
plt.title('correlation between Features')


# In[78]:


carsales_data.corr()


# In[ ]:


Insights
* mileage and engV are negatively correlated with year
* engV is positively correlated with mileage and Price
* positive correlation observed between year and price too


# ## Distribution of Price

# In[79]:


sns.displot(carsales_data['price'],color='g')
plt.title('Price Distribution')
plt.show()


# In[ ]:


Insights
* The Price mostly varies between 0 to 8000


# In[80]:


sns.distplot(carsales_data['price'],color='g',kde=False)


# ## Conclusion
# 
# * Sedan cars sold maximum
# * Price is increasing as the Engine Value is increasing
# * Price and Mileage goes down Engine Value is decreasing

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




