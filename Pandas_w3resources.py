#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


lix = ['good', 'better', 'best']
liy = pd.Series(lix)


# In[3]:


liy


# In[5]:


liy = list(liy)


# In[7]:


type(liy)


# In[18]:


a1 = pd.Series([2, 4, 6, 8, 10]) 
a2 = pd.Series([1, 3, 5, 7, 9])


# In[12]:


a_sum = a1 + a2
a_sum = list(a_sum)
a_sum


# In[15]:


a_divide = a1/a2
a_divide = list(a_divide)
a_divide


# In[19]:


a1 == a2


# In[20]:


lix = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
liw = pd.Series(lix)
liw


# In[ ]:


# QUESTION:
# Write a Pandas program to change the data type of given a column or a Series. 
# alia = pd.Series([100, 200, 'Python', 300.12, 400]) change from object to floating


# In[21]:


s1 = pd.Series([100, 200, 'Python', 300.12, 400])


# In[22]:


s2 = pd.to_numeric(s1, errors='coerce')
s2


# In[27]:


x1 = pd.Series([100, 200, 'Python', 300.12, 400])
x1


# In[29]:


x2 = np.array(x1)
type(x2)


# In[30]:


x1


# In[33]:


x2 = pd.to_numeric(x1, errors = 'coerce')
x2


# In[34]:


x2.sort_values()


# In[35]:


x1


# In[44]:


x3 = x2.append(pd.Series(['PHP', 500]))
x3


# In[46]:


x1


# In[49]:


g1 = pd.Series(['python', 'java', 'php', 'c#'])


# In[52]:


g1


# In[57]:


g1.apply(lambda x: x.title())


# In[58]:


y1 = pd.Series([1,2,3,4,5,6,7])
y1


# In[62]:


(y1.max())


# In[65]:


y1.index.min()


# In[ ]:




