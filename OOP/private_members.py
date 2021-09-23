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
    
    def details(self):
        self.__display_details()

