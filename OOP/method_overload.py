'''
Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python. 

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 
'''
class Test:
    def product(a, b):
        p = a * b
        print(p)

    def product(a, b, c):
        p = a * b*c
        print(p)

# Test.product(4, 5) # it throws 1 pos arg is missing as python considers the latest product method
Test.product(4, 5, 5)
print('*************************************')


'''
Method 1 (Not The Most Efficient Method):
We can use the arguments to make the same function work differently i.e. as per the arguments.
The problem with below code is that makes code more complex with multiple if/else statement and is not the desired way to achieve the method overloading.
'''

def add(datatype, *args):
    # if datatype is int initialize answer as 0
    if datatype =='int':
        answer = 0
          
    # if datatype is str initialize answer as ''
    if datatype =='str':
        answer =''
  
    # Traverse through the arguments
    for x in args:
        # This will do addition if the arguments are int. 
        # Or concatenation if the arguments are str
        answer = answer + x
  
    print(answer)

# Integer
add('int', 5, 6)
  
# String
add('str', 'Hi ', 'Geeks')
print('*************************************')


'''
Method 2 (Efficient One):
By Using Multiple Dispatch Decorator 
Multiple Dispatch Decorator Can be installed by: 

$ pip3 install multipledispatch
'''
from multipledispatch import dispatch
  
# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)
  
# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)
  
# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)
  

# calling product method with 2 arguments
product(2, 3, 2) # this will give output of 12
product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997
print('*************************************')