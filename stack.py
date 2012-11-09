class stack:
    def __init__(self):
        self.items = []
        
    def push(self, value = None):
        self.items.append(value)
                
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

def main():
    p = stack()
    p.push(10)
    p.push(23)
    p.push(12)
    while p.items != []:
        print p.pop()
    

if __name__ == '__main__':
    main()

    