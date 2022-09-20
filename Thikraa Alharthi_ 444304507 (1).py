#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


dataset = pd.read_csv("educ_figdp_1_Data.csv")


# In[23]:


dataset


# In[24]:


import pandas as pd 


# In[25]:


dataset = pd.read_csv("educ_figdp_1_Data.csv",
                     na_values =':',
                     usecols =["TIME","GEO","Value"])
dataset


# In[26]:


dataset.head()


# In[27]:


dataset.tail()


# In[28]:


dataset.describe()


# In[29]:


dataset['Value']


# In[30]:


dataset[10:14]


# In[35]:


dataset.loc [90:94, ['TIME','GEO']]


# In[36]:


dataset[dataset['Value'] > 6.5].tail()


# In[38]:


dataset[dataset["Value"].isnull()].head()


# In[39]:


dataset.max(axis =0)


# In[63]:



"pandas max function:",dataset['Value'].max()


# In[64]:


"python max function:",max(dataset['Value'])


# In[65]:


s = dataset['Value']/100
s.head()


# In[66]:


s = dataset["Value"].apply(np.sqrt)
s.head()


# In[68]:


s = dataset["Value"].apply(lambda d: d**2)
s.head()


# In[70]:


dataset["ValueNorm"]= dataset['Value']/dataset['Value'].max()
dataset.tail()


# In[71]:


dataset.drop('ValueNorm',axis = 1,inplace =True )
dataset.head()


# In[77]:


dataset =dataset.append({"TIME":2000 ,"Value":5.00 ,"GEO":'a'},
                       ignore_index =True
                       )
dataset.tail()


# In[86]:


dataset.drop(max(dataset.index),axis = 0,inplace =True )
                  
dataset.tail()


# In[91]:


datasetdrop = dataset.drop(dataset["Value"].isnull(),axis = 0)
                  
datasetdrop.head()


# In[90]:


datasetdrop = dataset.dropna(how = 'any' , subset = ["Value"])
datasetdrop.head()


# In[92]:


datasetfilled = dataset.fillna(value ={"Value":0})
datasetfilled.head()


# In[94]:


dataset.sort_values(by ='Value',ascending = False,
                   inplace =True)
dataset.head()


# In[96]:


dataset.sort_index(axis =0 ,ascending = True , inplace =True)
dataset.head()


# In[98]:


group = dataset[["GEO","Value"]].groupby('GEO').mean()
group.head()


# In[104]:


filtred_data =dataset[dataset["TIME"]>2005]
pivedu =pd.pivot_table(filtred_data,values ='Value',
                      index=['GEO'],
                      columns =['TIME'])
pivedu.head()


# In[109]:


pivedu.loc[['Spain','Portugal'],[2006,2011]]


# In[131]:


pivedu = pivedu.drop([
    'Euro area (13 countries)',
    'Euro area (15 countries)',
    'Euro area (17 countries)',
    'Euro area (18 countries)',
    'European Union (25 countries)',
    'European Union (27 countries)',
    'European Union (28 countries)'],
axis =0 )

pivedu = pivedu.rename(index = {'Germany (until 1990 former territory of The FRG )':'Germany'})
pivedu = pivedu.dropna()
pivedu.rank(ascending = False , method ='first').head()


# In[141]:


totalsum = pivedu.sum(axis =1)
totalsum.rank(ascending = False ,method ='dense')
totalsum.sort_values()


# In[143]:


totalSum = pivedu.sum (axis = 1 )

totalSum.plot (kind = 'bar',  style = 'b', alpha = 0.4,
               title = "Total Values for Conutry")


# In[145]:


my_colors = ['b', 'r', 'g', 'y', 'm', 'c',]
ax = pivedu.plot (kind = 'barh', 
                  stacked = True,
                  color = my_colors)
ax.legend(loc = 'center left', box_toanchor = (1, .5))


# In[ ]:





# In[ ]:





# In[ ]:




