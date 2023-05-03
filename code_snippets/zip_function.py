# You can find all built in functions in python using below method
# print(dir(__builtins__))

# Python docs link
# https://docs.python.org/3/library/functions.html#zip

# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.
# With a single iterable argument, it returns an iterator of 1-tuples.
# With no arguments, it returns an empty iterator. Equivalent to:


def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


a = zip([1, 2, 3, ], ('a', 'b', 'c'))
zipped_data = list(a)
print(zipped_data) # [(1, 'a'), (2, 'b'), (3, 'c')]

# in similar way we can un-pack the tuples using zip

a, b = zip(*zipped_data)  # returns tuples
print(a) # (1,2,3)
print(b) # ('a', 'b', 'c')

b = [1, 2, 3, 4]
print(list(zip(b)))  # it returns an iterator of 1-tuples [(1,), (2,), (3,), (4,)]
