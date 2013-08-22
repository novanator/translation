"""
Author: Novanator 2012
Program: Translation2
"""

class TN:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None

class BinTree(object):
    def __init__(self):
        self.root=None
        
    def exists(self,data):
        return self.__exist(data, self.root)
                 
    def insert(self,d):
        if root==None:
            root=TN(d)
            return
        put(d,root)

    def put(self,d,n):
        if n.data==d:
            print("Double: " , n.data) 
            return
        if n.data  >d and n.left==None:
            n.left=TN(d)
            return
        elif n.data <d and n.right==None:
            n.right=TN(d)
            return
        elif n.data>d:
            put(d, n.left)
        else:
            put(d, n.right)


    def __exist(self, data, r):
        while r!=None :
            if data < r.data:
                r = r.left
            elif data > r.data:
                r = r.right
            else:
                return True
        return False

    def write2(self):
        self.__write(self.root)
        
    def __write(self, r):
        if r == None:
            return
        self.__write(r.left)
        print(r.data)
        self.__write(r.right)

    def nElements(self):
        return self.__numberElements(self.root)

    def __numberElements(self,p):
        if p == None:
            return 0;
        return 1+self.__numberElements(p.left)+self.__numberElements(p.right);


tree=BinTree()
print("Insert words, finish by hitting return/enter")
while True:
    word=input()
    if word=="": break
    tree.put(word)
print("The whole tree:")
tree.write()
print ("Search for a word, finish by hitting return/enter")
while True:
    word=input()
    if word=="": break
    if tree.exists(word):
        print ( word,"exists")
        
        
        
