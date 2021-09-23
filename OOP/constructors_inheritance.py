# defining class A
class A:
  def __init__(self, txt):
    print(txt, 'I am in A Class')
  
# B class inheriting A
class B(A):
  def __init__(self, txt):
    print(txt, 'I am in B class')
    super().__init__(txt)
      
# C class inheriting B
class C(B):
  def __init__(self, txt):
    print(txt, 'I am in C class')
    super().__init__(txt)
  
# D class inheriting B
class D(B):
  def __init__(self, txt):
    print(txt, 'I am in D class')
    super().__init__(txt)
  
# E class inheriting both D and C
class E(D, C):
  def __init__(self):
    print( 'I am in E class')
    super().__init__('hello ')
  
# driver code
d = E()
print('')
h = C('hi')
