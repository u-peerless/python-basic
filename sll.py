import inspect

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class sll:
    def __init__(self):
        self.start = None
        self.last = None
    def insert(self, x):
        new_node = node(x, None)
        if self.start == None:
            self.start = new_node
            self.last = new_node
            self.start.next = None
        elif self.start == self.last:
            self.start.next = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    def __str__(self):
        if self.start == None:
            return "Empty List"
        out = "Linked List: ["
        ct_node = self.start
        while ct_node != None:
            out += str(ct_node.value) + " "
            ct_node = ct_node.next
        out += "]"
        return out
    
    def clear(self):
        self.__init__()        

    def print_reverse(self):
        print inspect.currentframe().f_lineno

        a = self.start
        b = None
        c = None
        while (a != None):
#            print inspect.currentframe().f_lineno
            c = b
            b = a
            a = a.next
            b.next = c
        self.start = b
        print self
#        print "Hello"
        
def main():
    L1 = sll()
    L1.insert(2)
    L1.insert(3)
    L1.insert(7)
    L1.insert(0)
    print L1
    L1.print_reverse()
#    print L1
    L1.clear()
    print L1
        
if __name__ == '__main__':
    main()
    