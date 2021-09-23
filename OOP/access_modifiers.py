"""
A Class in Python has three types of access modifiers:

Public Access Modifier
Protected Access Modifier
Private Access Modifier
"""

"""
Public Access Modifier:
The members of a class that are declared public are easily accessible from any part of the program. 
All data members and member functions of a class are public by default. 

In the below example, name and age are public data members and display_age() method is a public member function of the class Test. 
These data members of the class Test can be accessed from anywhere in the program.
"""

class Test:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.name = name
        self.age = age

    # public member function     
    def display_age(self):
        # accessing public data member
        print("Age: ", self.age)
 
# creating object of the class
obj = Test("Vinay", 26)
 
# accessing public data member
print("Name: ", obj.name)
 
# calling public member function of the class
obj.display_age()
print('*****************************')


"""
Protected Access Modifier:
The members of a class that are declared protected are only accessible to a class derived from it and from the same class where they are defined. 
Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 

In the below example, _name and _branch are protected data members and _display_branch() method is a protected method of the super class Student. 
The display_details() method is a public member function of the class Test which is derived from the Student class, the display_details() method in Test class accesses the protected data members of the Student class. 
"""

# super class
class Student:
    
    # protected data members
    _name = None
    _branch = None

    # constructor
    def __init__(self, name, branch): 
        self._name = name
        self._branch = branch

    # protected member function  
    def _display_branch(self):
        # accessing protected data members
        print("Branch: ", self._branch)
 
student = Student('Vinay_doppleganger', 'Physics')
print(f'Calling Protected Data members from the Same class where they have defined:: \n {student.__dict__}')
print(f'Calling Protected member function from Same class::')
student._display_branch()
print()
 
# derived class
class ProtectedTest(Student):
    # constructor
    def __init__(self, name, branch):
        Student.__init__(self, name, branch)
        
    # public member function
    def display_details(self):       
        # accessing protected data members of super class
        print("Name: ", self._name)
            
        # accessing protected member functions of super class
        self._display_branch()

# creating objects of the derived class       
obj = ProtectedTest("Vinay", "ECE")
 
# calling public member functions of the class
obj.display_details()
print('*****************************')

"""
Private Access Modifier:
The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. 
Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 
"""

class PrivateTest:
    # private members
    __name = None
    __branch = None

    # constructor
    def __init__(self, name, branch): 
        self.__name = name
        self.__branch = branch

    # private member function 
    def __display_details(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Branch: ", self.__branch)

    # public member function
    def access_private_function(self):
        # accesing private member function
        self.__display_details() 
 
# creating object   
obj = PrivateTest("Vinay_from_multiverse", "HealthSciences")
 
# calling public member function of the class
obj.access_private_function()

# It will throw error stating class object has no attribute __display_details
# PrivateTest.__display_details()
# PrivateTest.__name
# PrivateTest.__branch

"""
But here is a hack to access the private data members from outside
"""

obj = PrivateTest('vinay', 'ECE')
# hack_1
obj.access_private_function() # able to access everything with help of public member function which can access private members

# hack_2
print(obj.__dict__) # it will show all data members irrespective of private access modifier ('__') applied
obj._PrivateTest__name = 'Kumar'
obj._PrivateTest__name = 'CSE'
print(obj.__dict__)
print('*********************************')

"""
Below is a program to illustrate the use of all the above three access modifiers (public, protected, and private) of a class in Python: 
"""

# super class
class SuperClass:
    # public data member
    var1 = None

    # protected data member
    _var2 = None
    
    # private data member
    __var3 = None
    
    # constructor
    def __init__(self, var1, var2, var3): 
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    # public member function  
    def display_public_members(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)
    
    # protected member function  
    def _display_protected_members(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)
    
    # private member function  
    def __display_private_members(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def access_private_members(self):
        # accessing private member function
        self.__display_private_members()
  

# derived class
class SubClass(SuperClass):
    # constructor
    def __init__(self, var1, var2, var3):
        SuperClass.__init__(self, var1, var2, var3)
        
    # public member function
    def access_protected_members(self):    
        # accessing protected member functions of super class
        self._display_protected_members()
  
# creating objects of the derived class    
obj = SubClass("Vinay", 4, "Tech")
 
# calling public member functions of the class
obj.display_public_members()
obj.access_protected_members()
obj.access_private_members()
 
# Object can access protected member
print("Object is accessing protected member:", obj._var2)
 
# object can not access private member, so it will generate Attribute error
#print(obj.__var3)
print(obj._SuperClass__var3) # but can access private data members/member functions like this