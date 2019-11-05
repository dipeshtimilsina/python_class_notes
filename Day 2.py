#!/usr/bin/env python
# coding: utf-8

# ## Datatypes Continued
# ### List

# In[1]:


list_1 = ['ktm','Pokhara','Bhaktapur']


# In[2]:


print (list_1)


# In[3]:


list_1[0]


# In[4]:


type(list_1)


# In[5]:


list_1[-3]


# In[6]:


list_1[1] = 'Lalitpur'


# In[7]:


list_1


# In[9]:


list_1.remove('Lalitpur')


# In[10]:


list_1


# In[11]:


del list_1[1]


# In[12]:


list_1


# In[13]:


len(list_1)


# In[17]:


list_2 = [2,4,6,8,10]


# In[18]:


min(list_2)


# In[19]:


sum(list_2)


# In[21]:


list_1.append('Baluwatar')


# In[22]:


list_1


# In[23]:


list_1.append('pokhara')


# In[24]:


list_1


# In[27]:


list_1.count('pokhara')


# In[28]:


list_1.index('pokhara')


# In[41]:


list_1.insert(1,'Kirtipur')


# In[42]:


list_1


# In[43]:


list_1.reverse()


# In[44]:


list_1


# In[45]:


list_1_copy = list_1.copy()


# In[46]:


list_1_copy


# ### slicing of List
# ##### list[start: upto: step]

# In[48]:


list_2


# In[50]:


list_2_sliced=list_2[2::2]


# In[51]:


list_2_sliced


# ### Tuple

# In[52]:


tuple_1 = (1,2,3,4,5)


# In[53]:


type(tuple_1)


# In[54]:


tuple_1[2]


# In[55]:


tuple_1[2:4]


# ### Set

# In[56]:


set_1 = {1,2,3,4,5}


# In[57]:


type(set_1)


# ### Type Conversion

# In[61]:


a='5'


# In[62]:


type(a)


# In[63]:


integer=int(a)


# In[64]:


type(integer)


# In[65]:


type(a)


# In[66]:


list_1


# In[67]:


tup_1 = tuple(list_1)


# In[68]:


tup_1


# ### Dictionaries

# In[69]:


dict_1 = {
    'key1':'value1',
    'key2':'value2'
}


# In[70]:


dict_1


# In[71]:


dict_1['key1']='new_value'


# In[72]:


dict_1


# In[74]:


dict_2 ={
    'key4':'value4',
    'key5':'value5'
}


# In[75]:


dict_2


# In[77]:


dict_1.update(dict_2)


# In[78]:


dict_1


# In[79]:


dict_1.keys()


# In[81]:


dict_1.items()


# In[82]:


dict_1.values()


# ### Multiple statement and multiple assignment

# In[83]:


print('hello');dict_1.keys()


# In[84]:


a=b=1


# In[85]:


a,b = 1,2


# In[86]:


print(a,b)


# ### Tuple Unpacking

# In[88]:


tuple_new =(1,2,3)


# In[89]:


x,y,z = tuple_new


# In[90]:


x


# In[91]:


y


# In[92]:


z

