#!/usr/bin/env python
# coding: utf-8

# # 11_02 Get and Set methods in encapsulation

# In[1]:


class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        
    #methods
    
# person01 = Person("John", "Wrights", 34)
# print(f"Name: {person01._name} {person01._surname}\nAge: {person01._age}") #We shouldn't access encasulation from outside the class


# In[4]:


#Get and set

class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        
    #methods
    #get
    #add a decorator so we don't directly access the encapsulated attributes _attribute in __init__
    @property #this is a decorator that makes imposible to access the _attribute directly from outside the class
    def name(self):
        print("Calling Get method")
        return self._name
    
    #set method
    #only to modify the value of the attribute
    #can be deleted if you don't want to modify the attribute value from outside the class
    #without this, it is known as only-read code
    @name.setter
    def name(self, name):
        print("Calling Set method")
        self._name = name
    
# person01 = Person("John", "Wrights", 34)
# person01.name = "Mathew"
# print(f"Name: {person01.name} {person01._surname} - Age: {person01._age}") #We shouldn't access encasulation from outside the class


# In[5]:


#Get and set for the rest of the attributes

class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        
    #methods
    
    #get method for name
    @property
    def name(self):
        print("Calling Get method for name")
        return self._name
    
    #set method for name
    @name.setter
    def name(self, name):
        print("Calling Set method for name")
        self._name = name
        
    #get method for surname
    @property
    def surname(self):
        print("Calling Get method for surname")
        return self._surname
    
    #set method for surname
    @surname.setter
    def surname(self, surname):
        print("Calling Set method for surname")
        self._surname = surname
        
    #get method for age
    @property
    def age(self):
        print("Calling Get method for age")
        return self._age
    
    #set method for age
    @age.setter
    def age(self, age):
        print("Calling Set method for age")
        self._age = age
        
    #printing method
    def printing(self):
        print(f"Name: {self._name} {self._surname} - Age: {self._age}\n") #We shouldn't access encasulation from outside the class

    def __del__(self):
        print(f"You have deleted object {self._name}")


# In[6]:


# person02 = Person("Mary", "Shelly", 34)

# person02.printing()
# person02.name = "Kathy"
# person02.printing()
# person02.age = 29
# person02.printing()


# **Note:** run ``jupyter nbconvert --to script ./get_set.ipynb`` in the terminal (same directory) to transform this file into a ``.py`` file so it can be imported as a module in other Notebooks. ``%run get_set.ipynb`` might also work if added at the top of the other Notebook, but not recommended

# In[ ]:




