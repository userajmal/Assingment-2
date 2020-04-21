#!/usr/bin/env python
# coding: utf-8
# Task 1: 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
# In[27]:


a=[10,20,30,40]
x , x1 = (a[0]+a[1]) , (x+a[2])
Final_Value = x1+a[3]
print(Final_Value)


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[97]:


ages = [1,2,3,6,677,8,3,33,44,2,290,11,34,23,26,11]
def myFunc(ages):
    if ages < 19 :
        return False
    else:
        return True
for i in ages:
    if i < 19 :
        print(i)


# 2. Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 3. Implement a function longestWord() that takes a list of words and returns the longest one.

# In[17]:


a="ACADGILD"
finalresult = [b for b in a]
print(finalresult)


# In[22]:


a=["x","y","z"]
finalresult=[b*num for b in a for num in range(1,5)  ]
print(finalresult)


# In[30]:


a=["x","y","z"]
finalresult=[b*num for num in range(1,5)for b in a  ]
print(finalresult)


# In[28]:


a=[2,3,4]
finalresult=[[b+num] for b in a for num in range(0,3)  ]
print(finalresult)


# In[36]:


a=[2,3,4,5]
finalresult=[[b+num for b in a] for num in range(0,4)  ]
print(finalresult)


# In[34]:


c=[1,2,3]
finalresult=[(a,b) for b in a for a in c  ]
print(finalresult)

Implement a function longestWord() that takes a list of words and returns the longest one.
# In[62]:


def longestWord(words):
    word_len = []
    for n in words:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(longestWord(["ajmal", "is" ,"a", "good boy","and", "smartboy"]))


# In[59]:


def longestWord(words):
   words=["ajmal", "is" ,"a", "good boy","and", "smartboy"]
   max1 = ''
   for x in range (0, len(words)):
         if (len(max1) < len(words[x]) ):
             max1 = words[x]
   return max1
print(longestWord(words))
def main():
   m =longestword()
   print(len(m))

Task 2: 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula. area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.
# In[86]:


import sys
import math

a = int(input())
b = int(input())
c = int(input())
class triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s=(a + b + c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
t=triangle(a,b,c)
print(t.area())

Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
# In[121]:


def filter_long_words(words):
    word_len = []
    a=4
    for n in words:
        word_len.append((len(n), n))
    for i in range(len(n)):
        listwords = []
        if len(n[i]) > a:
            listwords.append(n[i])
        return listwords 
print(filter_long_words(["ajmal", "is" ,"a", "good boy","and", "smartboy"]))

Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# In[120]:


def map_to_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
def map_to_lengths_map(words):
    return map(len, words)
def map_to_lengths_lists(words):
    return [len(word) for word in words]
if __name__ == "__main__":
    words = ['ajmal', 'is', 'goodboy']
    print (map_to_lengths(words))
    print (map_to_lengths_map(words))
    print (map_to_lengths_lists(words))

Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
# In[119]:


def vowel(charc): 
    if (Charc == "a" or inputChar == "A" or inputChar == "e" or inputChar == "E" or inputChar == "i" or inputChar == "I" or inputChar == "o" or inputChar == "O" or inputChar == "u" or inputChar == "U"):
        return "True"
    else:
        return "False"

Charc = input()
if vowel(Charc) == "True":
 print("character is Vowel")
else:
 print("character is not Vowel")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




