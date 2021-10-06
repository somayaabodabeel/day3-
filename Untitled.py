#!/usr/bin/env python
# coding: utf-8

# In[1]:


for a in range(151):
    print(a)


# In[2]:


for b in range(5, 1001, 5):
    print(b)


# In[3]:


for c in range(1, 101):
    if c % 10 == 0:
        print("Divisible by 10")
    elif c % 5 == 0:
        print("Divisible by 5")
    else:
        print(c)


# In[7]:


sum = 0
for d in range(500001):
 if d % 2 != 0:
    sum += d
 print(sum)


# In[9]:


for x in range(2018, 0, -4):
 if x > 0:
  print(x)


# In[10]:


lowNum = 2
highNum = 9
mult = 3
for f in range(lowNum, highNum + 1):
 if f % mult == 0:
  print(f)


# In[ ]:




