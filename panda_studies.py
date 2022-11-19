#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('Iris.csv') #importing file to be read by pandas
df.shape


# In[5]:


# PRESENTING PANDA DATASETS IN SERIES STYLE
import pandas as pd
names = pd.Series (['hanna','jack','emma','sifon','praise','joe'], index=['a','b','c','d','e','f']) #panda Series
names


# In[10]:


#PRESENTING PANDA DATASETS AS DATAFRAME STYLE
import pandas as pd
names = pd.Series(['jack','emma','godfirst','dan','lucy'])
department = pd.Series(['mls','law','nursing','mmp','eng'])
cgpa = pd.Series(['3.5','4.5','3.9','2.9','5.0'])
data = pd.DataFrame({'Names': names, 'Department': department, 'CGPA': cgpa})
data


# In[12]:


#Second method for DataFrame style
import pandas as pd
Amount = pd.Series(['12,000','40,000','50,000','100,000'])
Data = pd.DataFrame({'Students':['jack','helen','jean','lucy'], 'Department':['mls','eng','nursing','law']})
Data['Amount'] = ['12,000','40,000','50,000','100,000']
Data


# In[19]:


import pandas as pd
jj = pd.read_csv('Iris.csv')
jj.head(10) #reading the first 10  item in an imported file


# In[22]:


import pandas as pd
jj = pd.read_csv('Iris.csv')
jj.tail(10)


# In[23]:


# add a row to Dataframe in Python using Pandas; By using DataFrame.append() method
import pandas as pd
new_value = ([('john','1985','korea'),('ime','7764','singapore'),('udo','7663','')])
gg = pd.DataFrame(new_value)
gg = colum
print(gg)

