#!/usr/bin/env python
# coding: utf-8

# # Pandas_Lib

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# # Load DataSeries

# In[3]:


a = [1,2,3,4,5,6,7]
dataset = pd.Series(a)
print(dataset)


# # Loading Data-Frames

# In[4]:


b = {"Games":["League","Valvorant","TFT"],"Champs":["Yasou","Nova","Pengu"]}
dataset = pd.DataFrame(b)
print(dataset)


# # Loading Dataset from files

# In[6]:


data1 = pd.read_csv("dataset.csv")
print(data1.head(5))


# In[8]:


data2 = pd.read_excel("dataset.xlsx")
print(data2.head(10))


# In[9]:


data3 = pd.read_csv("dataset.txt")
print(data3.tail(10))


# # Dataset Details

# In[13]:


print(data1.shape)
print(data1.describe())


# # Dataset Slicing

# In[19]:


print(data1.columns)
print(data1["Name"])
print(data1[["Name","Attack"]])
print(data1["Name"][0:6])


# In[23]:


print(data1.iloc[27])
print(data1.iloc[1:10])
print(data1.iloc[1,4])


# In[25]:


for index, row in data1.iterrows():
    print(index,row["Name"])


# # Dataset Slicing with Filter

# In[26]:


print(data1.loc[data1["Speed"] > 90])


# # Sorting - Slicing Data

# In[30]:


data1.sort_values(["HP"],ascending = False)


# # Editing Data

# In[31]:


data1["Power"] = data1["HP"] + data1["Speed"]
print(data1.head(10))


# # Exporting it as new Dataset 

# In[33]:


data1.to_csv("newdata1.csv")


# # Checking null values

# In[34]:


data1.isna().any()


# # Aqcuring Dataset without NaN values

# In[35]:


data1 = data1[data1["Type 2"].notna()]


# # Filling NaN values with the mean values of the column

# In[37]:


meandata = data1["Speed"].fillna(data1["Speed"].mean())
meandata


# # Mapping Certain data to another value

# In[39]:


print(data1.head(5))
Generation = set(data1["Generation"])
data1['Generation'] = data1['Generation'].map({1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six"}).astype(str)
print(data1.head(5))


# In[ ]:




