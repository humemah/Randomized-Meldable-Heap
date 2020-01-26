#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------"RANDOMIZEd MELDABLE PRIORITY QUEUE"--------------------------------------------------#

class Node:
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
class Priority_queue:
    def __init__(self):
        self.root=None
        self.size=0
        
    def Make_queue(self):
        if self.root==None:
            print("THE QUEUE IS EMPTY")
        else:
            print("THE QUEUE IS NON-EMPTY")
        
        
    def Insert(self,value):
        if self.root == None:
            u = Node(value)
            self.root = u
        else:
            u=Node(value)
            self.root=self.meld(u,self.root)
            self.root.parent=None
        self.size+=1
        return True
    
    def random(self,y):
        import random
       
    def meld(self,h1,h2):
        if h1==None:
            return h2
        if h2==None:
            return h1
        if h2.value<h1.value:
            (h1,h2)=(h2,h1)
        if self.random==0:
            h1.left=self.meld(h1.left,h2)
    
        else:
            h1.right=self.meld(h1.right,h2)
        return h1

    def Printt(self):
        return self.Inorder(self.root)
   
    def Inorder(self,x):
        if x:
            self.Inorder(x.left)
            print(x.value)
            self.Inorder(x.right)
            
    def Find_min(self):
        if self.size == 0:  
            print("empty queue")
        else:
            return self.root.value
    
   
    def Delete_min(self):
        if self.root== None: 
            print("empty queue")
        else:    
            value= self.root.value
            self.root=self.meld(self.root.left,self.root.right)
            if self.root is not None:
                self.root.parent=None
                self.size-=1
            return value
#------------------------------------------DRIVER CODE-------------------------------------------------------------------#
        
a=Priority_queue()
num=int(input(" Enter the range "))
for i in range (num):
    n=int(input("ENTER THE NUMBERS : "))
    a.Insert(n)
y=(1,0)
a.random(y)
a.Printt() 
print("The minimum node is : ",a.Find_min())
print("remove the min value in tree :",a.Delete_min())
a.Printt()


# In[ ]:




