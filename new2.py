
# coding: utf-8

# In[10]:


def fractiontup(t1,t2):
    num = int(t1[0]*t2[1])+(t1[1]*t2[0])
    den = int(t1[1]*t2[1])
    
    return num,den

t1=(1,2)
t2=(4,2)

q=fractiontup(t1,t2)


# In[11]:


print (str(q[0])+"/"+str(q[1]))


# In[ ]:





# In[48]:


def frac(a,b,c,d):
    if b == d:
        e=a+c
        return e,d
    else:
        f = int ((a*d)+(b*c))
        g = int (d*b)
        return f,g
        

        


# In[50]:


q=frac(2,1,4,2)
 


# In[55]:


print ('{}/ {}'.format(q[0],q[1]))


# In[62]:


list1 = [1,1]
list2 = [4,2]
def frac():
    if list1[1:] == list2[1:]:
        a = int(list1[0]+list2[0])
        
        return a,list2[1]
    else:
        b = int(list1[0]*list2[1])+(list1[1]*list2[0])
        c = int(list1[1]*list2[1])
        
        return b,c
    


# In[64]:


f=frac()


# In[65]:


print ('{}/ {}'.format(f[0],f[1]))


# In[ ]:





# In[74]:


class fractionclass:
    def __init__(self,a,b):
        self.numerator=a
        self.denomenator=b
    def add(f1,f2):
        num=(f1.numerator*f2.denomenator)+(f1.denomenator*f2.numerator)
        den=(f1.denomenator*f2.denomenator)
        return num,den
f1 = fractionclass(1,1)
f2 = fractionclass(4,1)
t = fractionclass.add(f1,f2)
#print('{} / {}'.format(t[0],t[1]))

print (str(t[0])+"/"+str(t[1]))


# In[75]:


type(t)


# In[76]:


print('{} / {}'.format(t[0],t[1]))

