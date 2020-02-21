class S_Node:
    def __init__(self,data):
        self.data = data
        self.link = None 
        
class Link_list:
    def __init__(self):
        self.head = None 
    def print_list(self):
        t = self.head 
        while t:
            print(t.data)
            t = t.link
l = Link_list()
l.head = S_Node(10)
l_2 = S_Node(20)
l_3 = S_Node(30)
l_4 = S_Node(40)
l_5 = S_Node(50)

l.head.link = l_2
l_2.link = l_3
l_3.link = l_4
l_4.link = l_5

l.print_list()           

print("__________________________________________")
def fun(head, n):
    t = head
    if (head == None):
        return
    else:
        i = 1
        while(i != n):
            t = t.link
            i += 1
        t1 = head.data
        head.data = t.data
        t.data = t1
fun(l.head,3)
l.print_list()
