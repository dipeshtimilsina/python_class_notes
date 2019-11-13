#!/usr/bin/env python
# coding: utf-8

# ### Dictionaries and json

# In[1]:


dict_1 = {
    'name':'Ram'
}


# In[2]:


from json import loads,dumps


# In[3]:


dumps(dict_1)


# In[6]:


str_json = '{"name":"Ram"}'


# In[7]:


loads(str_json)


# In[12]:


dict_1 = loads(str_json)


# In[13]:


dict_1['name']


# ### Random Package

# In[14]:


import random


# In[17]:


random.randint(1,100)


# In[18]:


random.random()


# In[19]:


list_1 = [1,2,3,4,5,6]


# In[20]:


random.choice(list_1)


# ### Date Time Package

# In[22]:


from datetime import datetime as dt


# In[24]:


dt.now()


# In[28]:


x= dt.now()
x.year


# In[29]:


print(x.year)
print(x.strftime("%A"))


# In[30]:


x.strftime("%a")


# In[33]:


x.strftime("%B")


# In[34]:


x.strftime("%Y-%m-%d")


# ### File Handling

# In[36]:


file = open('test.txt','w')


# In[41]:


file.write("Text Written From Python")


# In[42]:


file.close()


# In[53]:


file = open('test.txt','w')


# In[54]:


list_str = [f"line_{x}\n" for x in range(5)]


# In[55]:


list_str


# In[56]:


file.writelines(list_str)


# In[57]:


file.close()


# In[58]:


file = open('test.txt','r')


# In[59]:


for lines in file:
    print(lines)


# In[67]:


file = open('test.txt','r+')


# In[68]:


file.readlines()


# In[69]:


file.tell()


# In[70]:


file.readlines()


# In[71]:


file.write("Something")


# In[72]:


file.close()


# ### OS Package

# In[73]:


import os


# In[75]:


os.getcwd()

