
# coding: utf-8

# 1. Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print "division by zero!"
except Exception, err:
    print 'Caught an exception'
finally:
    print 'In finally block for cleanup'


# 2. Implement a python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in["Play", "watch"] and the object is in ["Baseball", "Cricket"].

# In[2]:


subject=["Americans", "Indians"]
verb=["Play","Watch"]
obj=["baseball","Cricket"]
sentence_list=[(sub+" "+vb+" "+ob)for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print(sentence)


# 3. Write a function so that the coloumn of the output matrix are powers of the input vector.
# The order of the power is determined by the incresing boolean orgument. Specfically, when increasing is false, the i-th output coloumn is the input vextor raised element-wise to the power of N-i-1.

# In[3]:


import numpy as np
x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)   
np.column_stack([x**(N-1-i) for i in range(N)])
x = np.array([1, 2, 3, 5])
np.vander(x)
np.vander(x, increasing=True)

