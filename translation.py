"""
Author: Novanator 2012
Program: Translation
"""


class Queue(object):

    class __Node(object):
        def __init__(self,value):
            self.value = value
            self.next=None

    
    def  __init__(self):
            self.__first=None
            self.__last=None
            
    def put(self, x):
        p = Queue.__Node(x)
        if self.__first==None:
            self.__first = p
            self.__last = p
        else:
            tmp = self.__last   
            tmp.next = p        
            self.__last = p     
                
    def get(self):
        if self.__first!=None:
            x = self.__first.value
            self.__first = self.__first.next
            return x
        return None

    def isempty(self):
        if self.__first==None:
            return True
        else:
            return False

    def show(self):
        p=self.__first
        while p != None:
            print(p.value,end=" ")
            p = p.next

class Translate:
    def __init__(self,swe,swa):
        self.swe=swe
        self.swa=swa

f=open("swabadoo.txt","r")
if f!="":
    print("Wordlist read!")
q=Queue()
list=[]
word=f.readline()
while word!="":
    word=word.strip()
    list.append(word)
    word=f.readline()

for i in range(0,14,2):
    g=Translate(list[i],list[i+1])
    q.put(g)

while not q.isempty():
    glossary=q.get()
    print("Translate to Swabadoo:",glossary.swe)
    answer=input("")
    if answer != glossary.swa:
        print("No, the right answer is: ",glossary.swa)
        q.put(glossary) 
    else:
        print("Correct!")
        

        
        
            
            
    








    
