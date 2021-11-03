class Iterator:
    def __init__(self, l):
        self._l = l
    
    def next(self):
        try:
            return self._l.pop(0)
        except:
            return None

    def has_next(self):
        return bool(len(self._l))


class FlattenIterator(Iterator):
    def __init__(self, l):
        self.input_list = l
        self.index = 0 
        self.list_len = len(self.input_list)

    def next(self):
        if self.index > self.list_len - 1:
            return "List already Parsed"

        obj = self.input_list[self.index]
        val = obj.next()

        if obj.has_next() is False:
            self.index += 1

        if val is None:
            self.index += 1
            if self.index > self.list_len - 1:
                return "List already Parsed"
            obj = self.input_list[self.index]
            return obj.next()
        else:
            return val


    def has_next(self):
        if self.index < self.list_len:
            obj = self.input_list[self.index]
            return True if obj.has_next() else False
        elif self.index == self.list_len:
            return False


flatten = FlattenIterator([Iterator([1]), Iterator([2,3,4]), Iterator([5,6])])
print(flatten.next())
print(flatten.next())
print(flatten.next())
print(flatten.next())
print(flatten.has_next())
print(flatten.next())
print(flatten.next())
print(flatten.has_next())
print(flatten.next())