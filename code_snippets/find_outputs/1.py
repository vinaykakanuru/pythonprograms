# (1)---------------------------------------------------------------------------
def m(val, list = []):
    list.append(val)
    return list
    
list1 = m(10)
list2 = m(123, [])
list3 = m("a")

print(f"list1: {list1}") # list1: [10, 'a']
print(f"list2: {list2}") # list2: [123]
print(f"list3: {list3}") # list3: [10, 'a']
# (1)---------------------------------------------------------------------------

# (2)---------------------------------------------------------------------------
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x) # 1,1,1
Child1.x = 2

print(Parent.x, Child1.x, Child2.x) # 1,2,1

Parent.x = 3
print(Parent.x, Child1.x, Child2.x) # 3,2,3
# (2)---------------------------------------------------------------------------

# (3)---------------------------------------------------------------------------
# (3)---------------------------------------------------------------------------

# (4)---------------------------------------------------------------------------
# (4)---------------------------------------------------------------------------




