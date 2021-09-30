"""
An abstract class can be considered as a blueprint for other classes. 
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
A class which contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation. 
While we are designing large functional units we use an abstract class. 
When we want to provide a common interface for different implementations of a component, we use an abstract class. 
"""

"""
Why use Abstract Base Classes : 
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 
This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes in your mind is difficult or not possible. 
"""

"""
How Abstract Base classes work : 
By default, Python does not provide abstract classes. 
Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. 
ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. 
A method becomes abstract when decorated with the keyword @abstractmethod.
"""
import abc
from abc import ABC, abstractmethod
 
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
 
# Driver code
R = Triangle()
R.noofsides()
 
R = Pentagon()
R.noofsides()
print('*********************************************')



class Animal(ABC):
    # unimplemented normal function
    def move(self):
        pass
 
class Human(Animal):
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
    def move(self):
        print("I can crawl")

# Driver code
R = Human()
R.move()
 
K = Snake()
K.move()
print('*********************************************')


"""
Implementation Through Subclassing : 
By subclassing directly from the base, we can avoid the need to register the class explicitly. 
In this case, the Python class management is used to recognize PluginImplementation as implementing the abstract PluginBase. 
A side-effect of using direct subclassing is, it is possible to find all the implementations of your plugin by asking the base class for the list of known classes derived from it. 
"""
 
class parent:  
    # unimplemented normal function     
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        print("child class")
 
# Driver code
print(issubclass(child, parent))
print(isinstance(child(), parent))
print('*********************************************')


"""
Concrete Methods in Abstract Base Classes : 
Concrete classes contain only concrete(normal) methods whereas abstract classes may contain both concrete methods and abstract methods. 
The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super(). 
In the below program, we can invoke the methods in abstract classes by using super(). 
"""

class R(ABC):
    @abstractmethod
    def ab_method(self):
        print("Abstract Method from Abstract Base Class")

    # normal function
    def rk(self):
        print("Normal function/method From Abstract Base Class")
 
class K(R):
    def ab_method(self):
        print("Implemented abstract method from Sub Class")

    def rk(self):
        super().rk() # calling normal method of Abstract class
        super().ab_method() # calling abstract method of Abstract class
        print("from subclass")
 
# Driver code
try:
    r = K()
    r.rk() # calling normal function from sub class
    r.ab_method() # calling implemented abstract method from sub class
except Exception as e:
    print(e)

print('*********************************************')


"""
Abstract Properties : 
Abstract classes include attributes in addition to methods, you can require the attributes in concrete classes by defining them with @abstractproperty. 
The Base class cannot be instantiated because it has only an abstract version of the property getter method
"""
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"

class child(parent):
    @property
    def geeks(self):
        return "child class"
  
  
try:
    r = parent() # Can't instantiate abstract class parent with abstract methods geeks
except Exception as e:
    print(e)
  
r = child()
print(r.geeks)
print('*********************************************')


"""
Abstract Class Instantiation : 
Abstract classes are incomplete because they have methods that have nobody. 
If python allows creating an object for abstract classes then using that object if anyone calls the abstract method, but there is no actual implementation to invoke. 
So we use an abstract class as a template and according to the need, we extend it and build on it before we can use it. 
Due to the fact, an abstract class is not a concrete class, it cannot be instantiated. 
When we create an object for the abstract class it raises an error. 
"""
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

try:
    c = Animal() # Cannot Instantiate the Abstract class
except Exception as e:
    print(e)