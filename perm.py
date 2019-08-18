
# coding: utf-8

# In[80]:


import sys
data1 = [['a', 'k'], 'q', ['t', 'r', 'o'], ['p', 'e']] 

#check if there is any list
def is_list(data):
    for item in data:
        if isinstance(item, list):
            break
    return True
        
def count_lists(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += 1
    return count
            
def get_all_lists(data):
    for item in data:
        if isinstance(item, list):
            yield({i : data.index(item) for i in item})

lists = get_all_lists(data1)

def fartaqa(data):
    if not is_list(data) and len(data) == 1:
        return "//".join(data[0])
    if is_list(data) and len(data) == 1:
        return "".join(data[0])
#     if count_lists > 1:
        


# In[81]:


print(fartaqa(data1))
print(is_list(data1))
print(count_lists(data1))
print(lists)


# In[82]:


next(lists)


# In[83]:


# try:
#     next(lists)
# #     next(lists)
# #     next(lists)
# except StopIteration:
# #     raise StopIteration.with_traceback
#     print("$$$$$$$$444")
next(lists)


# In[84]:


next(lists)

