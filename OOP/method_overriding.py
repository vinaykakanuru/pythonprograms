'''
Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. 
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

The version of a method that is executed will be determined by the object that is used to invoke it. 
If an object of a parent class is used to invoke the method, then the version in the parent class will be executed, but if an object of the subclass is used to invoke the method, then the version in the child class will be executed. 
In other words, it is the type of the object being referred to (not the type of the reference variable) that determines which version of an overridden method will be executed.
'''

# Defining parent class
class Parent():
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
          
    # Parent's show method
    def show(self):
        print(self.value)
          

# Defining child class
class Child(Parent):
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
# Driver's code
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()
print('*****************************')


'''
Method overriding with multiple and multilevel inheritance
Multiple Inheritance: When a class is derived from more than one base class it is called multiple Inheritance.
Example: Let’s consider an example where we want to override a method of one parent class only.
'''
# Defining parent class 1
class Parent1(): 
    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2():   
    # Parent's show method
    def display(self):
        print("Inside Parent2")
          
          
# Defining child class
class Child(Parent1, Parent2): 
    # Child's show method
    def show(self):
        print("Inside Child")
     
        
# Driver's code
obj = Child()
  
obj.show()
obj.display()
print('*****************************')


'''
Multilevel Inheritance: When we have a child and grandchild relationship.
Example: Let’s consider an example where we want to override only one method of one of its parent classes.
'''
# Python program to demonstrate overriding in multilevel inheritance 
class Parent(): 
    # Parent's show method
    def display(self):
        print("Inside Parent")
    
    
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
    # Child's show method
    def show(self):
        print("Inside Child")
    

# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
    # Child's show method
    def show(self):
        print("Inside GrandChild")         
    

# Driver code 
g = GrandChild()   
g.show()
g.display()
print('*****************************')


'''
Calling the Parent’s method within the overridden method
Parent class methods can also be called within the overridden methods. 
This can generally be achieved by two ways.

Using Classname: Parent’s class methods can be called by using the Parent "classname.method" inside the overridden method.
'''
class Parent():
    def show(self):
        print("Inside Parent")
          

class Child(Parent):
    def show(self):
        # Calling the parent's class
        # method
        Parent.show(self)
        print("Inside Child")
          

# Driver's code
obj = Child()
obj.show()
print('*****************************')


'''
Using Super(): Python super() function provides us the facility to refer to the parent class explicitly. It is basically useful where we have to call superclass functions. 
It returns the proxy object that allows us to refer parent class by ‘super’.
'''
## Example 1 with super()
class Parent():
    def show(self):
        print("Inside Parent")
          

class Child(Parent):
    def show(self):
        # Calling the parent's class
        # method
        super().show()
        print("Inside Child")
          

# Driver's code
obj = Child()
obj.show()
print('*****************************')


## Example 2 with super()
class A: 
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class A)') 
    
    def sub(self, b): 
        print('Printing from class A:', b) 
    

# class B inherits the A 
class B(A): 
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class B)') 
        super().__init__() 
    
    def sub(self, b): 
        print('Printing from class B:', b) 
        super().sub(b + 1) 
    

# class GFG3 inherits the GFG1 ang GFG2 both 
class C(B): 
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class C)') 
        super().__init__() 
    
    def sub(self, b): 
        print('Printing from class C:', b) 
        super().sub(b + 1) 
    

# driver code
c = C()
# calling the function sub() from class C which inherits both A and B classes 
c.sub(10)
print('*****************************')