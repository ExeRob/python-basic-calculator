#------------------------------append()------------------------------

#Add new data to a list
employees = ["Ana", "Carlos", "María"]
employees.append("Lucas")

print(employees)

#Building a list from a loop
numbers = []
for i in range(1, 6):
    numbers.append(i * 10)

print(numbers)

#Read and store data
#products = []

#for i in range(3):
#    name = input("Enter the product name: ")
#    products.append(name)

#print("Products loaded:", products)

#Filter data and save it
ages = [12, 18, 25, 16, 30, 40]
older = []

for age in ages:
    if age >= 18:
        older.append(age)

print("Adults:", older)

#Build a list from the results of a function
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
results = []

for n in numbers:
    results.append(square(n))

print("Squares:", results)

#Add dictionaries (records) to a list
customers = []

customers.append({"name": "Ana", "age": 28})
customers.append({"name": "Luis", "age": 35})

print(customers)

#Create a list with processed data
names = ["juan", "maria", "carla"]
capitalized_names = []

for n in names:
    capitalized_names.append(n.capitalize())

print(capitalized_names)

#Accumulate errors or messages
errors = []
records = ["ok", "error", "ok", "error"]

for r in records:
    if r == "error":
        errors.append("Error detected in registry")

print("List of errors:", errors)

#Create a list of valid files
files = ["data.csv", "foto.jpg", "reporte.xlsx", "script.py"]
valid = []

for file in files:
    if file.endswith((".csv", ".xlsx")):
        valid.append(file)

print("Valid files:", valid)

#Load numerical data and calculate the average
#numbers = []

#for i in range(3):
#    n = float(input("Enter a number: "))
#    numbers.append(n)

#average = sum(numbers) / len(numbers)
#print("Average:", average)

#Save valid results after validations
in_put = ["123", "abc", "456", "78x", "999"]
numerical_values = []

for i in in_put:
    if i.isdigit():
        numerical_values.append(int(i))

print(numerical_values)

#Create a dynamic list in a system
#tasks = []
#while True:
#    task = input("Add task (or 'end' to leave): ")
#    if task.lower() == "end":
#        break
#    tasks.append(task)

#print("📋 Tasks of the day:", tasks)

#Generate a list of dates, prices, or logs
from datetime import datetime

logs = []
for i in range(3):
    logs.append(f"Register {i+1} - {datetime.now().strftime('%H:%M:%S')}")

print(logs)

#Accumulate calculation results
values = [5, 10, 15]
double = []

for v in values:
    double.append(v * 2)

print("Results:", double)

#------------------------------extend()------------------------------

#Merge two data lists
employees_1 = ["Ana", "Carlos", "Lucía"]
employees_2 = ["Marcos", "Julieta"]

employees_1.extend(employees_2)
print("Total Employee List:", employees_1)

#Add multiple new values ​​to an existing list
sales = [150, 200, 250]
new_sales = [300, 350]

sales.extend(new_sales)
print("Total sales:", sales)

#Merge data from different departments
department_A = ["Luis", "Ana"]
department_B = ["Jorge", "María"]
team = []

team.extend(department_A)
team.extend(department_B)

print("Complete equipment:",team)

#Add multiple elements to the end from a loop
numbers = [1, 2, 3]

for i in range(4, 7):
    numbers.extend([i])

print(numbers)

#Combine results from different calculations
even = [2, 4, 6]
odd = [1, 3, 5]

all = []
all.extend(even)
all.extend(odd)

print("Combined list:", all)

#Load data from multiple sources
data_csv = ["name", "age", "city"]
data_api = ["mail", "phone"]

fields = []
fields.extend(data_csv)
fields.extend(data_api)

print("Combined fields:", fields)

#Extend a list with another tuple
fruit = ["apple", "pear"]
new = ("banana", "orange")

fruit.extend(new)
print("Updated fruits:", fruit)

#Create a list of available products
products = ["rice", "chicken"]
new_products = ["meat", "fish", "pasta"]

products.extend(new_products)
print("Updated stock:", products)

#Merge filtered record lists
may_sales = [100, 200]
june_sales = [150, 250]

total_sales = []
total_sales.extend(may_sales)
total_sales.extend(june_sales)

print("Combined sales:", total_sales)

#Add characters from a string
letters = ["a", "b"]
letters.extend("cd")

print(letters)

#Load partial data into a final list
final_data = []
batch_1 = [10, 20]
batch_2 = [30, 40]
batch_3 = [50, 60]

for batch in [batch_1, batch_2, batch_3]:
    final_data.extend(batch)

print("Combined data:", final_data)

#Extend list with unique items
numbers = [1, 2, 3]
new = [3, 4, 5]

for n in new:
    if n not in numbers:
        numbers.append(n)

print("No duplicates:", numbers)

#Extend system log list
logs = ["System startup"]
events = ["logged in user”", "File uploaded", "Process completed"]

logs.extend(events)
print("📋 system logs:", logs)

#Combine lists created with comprehension
even = [x for x in range(2, 11, 2)]
odd = [x for x in range(1, 10, 2)]

numbers = []
numbers.extend(even)
numbers.extend(odd)

print("All numbers:", numbers)

#Combine data read from different files
archive_1 = ["data1", "data2"]
archive_2 = ["data3", "data4"]

all_the_data = []
all_the_data.extend(archive_1)
all_the_data.extend(archive_2)

print("Combined data:", all_the_data)

#------------------------------insert()------------------------------

#Insert an element in a specific position
numbers = [10, 20, 30, 40]

numbers.insert(2, 25)
print("Updated list:", numbers)

#Insert at the beginning of a list
names = ["Ana", "Pedro", "Sofía"]
names.insert(0, "Lucía")

print("Updated list:", names)

#Insert an item only if it is not in the list
fruit = ["apple", "pear", "orange"]

if "kiwi" not in fruit:
    fruit.insert(1, "kiwi")

print("Updated list:", fruit)

#Insert an item in the middle of the list
numbers = [1, 2, 3, 4, 5, 6]
half = len(numbers) // 2
numbers.insert(half, 99)

print("Updated list:", numbers)

#Insert based on condition (after a specific value)
values = [5, 10, 15, 20, 25]
search = 15

if search in values:
    in_dex = values.index(search)
    values.insert(in_dex + 1, 99)

print("Updated list:", values)

#Insert items between two lists
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

for i in range(len(numbers)):
    letters.insert(i * 2 + 1, numbers[i])

print("Updated list:", letters)

#Insert after the highest number
values = [3, 8, 1, 5]
maximum = max(values)
index_max = values.index(maximum)

values.insert(index_max + 1, 100)
print("Updated list:", values)

#Insert multiple values ​​in specific positions
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
colors.insert(3, "violet")

print("Updated list:", colors)

#Insert elements dynamically
products = ["milk", "bread", "cheese"]
new = input("Enter a new product: ")
position = int(input("Enter the position where you want to insert it: "))

products.insert(position, new)
print("Updated list:", products)   

#------------------------------pop()------------------------------

#Delete last item
fruit = ["apple", "pear", "orange", "banana"]
removed = fruit.pop()

print("Deleted item:", removed)
print("Updated list:", fruit)

#Remove one item per position
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)

print("Deleted item:", removed)
print("Updated list:", numbers)

#Using pop() inside a loop
animals = ["cat", "dog", "parrot", "rabbit"]

while animals:
    removed = animals.pop()
    print("Removed:", removed)

print("Final List:", animals)

#Save deleted items to another list
tasks = ["read", "cook", "train", "sleep"]
completed_tasks = []

while tasks:
    done = tasks.pop()
    completed_tasks.append(done)

print("Tasks performed:", done)
print("Pending tasks:", tasks)

#Remove the first element (using index 0)
numbers = [5, 10, 15, 20]
removed = numbers.pop(0)

print("Removed:", removed)
print("Updated list:", numbers)

#Delete and use the deleted value
price = [100, 200, 300, 400]
discount = price.pop(1) * 0.10

print("Discount applied to:", discount)
print("Updated list:", price)

#Delete multiple items (by index and by default)
colors = ["red", "green", "blue", "yellow", "violet"]

colors.pop(0)   
colors.pop()    

print("Updated list:", colors)

#Error control (index out of range)
numbers = [1, 2, 3]

try:
    numbers.pop(5)
except IndexError:
    print("Error: Index out of range")

print("Current list:", numbers)

#------------------------------remove()------------------------------

#Delete a specific item
frutas = ["manzana", "pera", "banana", "naranja"]
frutas.remove("banana")

print("Lista actualizada:", frutas)

#Remove only the first match
numeros = [1, 2, 3, 2, 4, 2]
numeros.remove(2)

print("Lista actualizada:", numeros)

#Remove a value if it is present
colores = ["rojo", "verde", "azul"]

if "verde" in colores:
    colores.remove("verde")

print("Lista actualizada:", colores)

#Error handling with try and except
animales = ["gato", "perro", "conejo"]

try:
    animales.remove("loro")
except ValueError:
    print("Error: el elemento no existe en la lista")

print("Lista actual:", animales)

#Remove multiple items with a loop
numeros = [1, 2, 3, 2, 4, 2, 5]

while 2 in numeros:
    numeros.remove(2)

print("Lista sin el número 2:", numeros)

#Remove items based on a condition
edades = [12, 18, 25, 30, 15, 40]

for edad in edades[:]:  
    if edad < 18:
        edades.remove(edad)

print("Edades filtradas:", edades)

#Use remove() together with append()
pendientes = ["lavar", "cocinar", "leer", "dormir"]
hechas = []

tarea = "leer"
if tarea in pendientes:
    pendientes.remove(tarea)
    hechas.append(tarea)

print("Pendientes:", pendientes)
print("Hechas:", hechas)

#Remove all elements from a list according to another set
inventario = ["pan", "leche", "queso", "harina", "manteca"]
agotados = ["leche", "manteca"]

for producto in agotados:
    if producto in inventario:
        inventario.remove(producto)

print("Inventario actualizado:", inventario)

#Clear the list completely (alternative to clear())
elementos = [10, 20, 30, 40]

while elementos:
    elementos.remove(elementos[0])

print("Lista vacía:", elementos)

#------------------------------sort()------------------------------

#Sort a list of numbers
numbers = [5, 2, 9, 1, 7]
numbers.sort()

print("Sorted list:", numbers)

#Sort a list alphabetically
fruit = ["orange", "banana", "apple", "pear"]
fruit.sort()

print("Sorted list:", fruit)

#Sort in descending order
numbers = [10, 3, 5, 8, 1]
numbers.sort(reverse=True)

print("Descending order:", numbers)

#Sort a list of strings ignoring case
names = ["ana", "Pedro", "maria", "Juan"]
names.sort(key=str.lower)

print("Sorted list:", names)

#Sort a list of lists (by the first value)
even_numbers = [[3, 5], [1, 2], [4, 1], [2, 7]]
even_numbers.sort()

print("Sorted list:", even_numbers)

#Sort by a specific part of the sublist
students = [["Ana", 8], ["Juan", 10], ["Pedro", 6], ["Sofía", 9]]
students.sort(key=lambda x: x[1])

print("Students ranked by grade:", students)

#Sort by word length
words = ["python", "sun", "programming", "code", "pc"]
words.sort(key=len)

print("Sorted by length:", words)

#Ordering negative and positive numbers
numbers = [5, -2, 10, 0, -8, 3]
numbers.sort()

print("Sorted list:", numbers)

#Order by absolute value
values = [-5, 3, -1, 10, -8]
values.sort(key=abs)

print("Ordered by absolute value:", values)

#------------------------------reverse()------------------------------

#Reverse a list of numbers
numbers = [1, 2, 3, 4, 5]
numbers.reverse()

print("inverted list:", numbers)

#Reverse a list of strings
fruit = ["apple", "pear", "orange", "banana"]
fruit.reverse()

print("Inverted list:", fruit)

#Reverse an ordered list
numbers = [1, 3, 5, 7, 9]
numbers.reverse()

print("List in descending order:", numbers)

#Combine sort() + reverse()
ages = [15, 42, 30, 18, 25]

ages.sort()
ages.reverse()

print("From highest to lowest:", ages)

#Show original list and reversed list (without modifying the original)
names = ["Ana", "Pedro", "Lucía", "Juan"]
inverted = list(reversed(names))

print("Original:", names)
print("Inverted:", inverted)

#Reverse list of lists (sublists)
even_numbers = [[1, 2], [3, 4], [5, 6], [7, 8]]
even_numbers.reverse()

print("Inverted list:", even_numbers)

#Reverse the characters of a word using a list
words = "python"
letters = list(words)
letters.reverse()
inverted = "".join(letters)

print("inverted word:", inverted)

#Reverse a list only partially
numbers = [1, 2, 3, 4, 5, 6]

partial = numbers[2:5]
partial.reverse()

print("Inverted part:", partial)
print("Original List:", numbers)

#Invest and go through the list at the same time
values = [10, 20, 30, 40, 50]
values.reverse()

for v in values:
    print("Values:", v) 

#------------------------------count()------------------------------

##Counting a number in a list
numbers = [1, 2, 3, 2, 4, 2, 5]
number_of_numbers = numbers.count(2)

print("The number 2 appears:", number_of_numbers, "times")

#Counting a word in a list of strings
fruit = ["apple", "pear", "banana", "pear", "orange", "pear"]
print("The word 'pear' appears:", fruit.count("pear"), "times")

#Counting letters in a word
words = "programming"
print("The letter 'o' appears:", words.count("o"), "times")

#Counting a substring within another
text = "Python is powerful and Python is easy"
print("The word 'Python' appears:", text.count("Python"), "times")

#Be case-sensitive
phrase = "Hello hello Hello HELLO"
print("Number of 'hello'':", phrase.count("hello"))

#Counting elements within a list of repeated numbers
exam_notes = [10, 7, 8, 10, 9, 10, 6, 10]
print("Times the number 10 appears:", exam_notes.count(10))

#Counting occurrences within a tuple
tuple_colors = ("red", "blue", "green", "red", "red", "yellow")
print("The color 'red' appears:", tuple_colors.count("red"), "times")

#Counting specific characters in a sentence
phrase = "Learning Python is fun"
print("Number of spaces:", phrase.count(" "))

#Count how many times each element appears (using a loop)
colors = ["red", "blue", "red", "green", "blue", "red"]

for color in set(colors):
    print(color, "→", colors.count(color))
    
#Counting words in a text
text = "Python is easy and Python is powerful"
words = text.split()
print("The word 'python' appears:", words.count("python"))

#------------------------------index()------------------------------

#Find the index of a number
numbers = [10, 20, 30, 40, 50]

position = numbers.index(30)
print("The number 30 is in position:", position)

#Find the first occurrence of a repeated value
names = ["Ana", "Luis", "Ana", "Pedro"]
print(names.index("Ana"))

#Find the index of an element in a tuple
colors = ("red", "blue", "green", "blue")

position = colors.index("blue")
print(position)

#Find the index of a letter in a string
text = "programming"
print(text.index("a"))

#Avoid error if the element does not exist
fruit = ["apple", "banana", "orange"]

if "pear" in fruit:
    print(fruit.index("pear"))
else:
    print("Pear is not on the list")
    
#Avoid error if the element does not exist
fruit = ["apple", "banana", "orange"]

if "pear" in fruit:
    print(fruit.index("pear"))
else:
    print("Pear is not on the list")
    
#Finding the second occurrence of a value
li_st = [5, 3, 5, 7, 5]

first = li_st.index(5)
second = li_st.index(5, first + 1)

print("First:", first)
print("Second:", second)

#Find the position of the maximum value
numbers = [4, 9, 2, 9, 1]

maximum = max(numbers)
position = numbers.index(maximum)

print("largest number:", maximum, "→ Position:", position)

#Search index within a range
letters = ["a", "b", "c", "d", "b", "e"]

position = letters.index("b", 2, 5)
print(position)

#Change an element using index()
animals = ["dog", "cat", "fish"]

position = animals.index("cat")
animals[position] = "Siamese cat"

print(animals)

#Counting and finding positions (mixed with count())
values = [1, 2, 3, 2, 4, 2]

print("appears,:", values.count(2), "times")
position = values.index(2)

print("First position:", position)