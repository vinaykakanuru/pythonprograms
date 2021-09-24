""" Sort the given list of dictionaries """

from operator import itemgetter

test = [{'name': 'vinay', 'profession': 'IT', 'date': '2021-01-01', 'age': 25},
        {'name': 'sreekar', 'profession': 'Business',
            'date': '2019-01-01', 'age': 24},
        {'name': 'sasi', 'profession': 'Student', 'date': '2020-09-01', 'age': 27},
        {'name': 'nissar', 'profession': 'Consultant',
            'date': '2020-04-01', 'age': 29},
        {'name': 'Ajay', 'profession': 'Public sector', 'date': '2020-11-05', 'age': 23}, ]

# sort the given list based on keys in the dictionary objects
test.sort(key=itemgetter('name'))
# sort the given list in reverse order based on keys in the dictionary objects
test.sort(key=itemgetter('name'), reverse=True)

# store the sorted list into new variable
new_test = sorted(test, key=itemgetter('date'))
print(new_test)


# Without using in-built functions
def sort_list_of_dicts(test_list, key):
    a = [(i, j[key]) for i, j in enumerate(test_list)]
    b = sorted([i[1] for i in a])
    sorted_index = [j[0] for i in b for j in a if i == j[1]]
    return [test_list[i] for i in sorted_index]


print(sort_list_of_dicts(test, 'date'))
