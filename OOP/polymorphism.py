'''
What is Polymorphism: The word polymorphism means having many forms. 
In programming, polymorphism means the same function name (but different signatures) being used for different types.
'''

## Examples of user-defined polymorphic functions : 
def add(x, y, z = 0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))


'''
Polymorphism with class methods: 
The below code shows how Python can use two different class types, in the same way. 
We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is. 
We assume that these methods actually exist in each class. 
'''

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for idx, country in enumerate((obj_ind, obj_usa)):
    print(f'***** Iteration - {idx} for {country.__class__.__name__} *****')
    country.capital()
    country.language()
    country.type()
    

'''
Polymorphism with Inheritance: 
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. 
In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. 
In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding. 
'''

class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()


'''
Polymorphism with a Function and objects: 
It is also possible to create a function that can take any object, allowing for polymorphism. 
In this example, let’s create a function called “func()” which will take an object which we will name “obj”. 
Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. 
Next, let’s give the function something to do that uses the ‘obj’ object we passed to it. 
In this case, let’s call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. 
Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. 
With those, we can call their action using the same func() function: 
'''

def func(obj):
    obj.capital()
    obj.language()
    obj.type()
  
obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)


'''
Method Overloading: 
Method Overloading is an example of Compile time polymorphism. 
In this, more than one method of the same class shares the same method name having different signatures. 
Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.

Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method.
'''

class Test():
    def m1(self):
        print('First Method')
    
    def m1(self):
        print('Second Method')
    
    def m1(self, val):
        print(f'Third method with given {val}')

# the latest defined second method overloads the first method
overload_obj = Test()
overload_obj.m1(10)
# overload_obj.m1() # It will call the m1 with args but both m1() and m1(val) cannot be called at a time


'''
Method Overriding: 
Method overriding is an example of run time polymorphism. 
In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. 
It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. 
In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.
'''


class A:
    def fun1(self):
        print('feature_1 of class A')
         
    def fun2(self):
        print('feature_2 of class A')
     
 
class B(A):
    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')   
         
    def fun3(self):
        print('feature_3 of class B')
         
 
# Create instance
obj = B()
     
# Call the override function
obj.fun1()