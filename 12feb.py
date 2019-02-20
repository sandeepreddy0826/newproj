
# coding: utf-8

# In[ ]:


problem 1:
    "a=b","hello=world","d=e"
    [("a","b"),("hello","world"),("d,e")]


# In[111]:


c = "a=b,hello=world,d=e"
def prb1():
    r=(c.replace("=",","))
    k = r.split(",")
    
    return k


# In[112]:


j = prb1()


# In[113]:


print('[("{}","{}"),("{}","{}"),("{}","{}")]'.format(j[0],j[1],j[2],j[3],j[4],j[5]))

