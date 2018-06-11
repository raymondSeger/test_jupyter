
# coding: utf-8

# In[3]:


1+1


# In[4]:


a = 10


# In[5]:


a+1


# In[7]:


"This is a regular Text"


# # The largest heading
# ## The second largest heading
# ###### The smallest heading
# 
# In the words of Abraham Lincoln:
# 
# > Pardon my French

# In[9]:


for i in range(10):
    print(i)


# In[10]:


import numpy


# In[12]:


distances = [10, 15, 17]
times = [0.3, 0.47, 0.55]
distances = numpy.array(distances)
times = numpy.array(times)


# In[13]:


speeds = distances / times


# In[14]:


speeds


# In[15]:


speeds.sum()


# In[16]:


x = numpy.arange(start=0, stop=20, step=2)
x


# In[17]:


x + 1


# In[18]:


numpy.sin(x)


# In[19]:


numpy.sqrt(x)


# # Indexing

# In[21]:


one_dim = numpy.linspace(-0.5, 0.6, 12)
one_dim


# In[22]:


one_dim[0]


# In[23]:


two_dim = numpy.array([[3,5,2,4], [7,6,5,5], [1,6,-1,-1]])
two_dim


# In[24]:


two_dim[0,3]


# # Slicing

# In[26]:


one_dim[2:5]


# In[27]:


two_dim[:2,:2]


# In[30]:


two_dim[:,:2]


# # Reshape

# In[33]:


one_dim


# In[34]:


one_dim.reshape(4,3)


# In[35]:


two_dim


# In[36]:


two_dim.flatten()


# # Coin Flips

# In[45]:


numpy.random.randint(low=0, high=2, size=1)


# In[49]:


experiment = numpy.random.randint(low=0, high=2, size=10)
print(experiment)
print(experiment.sum())

