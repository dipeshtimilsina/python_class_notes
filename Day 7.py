#!/usr/bin/env python
# coding: utf-8

# ### Function Continued

# In[17]:


def call_twice(function):
    def wrapper(*args,**kwargs):
        function(*args,**kwargs)
        function(*args,**kwargs)
    return wrapper


# In[18]:


@call_twice
def sum_num(a,b):
    print (a+b)


# In[19]:


sum_num (3,4)


# ### Example of Decorator

# In[30]:


def pin_check(func):
    def wrapper(*args,**kwargs):
        if kwargs.get('pin') == 1234:
            return func(*args,**kwargs)
        else:
            print("Invalid Pin")
    return wrapper


# In[31]:


@pin_check
def withdraw(amt,pin):
    print(f"{amt} withdrawn")


# In[33]:


withdraw(12,pin=1234)


# In[38]:


def call_n_times(n=1):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range (n):
                function(*args,**kwargs)
        return wrapper
    return decorator


# In[41]:


@call_n_times()
def greet(name):
    print(f"Hello {name}")


# In[42]:


greet ('John')


# ### Recursive Function

# In[1]:


def recur():
    print("Function Called")
    recur()


# In[4]:


list_1 = [1,2,3,4,5,6,7]


# In[5]:


def sum_rec(list_1):
    if len(list_1)==1:
        return list_1[0]
    else:
        return list_1[0] + sum_rec(list_1[1:])


# In[7]:


sum_rec(list_1)


# ### Factorial

# In[8]:


def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)


# In[9]:


factorial(5)


# ### Fibonacci Series

# In[12]:


def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# In[13]:


fib(7)


# ### Nested List

# In[24]:


list_2=[1,2,[3,4],5]


# In[25]:


def rec_sum_list(list_2):
    sum_list=0
    for element in list_2:
        if type(element) == type([]):
            sum_list = sum_list + rec_sum_list(element)
        else:
            sum_list = sum_list + element
        return sum_list


# In[26]:


rec_sum_list(list_2)


# In[27]:


def gen_list(upto):
    for i in range(upto):
        yield i


# In[37]:


generated = gen_list(5)


# In[38]:


next(generated)


# In[39]:


for i in generated:
    print(i)


# In[ ]:




