""" You can't use Lambdas only with If statements and without else statement. """
print(list(map(lambda x:x**2 if x%2==1 else None, list(range(1, 11)))))
print(list(map(lambda x: x**2, list(filter(lambda x:x%2==1, list(range(1, 11)))))))

""" You can easily perform intersection without using set operator """
a, b = [2,3,6,7,8,4], [1,2,3,4,5]
print(set.intersection(set(a), set(b)))
print(set.union(set(a), set(b)))
print(list(filter(lambda x: x in a, b)))