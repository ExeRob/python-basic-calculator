#------------------------------add()------------------------------

#Add a number to an empty set
numbers = set()
numbers.add(5)

print(numbers)

#Add multiple items (one by one)
fruit = {"apple", "banana"}
fruit.add("pear")
fruit.add("orange")

print(fruit)

#Try adding a duplicate
names = {"Ana", "Luis"}
names.add("Ana")

print(names)

#Add elements within a loop
values = set()

for i in range(1, 6):
    values.add(i)

print(values)

#Add elements received from a simulated input
colors = set()

tickets = ["red", "green", "blue", "red"]

for c in tickets:
    colors.add(c)

print(colors)

#Add tuples (immutable structures)
points = set()
points.add((1, 2))
points.add((3, 4))

print(points)

#Add items to remove duplicates in a list
li_st = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = set()

for n in li_st:
    no_duplicates.add(n)

print(no_duplicates)

#Create a set with unique values ​​from a text
text = "banana"
unique_letters = set()

for letter in text:
    unique_letters.add(letter)

print(unique_letters)

#Add values ​​conditionally
numbers = set()
values = [10, -3, 5, -1, 8]

for v in values:
    if v > 0:
        numbers.add(v)

print(numbers)

#------------------------------union()------------------------------

#Join two simple sets
a = {1, 2, 3}
b = {3, 4, 5}

resultado = a.union(b)
print(resultado)

#Join three sets
a = {1}
b = {2}
c = {3, 4}

result = a.union(b, c)
print(result)

#Union where there are duplicate elements
fruit1 = {"apple", "banana"}
fruit2 = {"banana", "pear"}

result = fruit1.union(fruit2)
print(result)

#Union of sets created from lists
li_st1 = [1, 2, 3, 3]
li_st2 = [3, 4, 5]

result = set(li_st1).union(set(li_st2))
print(result)

#Join generated sets in a loop
even_numbers = {2, 4, 6}
odd_numbers = {1, 3, 5}

result = even_numbers.union(odd_numbers)
print(result)

#Join sets to remove duplicates from multiple lists
li_st1 = ["Ana", "Luis", "Ana"]
li_st2 = ["Luis", "Pedro"]

unique = set(li_st1).union(li_st2)

print(unique)

#Join a set with an empty set
a = {10, 20, 30}
b = set()

result = a.union(b)
print(result)

#Join sets to combine categories within a system
base_categories = {"admin", "user"}
extra_categories = {"editor", "guest"}

all = base_categories.union(extra_categories)

print(all)

#Join sets within a list of sets
groups = [
    {"Ana", "Luis"},
    {"Luis", "Pedro"},
    {"Maria", "Ana"}
]

result = set().union(*groups)

print(result)

#Join sets generated from text
text1 = "hello"
text2 = "world"

result = set(text1).union(text2)

print(result)

#------------------------------intersection()------------------------------

#Basic intersection between two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)
print(result)

#Intersection with no common elements
a = {1, 2, 3}
b = {4, 5, 6}

result = a.intersection(b)
print(result)

#Intersection between three sets
a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

result = a.intersection(b, c)
print(result)

#Intersection between sets created from lists
li_st1 = [1, 2, 3, 4]
li_st2 = [3, 4, 5, 6]

result = set(li_st1).intersection(li_st2)
print(result)

#Intersection with strings (common characters)
a = set("python")
b = set("typhoon")

result = a.intersection(b)
print(result)

#Intersection within a cycle
group1 = {"Ana", "Luis", "Carlos"}
group2= {"Luis", "Maria"}

in_common = group1.intersection(group2)
print(in_common)

#Intersection to find even numbers in multiple lists
a = {2, 4, 6, 8}
b = {4, 5, 6, 7}

result = a.intersection(b)
print(result)

#Intersection of several sets within a list
sets = [
    {1, 2, 3, 4},
    {2, 3, 5},
    {0, 2, 3, 9}
]

result = sets[0].intersection(*sets[1:])
print(result)

#Intersection to find common products
store_a = {"bread", "milk", "sugar"}
store_b = {"flour", "milk", "bread"}

result = store_a.intersection(store_b)
print(result)

#Intersection to filter repeated data in multiple lists
li_st1 = ["Ana", "Luis", "Carlos"]
li_st2 = ["Carlos", "Pedro", "Ana"]

in_common = set(li_st1).intersection(li_st2)
print(in_common)

#------------------------------difference()------------------------------

#Basic difference between two sets
a = {1, 2, 3, 4}
b = {3, 4, 5}

result = a.difference(b)
print(result)

#Difference when there are no common elements
a = {10, 20, 30}
b = {40, 50}

result = a.difference(b)
print(result)

#Difference with sets where the first one is empty
a = set()
b = {1, 2, 3}

result = a.difference(b)
print(result)

#Difference using lists converted into sets
li_st1 = [1, 2, 3, 4]
li_st2 = [3, 4, 5]

result = set(li_st1).difference(li_st2)
print(result)

#Difference between three sets
a = {1, 2, 3, 4}
b = {2, 4}
c = {1}

result = a.difference(b, c)
print(result)

#Difference with strings (characters exclusive to the first)
a = set("python")
b = set("phone")

result = a.difference(b)
print(result)

#Use difference() to filter out prohibited values
allowed = {10, 20, 30, 40}
prohibited = {20, 40}

result = valid_permissions = allowed.difference(prohibited)
print(result)

#Difference in a data flow
current = {"Ana", "Luis", "Carlos"}
eliminate = {"Carlos"}

result = current.difference(eliminate)
print(result)

#A difference in finding products that aren't in other stores.
store_a = {"bread", "milk", "sugarr", "coffee"}
store_b = {"bread", "coffee"}

result = store_a.difference(store_b)
print(result)

#Multiple difference in sets within a list
sets = [
    {1, 2, 3, 4, 5},
    {2, 5},
    {1, 4}
]

result = sets[0].difference(*sets[1:])
print(result)

#------------------------------clear()------------------------------

#Empty a list
numbers = [1, 2, 3, 4]
numbers.clear()

print(numbers)

#Vaciar un diccionario
person = {"name": "Ana", "age": 25}
person.clear()

print(person)

#Empty a set
fruit = {"apple", "pear", "banana"}
fruit.clear()

print(fruit)

#Empty a list after processing it
tasks = ["clean", "cook", "study"]

for t in tasks:
    print("Made:", t)

tasks.clear()
print(tasks)

#Empty a shopping cart
cart = ["milk", "bread", "rice"]
print("cart before:", cart)

cart.clear()
print("cart later:", cart)

#Reset a configuration dictionary
config = {"tema": "dark", "volumen": 80, "language": "ES"}

config.clear()

print(config)

#Empty a set for reuse
values = {1, 2, 3}
values.clear()

values.add(10)
values.add(20)

print(values)

#Emptying a list into another structure
users = {
    "active": ["Ana", "Luis", "Carlos"],
    "inactive": ["Pedro"]
}

users["active"].clear()

print(users)

#Empty data to free up memory in a process
buffer = [100, 200, 300]
print("Buffer:", buffer)

buffer.clear()

print("buffer cleared:", buffer)

#Empty a set before filling it with new unique values
unique = {1, 2, 3}
unique.clear()

for n in [4, 4, 5, 6]:
    unique.add(n)

print(unique)

