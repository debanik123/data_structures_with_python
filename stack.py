#!/usr/bin/env python
# coding: utf-8

# In[20]:


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
    
c = stack()
c.push("a")
c.push("b")
#c.push("c")
#c.push("d")
print(c.display())
print(c.peek())
print(c.is_empty())
print(c.display())

c.pop()
print(c.display())
print(c.is_empty())

c.pop()

print(c.display())
print(c.is_empty()) 


# In[ ]:




