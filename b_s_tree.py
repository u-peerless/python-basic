class node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)

class b_s_tree:
    c = node()
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.c.value)
        
    def insert_node(self, value):
        b = node(value)
        if self.root == None:
            self.root = b
            return b
        current = self.root
        while 1:
            if value < current.value:
                if current.left != None:
                    current = current.left
                else:
                    current.left = b
                    break
            elif value > current.value:
                if current.right != None:
                    current = current.right
                else:
                    current.right = b
                    break
            else:
                break
                
    def display(self, root):
        if root == None:            
            return
        print root.value
        self.display(root.left)
        self.display(root.right)
        
b = b_s_tree()
print b
b.insert_node(10)
b.insert_node(6)
b.insert_node(15)
b.insert_node(3)
b.insert_node(8)
b.insert_node(13)
b.insert_node(20)
b.insert_node(7)
b.insert_node(9)
b.insert_node(14)

b.display(b.root)    