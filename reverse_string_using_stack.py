#!/usr/bin/env python
# coding: utf-8

# In[27]:


class stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def display(self):
        return self.items


# In[28]:


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        print(input_str[i])
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str
stack = stack()
ip = "DEBANIK"
r = reverse_string(stack,ip)
print(r)


# In[ ]:




