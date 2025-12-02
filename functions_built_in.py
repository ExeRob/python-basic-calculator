#------------------------------(print)------------------------------

#Print a simple message
print("Genau")

#Print multiple lines
print("Bis Montag")
print("¿Wie get es dir?")
print("Entschuldigen Sie")

#Print numbers
print(10)
print(3.14)

#Print the result of an operation
print(5 + 3)
print(10 * 2)
print(15 / 3)

#Concatenate text and numbers
age = 25
print("I am " + str(age) + " years old")    

#Using commas in print to separate values
name = "Exequiel"
age = 33
print("My name is", name, "and I am", age, "years old")

#Print with formatting using f-strings
name = "Exequiel"
age = 33
print(f"My name is {name} and I am {age} years old")

#Print special characters
print("Hola\nMundo")  # salto de línea
print("Hola\tMundo")  # tabulación

#Print results of complex operations
a = 10
b = 5
print(f"The sum is {a + b}, the subtraction is {a - b}, the product is {a * b}, and the division is {a / b}")

#Print lists and variables
fruit = ["apple", "banana", "orange"]
print("My favorite fruits are:", fruit)

#Print with repeat
print("Python " * 5)

#------------------------------input()------------------------------

#Ask for the username
name = input("Enter your name: ")
print("Hello", name)

#ask for a number
number = input("Enter a number: ")
print("The number you entered is:", number)

#Request various data
name = input("Enter your name: ")
edad = input("Enter your age: ")

print("hello", name, "you have", edad, "years old")

#Add two entered numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

suma = num1 + num2
print("The sum is:", suma)

#Calculate the average of three numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

average = (n1 + n2 + n3) / 3
print("The average is:", average)

#Concatenate first and last name
name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Your full name is:", name + " " + last_name)

#Convertir de metros a centímetros
meters = float(input("Enter the measurement in meters: "))
centimeters = meters * 100
print(meters, "the meters are", centimeters, "centimeters")

#Convert age to months
age = int(input("Enter your age in years: "))
months = age * 12
print("Your age in months is:", months)

#Check if a number is greater than 10
number = int(input("Enter a number: "))
if number > 10:
    print("The number is greater than 10")
else:
    print("The number is 10 or less")
    
#Ask for a number and show its square and cube
number = int(input("Enter a number: "))
print(f"the square of {number} es {number*2} and the cube is {number*3}")

#------------------------------len()------------------------------

#with a string
text = "Python"
print(len(text))

#with a list
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

#with a tuple
colors = ("red", "green", "blue")
print(len(colors))

#with a dictionary
person = {"name" : "Exequiel", "age" : "33", "city" : "Buenos Aires"}
print(len(person))

#with a set
fruit = {"apple", "pear", "banana"}
print(len(fruit))

#with a for loop using range
animals = ["dog", "cat", "parrot"] #definimos una lista que contiene tres strings

for i in range(len(animals)): #len(animals) devuelve la cantidad de elemntos de la lista / range(len(animals)) genera un rango de numeros 

 print(f"Índex {i} → {animals[i]}")
    
#Function that counts the characters of a string
def count_string(string):
    return len(string)

print(count_string("einhundertsiebenundvierzig"))

#function that tells if a list is empty     
def empty_list(list):
    if len(list) == 0:
        return "The list is empty"
    else:
        return "The list has elements"
    
print(empty_list([]))
print(empty_list([1,2,3]))

#function that finds the longest word using max
def longest_word(word_list):
    return max(word_list, key=len) #la funcion max() busca el elemento  maximo dentro de la lista
                                   #el argumento key=len le indica a max que no compare las palabas por su valor alfabetico sino por su longitud (len)
print(longest_word(["acht", "zwanzig", "sechsundfunzig","zwei"]))

#Function that counts how many words a text has
def counting_words(text):
    words = text.split()
    return len(words)

print(counting_words("Hallo wie geht es dir"))


#------------------------------type()------------------------------

#type of values
print(type(5))        # int
print(type(5.3))      # float
print(type("hola"))   # string
print(type(True))     # bool

#lists, dictionaries and tuples
print(type([]))
print(type({}))
print(type(()))

#Compare types
x = 10
y = "10"

if type(x) == type(y):
    print("They are the same type")
else:
    print("They are different")  

#Detect input type
#value = input("Write something: ")

#print("The type of value entered is:", type(value)) #Will always be str 

#try:                 #we convert to int
#    num = int(value)
#    print("Converted to int:", num, type(num))
#except:
#    print("Could not be converted to int")
    
#List of different types
data = [123, 45.6, "Hello", True, [1,2], {"a":1}]

for item in data:
    print(item, "->", type(item))

#Use type in conditions
values = [10, "text", 3.5, [1, 2, 3]]

for v in values:
    if type(v) == int:
        print(v, "-> Int number")
    elif type(v) == str:
        print(v, "-> Text string")
    elif type(v) == float:
        print(v, "-> Float number")
    elif type(v) == list:
        print(v, "-> Detected list")  
        
#With isinstance()
values = [10, "texto", 3.5, [1, 2, 3]]

for v in values:
    if isinstance(v, int):
        print(v, "-> Int number")
    elif isinstance(v, str):
        print(v, "-> Text string")
    elif isinstance(v, float):
        print(v, "-> Float number")
    elif isinstance(v, list):
        print(v, "-> Detected list")
        
        
#------------------------------ range()------------------------------   

#Print numbers from 1 to 10
for i in range(1, 11):  # Starts at 1, ends at 10 (11 not included)
    print(i)

#Print even numbers from 2 to 20
for i in range(2, 21, 2):  #start at 2, end at 20, step 2
    print(i)    
    
#Add the first 50 numbers
add = 0
for i in range(1, 51):
    add += i
print("the sum is:", add)

#Count backwards
for i in range(10, 0, -1):
    print(i)  

#Iterate over a list with index
fruit = ["apple", "banana", "cherry", "peach"]

for i in range(len(fruit)):
    print(f"{i}: {fruit[i]}")
    
#Custom jumps
for i in range(5, 51, 5):  
    print(i) 

#Multiplication table       
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}") 
    
#Stock control in a warehouse   
stock = [12, 5, 0, 7, 3, 10, 0, 4]

print("Products out of stock on the shelves:")
for i in range(len(stock)):
    if stock[i] == 0:
        print(f"- Shelf {i}")   
        
#Calculate multiples in a range
multiples = [i for i in range(50, 201) if i % 7 == 0] #la condición i % 7 == 0 filtra y deja pasar solo los números que son múltiplos de 7
print(multiples)

##Adding even numbers in a range
sum_of_even_numbers = sum(i for i in range(2, 101, 2))
print("the total sum is:", sum_of_even_numbers)

#to list a series of products
products = ["bread", "milk", "rice", "chicken"]

for i in range(len(products)): #len(products) → devuelve la cantidad de elementos (en este caso 4) #range(len(products)) → genera una secuencia de índices [0, 1, 2, 3]

    print(f"{i+1}. {products[i]}") #i+1 → se usa para que la numeración empiece en 1 (porque por defecto en Python los índices comienzan en 0)
                                   #products[i] → accede al producto en la posición correspondiente
                                   
##Calculate the total cost of purchases
price = [1200, 850, 600, 400]

total = 0
for i in range(len(price)):
    total += price[i]

print("Total  purchase:", total)

#Display even numbers up to 50
for i in range(0, 51, 2):
    print(i,end=" ") #separa con un espacio en vez de saltar linea, si no dejamos el espacio no hace el salto de linea                                    

#Count how many values meet a condition
temperatures = [12, 18, 21, 25, 30, 10, 15]

warm_days = 0
for i in range(len(temperatures)):
    if temperatures[i] > 20:
        warm_days += 1

print("number of warm days:", warm_days)

#------------------------------enumerate()------------------------------

#Create a list of products with their position
products = ["Mouse", "Teclado", "Monitor", "Notebook"]

for i, product in enumerate(products, start=1):
    print(f"{i}. {product}")
    
#Traverse a list with index and value
fruit = ["apple", "banana", "cherry"]

for i, fr in enumerate(fruit):
    print(f"{i}: {fr}")
    
#Filter with index and value
numbers = [10, 25, 30, 45, 60]

for i, num in enumerate(numbers): #i es el indice / num es el valor de la posicion 
    if num % 2 == 0: #verifica si el numero es par
        print(f"Index {i} → even number {num}")
        
#Create a dictionary with indexes
fruit = ["apple", "banana", "cherry"]

dictionary = dict(enumerate(fruit))

print(dictionary)

#Update values ​​in a list using the index
prices = [100, 200, 300]

for i, price in enumerate(prices):
    prices[i] = price * 1.10  #aumento del 10% / prices[i] es el indice que va a iterar los elementos de la variable 

print(prices)

#Compare two lists at the same time
products = ["Mouse", "Keyboard", "Monitor"]

stock = [12, 5, 0]
for i, product in enumerate(products):
    print(f"{i} - {product}: {stock[i]} in stock")
    
##Search for an item and display its index
fruit = ["apple", "banana", "cherry", "pear"]

for i, fr in enumerate(fruit): 
    if fr == "cherry":
        print(f"Found in position {i}")
        
#Enumerating in lists of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(f"Row {i}, Column {j} → {value}")
        
#------------------------------zip()------------------------------

#Match two lists
names = ["Ana", "Luis", "Pedro"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old") 
    
#Add elements of two lists
a = [1, 2, 3]
b = [4, 5, 6]

add = [x + y for x, y in zip(a, b)]
print(add)

#Create dictionary from two lists (one of the most practical uses)
keys = ["name", "age", "city"]
values = ["Ana", 25, "Buenos Aires"]

my_dict = dict(zip(keys, values)) #zip(keys, values) combina ambas listas/dict() convierte esa lista de pares en un diccionario
print(my_dict)     

#Compare elements of two lists
list1 = [10, 20, 30]
list2 = [10, 25, 30]

for x, y in zip(list1, list2):
    if x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is different from {y}")
        
#Multiply values ​​from two lists
x = [2, 4, 6]
y = [3, 5, 7]

product = [i * j for i, j in zip(x, y)]
print(product)

#Loop through two lists at the same time
products = ["Mouse", "Keyboard", "Monitor"]
prices = [1200, 3500, 8000]

for product, price in zip(products, prices):
    print(f"{product}: ${price}")
    
#Combine lists of different lengths
a = [1, 2, 3, 4]
b = [10, 20]

combined = list(zip(a, b)) #zip(a, b) crea pares, pero como iterador.
print(combined)            #list(zip(a, b)) los convierte en una lista para que se pueda manipular facilmente

#Transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix)) #zip(*matrix) → transpone la matriz (convierte filas en columnas) /  *operador desempaquetado
print(transposed)               #zip(matrix) → solo mete cada fila en una tupla de un elemento.

#Compare elements of two lists
a = [5, 8, 2]
b = [3, 9, 4]

older = [max(x, y) for x, y in zip(a, b)]
print(older)

#Concatenate strings from two lists
words1 = ["Py", "Ja", "Ru"]
words2 = ["thon", "va", "by"]

result = [w1 + w2 for w1, w2 in zip(words1, words2)]
print(result)

#List pairs with index
a = ["a", "b", "c"]
b = [1, 2, 3]

for i, (x, y) in enumerate(zip(a, b), start=1): 
    print(f"{i}. {x} - {y}")
    
#------------------------------max()------------------------------

#Finding the largest number in a list
numbers = [4, 7, 1, 9, 2]

older = max(numbers)
print("The largest number is:", older)

#Compare multiple values
a = 15
b = 27
c = 12

older = max(a, b, c)
print("The largest among a, b and c is:", older)

#Find the longest word in a list
words = ["apple", "pear", "banana", "kiwi"]

older = max(words, key=len)
print("The longest word is:", older)

#Finding the maximum age in a dictionary
ages_and_names = {"Ana": 25, "Luis": 30, "María": 22}

older = max(ages_and_names.values())
print("The oldest age is:", older)

#Maximum of a list of tuples (comparison by first value)
tuples = [(2, 5), (3, 1), (10, 7), (8, 9)]
print(max(tuples))

#Maximum of a list of tuples (comparison by second value)
tuples = [(2, 5), (3, 1), (10, 7), (8, 9)]
print(max(tuples, key=lambda x: x[1])) #En este caso la función es lambda x: x[1], es decir: para cada tupla x, toma su segundo elemento (x[1]) y usa ese número para decidir cuál es el mayor.

#Hottest day in a temperature dictionary
temperatures = {"Lunes": 21, "Martes": 25, "Miércoles": 19}

hottest = max(temperatures.items(), key=lambda x: x[1]) #items() → devuelve tuplas de (clave, valor) / 
print(hottest)

#Number with the greatest absolute value
nums = [4, 9, -15, 3]
print(max(nums, key=abs))

#Best student in a dictionary list
students = [
    {"name": "Ana", "score": 85},
    {"name": "Luis", "score": 92},
    {"name": "Pedro", "score": 78}
]   

top = max(students, key=lambda x: x["score"])
print(top)

#------------------------------min()------------------------------

#find the smallest number
numbers = [15, 22, 8, 19, 31]

small_num = min(numbers)
print("The smallest number is:", small_num)

#Minimum of multiple variables
a = 12
b = 7
c = 20

minimum_value = min(a, b, c)
print("The minimum value is:", minimum_value)

#minimum of a list of lists
matrix = [
    [4, 9, 1],
    [7, 2, 5],
    [8, 6, 3]
]

for row in matrix:
    print("The minimum of the row", row, "is", min(row))
    
#minimum with strings
words = ["apple", "banana", "pear", "kiwi"]

minimum_word = min(words)
print("The minimum word is:", minimum_word)    

#minimum with key
words = ["apple", "banana", "pear", "kiwi"]

mini_word = min(words, key=len) #Con el argumento key=len, le estamos diciendo que compare los elementos basándose en su longitud (len)
print("The shortest word is:", mini_word)

#minimum of a list with conditions
numbers = [4, 15, 22, 8, 19, 31]

older_10 = [n for n in numbers if n > 10]
print("The smallest number greater than 10 is:", min(older_10))

#------------------------------sum()------------------------------

#Add all the numbers in a list
numbers = [5, 10, 15, 20]

result = sum(numbers)
print("The total sum is:", result)

#Sum of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [n for n in numbers if n % 2 == 0]
print("The sum of even numbers is:", sum(even_numbers))  

#Sum of squares
numbers = [1, 2, 3, 4, 5]

sum_of_squaress = sum(n ** 2 for n in numbers)
print("The sum of the squares is:", sum_of_squaress)  

#Sum of values ​​in a dictionary
sales = {"Monday": 100, "Tuesday": 200, "Wednesday": 150}

total = sum(sales.values())
print("Total sales are:", total)

#Sum accumulated with condition
numbers = [10, 25, 30, 12, 5, 8]

older_15 = [n for n in numbers if n > 15]
print("The sum of the numbers greater than 15 is:", sum(older_15))

#------------------------------sorted()------------------------------

#Sort a list of numbers (ascending and descending)
numbers = [5, 2, 9, 1, 7]

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

#Sort words alphabetically
words = ["banana", "apple", "pear", "kiwi"]
print("Alphabetic order:", sorted(words))

#Sort by word length
words = ["banana", "grape", "watermelon", "pear"]

ordered = sorted(words, key=len)
print("by length:", ordered)

#Sort a list of tuples by the second element
even = [(1, 5), (3, 2), (4, 9), (2, 1)]

ordered = sorted(even, key=lambda x: x[1])
print("Sorted by second value:", ordered)

#Sort a dictionary by its values
grades = {"Ana": 8, "Luis": 6, "Pedro": 9, "Marta": 7}

ordered = sorted(grades.items(), key=lambda x: x[1])
print("Grades sorted by value:", ordered)

#Remove duplicates and sort
numbers = [4, 2, 9, 2, 4, 1, 9, 7]

result = sorted(set(numbers))
print("No duplicates and sorted:", result)

#Sort ignoring case
words = ["banana", "apple", "pear", "Kiwi"]

ordered = sorted(words, key=str.lower)  
print("Ignoring capital letters:", ordered)

#Sort a list of numbers by their absolute value
numbers = [-10, 5, -3, 8, -20]

ordered = sorted(numbers, key=abs)
print("By absolute value:", ordered)

#------------------------------any()------------------------------

#Check if there is any positive number
numbers = [-5, -2, -1, 0, 3]

result = any(n > 0 for n in numbers)
print("¿Are there any positive numbers?", result)

#Check if there is any non-empty string
words = ["", "", "hello", ""]

result = any(words)
print("¿Is there any non-empty string?", result)

#Detect if a student passed
grades = [3, 2, 4, 7]

result = any(grade >= 6 for grade in grades)
print("¿Did the student pass any subjects?", result)

#Check if a list contains even numbers
numbers = [1, 3, 5, 9, 11]

result = any(n % 2 == 0 for n in numbers)
print("¿Is there an even number?", result)

#Check if there is a True value in a list of conditions
conditions = [False, False, True, False]
print(any(conditions))

#Find if a word contains vowels
word = "rhythm"
vowels = "aeiou"

result = any(letter in vowels for letter in word)
print("¿Does the word have any vowels?", result)

#Check if any file has the .txt extension
files = ["datas.csv", "report.pdf", "note.txt", "image.png"]    

result = any(name.endswith(".txt") for name in files)
print("¿Is there a .txt file?", result)

#Check for numbers greater than 100
numbers = [20, 50, 99, 150, 80]

result = any(n > 100 for n in numbers)
print("¿Is there any number greater than 100?", result)

#Check if a list is completely empty
lists = [[], [], [1, 2], []]

result = any(len(l) > 0 for l in lists)
print("¿Does any list contain items?", result)

#------------------------------all()------------------------------

#Check if all numbers are positive
nums = [3, 5, 7, 10]

result = all(n > 0 for n in nums) #Para cada elemento n en nums evalúa la expresión booleana n > 0 y genera True o False para cada n
print("¿Are all numbers positive?", result)

#Check if all strings are not empty
words = ["hello", "numbers", "python"]

result = all(words)
print("¿Do all strings have content??", result)

#Check if all students passed
grades = [7, 9, 10, 6]

result = all(grade >= 6 for grade in grades)
print("¿Did all the students pass?", result)

#Check if all numbers are even
numbers = [2, 4, 6, 8]

result = all(n % 2 == 0 for n in numbers)
print("¿Did all numbers are even?", result)

#Validate if all passwords meet a minimum of 8 characters
keys = ["password123", "key1234", "12345678"]

result = all(len(c) >= 8 for c in keys)
print("¿Are all passwords secure??", result)

#check if all lists are empty
lists = [[], [], []]

result = all(len(l) == 0 for l in lists)
print("¿All lists are empty??", result)

#Check if all files are .txt
files = ["note.txt", "data.txt", "report.txt"]

result = all(name.endswith(".txt") for name in files) #str.endswith(sufijo) comprueba si la cadena termina con el sufijo dado
print("¿Are all files .txt?", result)

#Check if all numbers are greater than 100
numbers = [150, 200, 300, 400]

result = all(n > 100 for n in numbers)
print("¿Are all numbers greater than 100?", result)

#Verify that all words are in lowercase    
words = ["python", "code", "example"]

result = all(w.islower() for w in words)
print("¿Are all words in lowercase??", result)

#------------------------------map()------------------------------

#Square all numbers with lambda
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))
print(squares)

#Square all numbers with a custom function
def square(x):
    return x ** 2

squares = list(map(square, numbers))
print(squares)

#Square all numbers with a list comprehension
squares = [x ** 2 for x in numbers]
print(squares)

#Change all names to uppercase
names = ["ana", "juan", "sofia", "mario"]

upper_names = list(map(str.upper, names))
print(upper_names)

#Change all names to uppercase with a custom function
def to_upper(name):
    return name.upper()

upper_names = list(map(to_upper, names))
print(upper_names)

#Change all names to uppercase with a list comprehension
upper_names = [name.upper() for name in names]
print(upper_names)

#Convert numbers to string
numbers = [10, 20, 30, 40]

strings = list(map(str, numbers))
print(strings)

#Convert numbers to string with lambda
strings = list(map(lambda x: str(x), numbers))
print(strings)

##Convert numbers to string with a list comprehension
def to_string(x):
    return str(x)

strings = list(map(to_string, numbers))
print(strings)

#Add 100 to each element
nums = [5, 10, 15]

plus_100 = list(map(lambda x: x + 100, nums))
print(plus_100)

#Add 100 to each element with a list comprehension
plus_100 = [x + 100 for x in nums]
print(plus_100)

#Add 100 to each element with a custom function
def add_100(x):
    return x + 100

plus_100 = [add_100(x) for x in nums]
print(plus_100)

#Calculate word lengths
words = ["python", "map", "exercise", "code"]

lengths = list(map(len, words))
print(lengths)

#Calculate word lengths with a list comprehension
lengths = [len(x) for x in words]
print(lengths)

#Calculate word lengths with a custom function
def word_length(word):
    return len(word)

lengths = list(map(word_length, words))
print(lengths)

#Multiply element by its index
nums = [4, 5, 6, 7]

result = list(map(lambda x, i: x * i, nums, range(len(nums))))
print(result)

#Multiply element by its index with a list comprehension
result = [x * i for i, x in enumerate(nums)]
print(result)

#------------------------------filter()------------------------------

#Even numbers
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

#Even numbers with a custom function
def its_even(x):
    return x % 2 == 0

result = list(filter(its_even, numbers))
print(result)

#Even numbers with a list comprehension
numbers = [1, 2, 3, 4, 5, 6]

result = [x for x in numbers if x % 2 == 0] #recorre cada elemento de la lista y mantiene solo los elementos que cumplen la condición
print(result)

#Numbers greater than 10
numbers = [5, 12, 7, 18, 3]

result = list(filter(lambda x: x > 10, numbers))
print(result)

#Numbers greater than 10 with a custom function
numbers = [5, 12, 7, 18, 3]

def greater_than_10(x):
    return x > 10

result = list(filter(greater_than_10, numbers))
print(result)

#Numbers greater than 10 with a list comprehension
numbers = [5, 12, 7, 18, 3]

result = [x for x in numbers if x > 10]
print(result)

#Long words
words = ["sun", "moon", "stars", "heaven"]

result = list(filter(lambda x: len(x) > 4, words))
print(result)

#Long words with a custom function
words = ["sun", "moon", "stars", "heaven"]
def long_words(x):
    return len(x) > 4

result = list(filter(long_words,words))
print(result)

#Long words with a list comprehension
words = ["sun", "moon", "stars", "heaven"]

result = [x for x in words if len(x) > 4 ]
print(result)

#Remove empty strings
words = ["hello", "", "python", "", "map"]

result = list(filter(lambda x: x != "", words))
print(result)  

#Remove empty strings with a list comprehension
result = [x for x in words if word != ""]
print(result)

#Remove empty strings (more simplified)
result = [x for x in words if x]
print(result) 

#Positive numbers
numbers = [-3, 0, 2, -5, 7]

result = list(filter(lambda x: x > 0, numbers))
print(result)

#Positive numbers with a list comprehension
result = [x for x in numbers if x > 0]
print(result)

#Positive numbers with a custom function
def is_positive(x):
    return x > 0

result = [x for x in numbers if is_positive(x)]
print(result)

#Odd numbers
numbers = [10, 15, 22, 33, 40] 

result = list(filter(lambda x: x % 2 != 0, numbers)) 
print(result)

#Odd numbers with a list comprehension
result = [x for x in numbers if x % 2 != 0]
print(result)

#Odd numbers with a custom function
def is_odd(x):
    return x % 2 != 0

result = [x for x in numbers if is_odd(x)]
print(result)

#Words that begin with "p"
words = ["python", "map", "code", "pro"]

result = list(filter(lambda x: x.startswith("p"), words))
print(result)

#Words that begin with "p" with a list comprehension
result = [x for x in words if x.startswith("p")]
print(result)

#Words that begin with "p" with a custom function
def starts_with_p(x):
    return x.startswith("p")

result = [x for x in words if starts_with_p(x)]
print(result)

#Numbers less than or equal to 20
numbers = [12, 25, 7, 30, 20]

result = list(filter(lambda x: x <= 20, numbers))
print(result) 

#Numbers less than or equal to 20 with a list comprehension
result = [x for x in numbers if x <= 20]
print(result)

#Numbers less than or equal to 20 with a custom function
def less_than_or_equal_to_20(list):
    return [x for x in list if x <= 20]

result = less_than_or_equal_to_20(numbers)
print(result)

#Words that contain the letter "a"
words = ["table", "chair", "lamp", "door"]

result = list(filter(lambda x: "a" in x, words))
print(result)

#Words that contain the letter "a" with a list comprehension
result = [x for x in words if "a" in x]
print(result)

#Words that contain the letter "a" with a custom function
def filter_by_a(list):
    return [x for x in list if "a" in x]

result = filter_by_a(words)
print(result)
 
#------------------------------str()------------------------------

#Convert a number to a string
numb = 123

text = str(numb)
print("Number string:", text)
print("Data type:", type(text))

#Concatenate strings 
age = 25

message = "I am " + str(age) + " years old"
print(message)

#Convert a boolean to a string
value = True

text = str(value)
print("Text:", value)
print("Type:", type(value))

#Convert a list to a string
list = [1, 2, 3]

text = str(list)
print("list as string:", text)

#Convert a dictionary to a string
data = {"name": "Ana", "age": 30}

text = str(data)
print("Dictionary as string:", text)

#Save converted data to a single string
name = "Exequiel"
age = 28
weight = 70.5

info = "Name: " + str(name) + ", age: " + str(age) + ", Weight: " + str(weight)
print(info)

#Join numbers in a string to display
a, b, c = 10, 20, 30

result = "The numbers are: " + str(a) + ", " + str(b) + " and " + str(c)
print(result)

#Convert a decimal number to a string and concatenate
pi = 3.14159

text = "The value of pi is " + str(pi)
print(text)

#Pass a set to string
set = {1, 2, 3, 4}

text = str(set)
print("Set converted to string:", text)

#Display multiple types in a single string
name = "Laura"
age = 32
married = False

text = "Name: " + str(name) + " | Age: " + str(age) + " | Married: " + str(married)
print(text)

#------------------------------int()------------------------------

#Convert a decimal number to an integer
number = 8.7 

integer = int(number) ##redondea hacia abajo (trunca)
print("Integer:", integer) 

#Convert a numeric string to an integer
text = "456"

number = int(text)
print("Number + 10 =", number + 10)
                            
#Convert Boolean values
print(int(True))   
print(int(False))

#Calculate the discounted price (converting string to int)
price = "1500"
discount = "300"

final_price = int(price) - int(discount)
print("Final price:", final_price)

#Convert a list of strings to integers
list_str = ["1", "2", "3", "4"]

list_int = [int(x) for x in list_str]
print(list_int)

#Add two numbers that the user enters as strings
a = input("Number 1: ")
b = input("Number 2: ")

sum = int(a) + int(b)
print("The sum is:", sum)

#Save only the integer part of a division
division = 17 / 4
i = int(division)
print(i)

#------------------------------float()------------------------------

#Convert a string to a decimal number
num_str = "3.14"

num = float(num_str)
print(num * 2)

#Convert an integer to a float
num = 7

num_float = float(num)
print(num_float)

#Read a decimal number from the user and multiply it by 10
price = float(input("Enter a price: "))
print("The price for 10 units is:", price * 10)

#Calculate the average of a list of integers (using float to avoid truncation)
numbers = [3, 4, 5]

average = float(sum(numbers)) / len(numbers) #sum(numbers) → suma todos los valores de la lista
print(average)                               #len(numbers) → da la cantidad de elementos en la lista

#------------------------------list()------------------------------

#Convert a string to a list of characters
text = "python"
lis_ta = list(text)

print(lis_ta)

#Create a list from a range of numbers
numbers = list(range(1, 6))
print(numbers)

#Convert a tuple to a list
tu_ple = (10, 20, 30)
li_st = list(tu_ple)

print(li_st)

#Convert a set to a list
my_set = {5, 10, 15}

li_st = list(my_set)
print(li_st)

#Separate a word into letters and put it back together
word = "scheise"

li_st = list(word)
print(li_st)   
new = "".join(li_st)
print(new)

#List of words from a phrase
phrase = "Hallo Ricardo, ich bin noch beim Zahnarzt. Können wir die heutige Stunde morgen oder am Freitag oder am Samstag nachholen?"

words = list(phrase.split())
print(words)

#Create a list of digits from a number
number = 2025

list_digits = list(str(number))
print(list_digits)

#------------------------------(dict)------------------------------

#Create an empty dictionary
my_dict = dict()
print(my_dict)

#Create a dictionary from key-value pairs
my_dict = dict(name="Ana", age=25, city="Madrid")
print(my_dict)

#Convert a list of tuples to a dictionary
li_st = [("a", 1), ("b", 2), ("c", 3)]

my_dict = dict(li_st)
print(my_dict)

#Convert two lists into a dictionary with zip
ke_ys = ["name", "age", "city"]
values = ["Luis", 30, "Buenos Aires"]

my_dict = dict(zip(ke_ys, values))
print(my_dict)

#Create a dictionary of letters and their position
text = "python"

my_dict = dict((letter, i) for i, letter in enumerate(text))
print(my_dict)

#Create a dictionary from a range
my_dict = dict((x, x**2) for x in range(1, 6))
print(my_dict)

#Clone a dictionary with dict()
original = {"a": 1, "b": 2}

copy = dict(original)
copy["c"] = 3
print("Original:", original)
print("Copy:", copy)

#------------------------------(set)------------------------------

#Create an empty set
my_set = set()
print(my_set)

#Create a set from a list
numbers = [1, 2, 2, 3, 4, 4, 5]

my_set = set(numbers)
print(my_set)

#Create a set from a string
word = "banana"

my_set = set(word)
print(my_set)

#Remove duplicates from a list
fruit = ["apple", "pear", "apple", "orange", "pear"]

without_repeating = list(set(fruit))
print(without_repeating)

#Convert a tuple to a set
tu_ple = (10, 20, 20, 30, 40, 40)

my_set = set(tu_ple)
print(my_set)

#Clone a set 
original = {1, 2, 3}

copy = set(original)
copy.add(4)
print("Original:", original)
print("Copy:", copy)

#------------------------------(round)------------------------------

#Round a decimal number to the nearest whole number
number = 3.7

result = round(number)
print(result)

#Round a number down
number = 5.2

result = round(num)
print(result)

#Round a number to specific decimal places
number = 3.14159

result = round(number, 2)  
print(result)

#Rounding a negative number with decimals
number = -2.71828

result = round(number, 3)  
print(result)

#Round numbers in a list
numbers = [1.2, 2.5, 3.7, 4.4]

ro_und = [round(n) for n in numbers]
print(ro_und)

#Round to tens or hundreds
number = 456

result = round(number, -1)  # Redondear a la decena más cercana
print(result)

result2 = round(number, -2) # Redondear a la centena más cercana
print(result2)

#Round and convert to integer
number = 7.9

result = int(round(number))
print(result)

#------------------------------(dir)------------------------------

#View the methods of a string
text = "Hallo Ricardo, heute reise ich nach Mar del Plata und komme am Dienstag zurück"
print(dir(text))

#View the methods of a number
number = 42
print(dir(number))

#Using dir() on a list
my_list = [1, 2, 3]
print(dir(my_list))

#View the attributes of a dictionary
my_dict = {"a": 1, "b": 2}
print(dir(my_dict))



