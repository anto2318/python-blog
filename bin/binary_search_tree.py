class Tree:
    def __init__(self, data = None):
        self.d = data 
        self.l = None
        self.r = None

    def insert(self, data):
        if self.d:
            if data > self.d:
                if self.r:
                    self.r.insert(data)
                else:
                    self.r = Tree(data)
            else:
                if self.l:
                    self.l.insert(data)
                else:
                    self.l = Tree(data)
        else:
            self.d = data
    
    def pre(self):
        if self.d:
            print(self.d)
        if self.l:
            self.l.pre()
        if self.r:
            self.r.pre()

    def inorder(self):
        if self.l:
            self.l.inorder()
        if self.d:
            print(self.d)
        if self.r:
            self.r.inorder()
    
    def post(self):
        if self.l:
            self.l.post()
        if self.r:
            self.r.post()
        if self.d:
            print(self.d)
    
    def search(self, data):
        while self != None and self.d:
            if data < self.d:
                self = self.l
            elif data > self.d:
                self = self.r
            else:
                return print("Element found")
        else:
            print("Element Not found")

binary_tree = Tree()
binary_tree.search(5)
binary_tree.pre()
binary_tree.inorder()
binary_tree.post()

values = [50, 10, 90, 80, 20]
for i in values:
    binary_tree.insert(i)

print("Pre Order Transversal: ")
binary_tree.pre()

print("In Order Transversal: ")
binary_tree.inorder()

print("Post Order Transversal: ")
binary_tree.post()

binary_tree.search(20)
binary_tree.search(25)
