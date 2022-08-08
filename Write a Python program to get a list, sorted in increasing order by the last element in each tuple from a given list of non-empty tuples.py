#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Write a Python program to get a list, sorted in increasing order by the 
# last element in each tuple from a given list of non-empty tuples



# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


my_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for  i in range(0,len(my_list)):
    for j in range(0,len(my_list)-i-1):
        if my_list[j][-1]>my_list[j+1][-1]:
                temp = my_list[j] 
                my_list[j]= my_list[j + 1] 
                my_list[j + 1]= temp 
print(my_list)


# In[ ]:





# In[ ]:





# In[ ]:




