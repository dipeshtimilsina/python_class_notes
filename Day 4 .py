#!/usr/bin/env python
# coding: utf-8

# ### Loops in Python

# ### For Loop

# In[6]:


list_1 = [1,2,3,4,5]


# In[7]:


for i in list_1:
    print(i)


# In[9]:


hello = 'hello'
for character in hello:
    print (character)


# In[11]:


list_2 = [1,2,3,4,5]
sum_list = 0
for num in list_2:
    sum_list += num
print(f'Sum is : {sum_list}')


# In[13]:


for i in list_2:
    print ('hello')


# In[14]:


range_10 = range(10)


# In[15]:


type(range_10)


# In[16]:


list(range_10)


# In[18]:


for i in range (5):
    for j in range (100,105):
        print(f"i -> {i} and j -> {j}")
    print("inside i loop")


# # Solving Questions

# ### Generate a list and tuple with comma-seperated number string

# In[24]:


a = "1,2,3,4,5"
new_list = a.split(",")


# In[25]:


tuple(new_list)


# ### Convert a list of characters into a string

# In[27]:


a= ["a","b","c","d","e"]
"".join(a)


# ### Write a Python program to unpack a tuple in several variables.

# In[29]:


x,y,z = (1,2,3)
print(f"x->{x},y->{y},z->{z}")


# ### Concatenate dictionaries to create a new one
# 

# In[31]:


d1 = {'key1':'value1'}
d2 = {'key2':'value2'}

d1.update(d2)
print(d1)


# ### Write a python program to determine if the variable is defined or not

# In[34]:


try:
    print(z)
except:
    print("Variable nor defined")


# In[42]:


nested_list = [1,2,[3,4],5]
for elements in nested_list:
    if type(elements) == type([]):
        print('Sunlist exists')


# In[ ]:




