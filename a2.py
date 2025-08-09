# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict1 = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict2 = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'Jack', 'age': 26,'hobby':"reading"}

# access a particular element
print("Name :", my_dict.get('name'))
print("Name :", my_dict['name'])

# update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove particular element
my_dict.pop('age')
print(my_dict)
print(my_dict.popitem())

# remove all the elements
my_dict.clear()
print(my_dict)
