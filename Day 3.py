#!/usr/bin/env python
# coding: utf-8

# ### Boolean

# In[1]:


boolean = True


# In[2]:


type(boolean)


# ### is and in used in a list

# In[3]:


list_1 = [1,2,3,4,5]


# In[4]:


5 in list_1


# In[5]:


5 is '5'


# In[6]:


5 is int


# In[7]:


5 is 5


# ### Operators

# In[8]:


5==5


# In[9]:


6>=6


# In[10]:


7!=7.1


# ### 3 operation on boolean (and, or and not)

# In[12]:


a=True
b=False


# In[13]:


a and b


# In[14]:


not a 


# ### if, elseif, else, break, continue

# In[17]:


if 5<3:
    print('5 is less than 3')
else:
    print('5 is greater')


# In[43]:


try:
    ans = input("Enter your percentage: ")
    ans = float(ans)
    assert ans<=100 and ans>= 0
    if ans >= 80:
        print ("Grade A")
    elif ans >= 70:
        print ("Grade B")
    elif ans >= 60:
        print ("Grade C")
    elif ans >= 50:
        print ("Grade D")
    elif ans >= 35:
        print ("Grade P")
    else:
        print ("Grade F")
except AssertionError:
    print ("Invalid Percentage")
except Exception as e:
    print (e)


# ### Input from user

# In[19]:


ans = input("Enter a number ")


# In[20]:


type(ans)


# In[21]:


ans = int(ans)


# In[22]:


ans + 5


# ### Exception and error handling

# In[32]:


ans = input("Enter a number :")
try:
    print("Inside try block")
    ans = int(ans)
    ans + 5
except Exception as e:
    print("Invalid Integer")
    print(e)


# ### Using if else for error handling

# In[27]:


ans = input("Enter a number:")
if ans.isnumeric():
    ans = int(ans)
    print(ans + 5)
else:
    print('Invalid Integer')


# In[63]:


try:
    ans = input('Enter a number:')
    ans = int(ans)
    if ans%2 != 0:
        print(f'{ans} is odd')
    else:
        print (f'{ans} is even')
except:
    print("invalid Number")

