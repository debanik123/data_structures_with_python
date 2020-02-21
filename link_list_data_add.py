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
l.head = S_Node(12)
l.head.link = S_Node(121)
l.head.link.link = S_Node(112)
l.head.link.link.link = S_Node(111)
l.head.link.link.link.link = S_Node(222)


l.print_list()           
def add_l(head):
    t = head 
    if head == None:
        return 
    else:
        while t.link != None:
            t.data = t.data + t.link.data
            t = t.link
add_l(l.head)
l.print_list()
