#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sum_product (a,b):
    sum_ab = a+b
    product_ab= a*b
    return (sum_ab,product_ab)


# In[5]:


s,p = sum_product(3,4)
print(s,p)


# In[2]:


sum_product (2,3)


# In[6]:


s,p = sum_product (b=5, a=3)
print(s,p)


# In[7]:


def sum_product(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


# In[8]:


sum_product(1,2,3,4,5,a=5,b=6)


# In[13]:


def sum_product(*args, **kwargs):
    arg_sum= 0
    arg_prod= 1
    for i in args:
        arg_sum = arg_sum + i
        arg_prod = arg_prod * i
    return (arg_sum, arg_prod)


# In[14]:


sum_product(1,2,3,4,5,6)


# In[15]:


def sum_product(a=1,b=1):
    sum_ab = a+b
    prod_ab = a*b
    return (sum_ab, prod_ab)


# In[16]:


sum_product(5,6)


# ### Lambda Function
# #### Syntax
# lambda arguments : expression

# In[18]:


def sum_num(a,b):
    return a+b


# In[19]:


sum_num(1,2)


# In[20]:


sum_num = lambda a,b : a+b


# In[21]:


sum_num(1,2)


# ### Map -> Transform, 
# ### Reduce -> Aggregation, 
# ### Filter -> True, False

# In[33]:


list_1 = [1,2,3,4,5]


# In[34]:


plus_five = lambda x : x+5


# In[35]:


map(plus_five,list_1)


# In[36]:


res = map(plus_five,list_1)


# In[37]:


list(res)


# ### Filter

# In[39]:


def less_than_5(num):
    if num < 5:
        return True
    else:
        return False


# In[40]:


def less_than_5(num):
    return num < 5


# In[41]:


less_than_5 = lambda num: num<5


# In[45]:


filtered = filter(less_than_5, list_1)


# In[46]:


list(filtered)


# ### Reduce

# In[4]:


list_1 = [1,2,3,4,5]


# In[5]:


import functools


# In[6]:


sum_function = lambda x,y : x+y


# In[9]:


functools.reduce(sum_function,list_1)


# In[13]:


functools.reduce (lambda x,y: x*y,list_1)


# ### Decorator

# In[16]:


def call_func(function):
    print("In call_func")
    name = "john"
    function(name)


# In[17]:


def greet(name):
    print(f"Hello {name}")


# In[18]:


call_func(greet)


# #### Simple Decorator Syntax

# In[39]:


def call_twice(function):
    def wrapper(name):
        function(name)
        function(name)
    return wrapper


# #### Example

# In[40]:


@call_twice
def greet(name):
    print(f"Hello {name}")


# In[41]:


greet("John")


# In[ ]:




