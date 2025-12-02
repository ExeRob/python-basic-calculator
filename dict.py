#------------------------------keys()------------------------------

#Show all the keys in a dictionary
person = {"name": "Juan", "age": 30, "city": "Córdoba"}

print(person.keys())

#Convert the keys to a list
product = {"id": 101, "name": "Mouse", "price": 4500}

ke_ys = list(product.keys())
print(ke_ys)

#Iterate through the keys with a loop
student = {"name": "Ana", "note": 9, "subject": "Python"}

for ke_y in student.keys():
    print("key:", ke_y)
    
#To know if a key exists
employee = {"name": "Luis", "workstation": "Sales"}

if "workstation" in employee.keys():
    print("The key exists")
    
#Obtain keys and then access values
car = {"Car brand": "Ford", " Car model": "Fiesta", "age": 2018}

for ke_y in car.keys():
    print(ke_y, "→", car[ke_y])
    
#See how many keys a dictionary has
data = {"a": 1, "b": 2, "c": 3}

amount = len(data.keys())
print("Number of keys:", amount)

#Comparing keys between two dictionaries    
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 10, "c": 20, "d": 30}

common_keys = dic1.keys() & dic2.keys()
print("Common keys:", common_keys)

#Get sorted keys
inventory = {"keyboards": 30, "mouse": 50, "monitors": 20}

ordered = sorted(inventory.keys())
print(ordered)

#Filter keys based on a condition
prices = {"bread": 1200, "milk": 900, "cheese": 5500, "eggs": 1500}

faces = [ke_y for ke_y in prices.keys() if prices[ke_y] > 1000]
print("expensive products:", faces)

#Create a new dictionary based only on keys
students = {"ana": 8, "juan": 7, "pepe": 9}

only_keys = {ke_y: "value not available" for ke_y in students.keys()}
print(only_keys)

#------------------------------values()------------------------------

#Show all dictionary values
person = {"name": "Juan", "age": 30, "city": "Córdoba"}

print(person.values())

#Convert the values ​​to a list
product = {"id": 101, "name": "Mouse", "price": 4500}

val_ues = list(product.values())
print(val_ues)

#Iterate through the values ​​with a loop
student = {"name": "Ana", "note": 9, "course": "Python"}

for val_ues in student.values():
    print("Value:", val_ues)
    
#Adding numerical values
tax_expenses = {"electricity taxes": 12000, "water": 8000, "internet": 6000}

total = sum(tax_expenses.values())
print("Total expenditure:", total)

#Count how many times a value appears
school_grades = {"ana": 10, "juan": 8, "pepe": 10, "luis": 7}

print("Number of times it appears: 10:", list(school_grades.values()).count(10))

#Check if a value exists
employee = {"name": "Luis", "position": "Sales"}

if "Sales" in employee.values():
    print("The value exists")
    
#Get unique values
colors = {"car": "red", "motorbike": "blue", "bicycle": "red"}

only = set(colors.values())
print(only)

#Filter keys based on values ​​(reverse lookup)
prices = {"bread": 1200, "milk": 900, "cheese": 5500, "eggs": 1500}

expensive_products = [product for product, price in prices.items() if price > 1000]
print("Expensive:", expensive_products)

#Create a dictionary sorted by values
qualifications = {"ana": 80, "juan": 50, "pepe": 90}

ordered = dict(sorted(qualifications.items(), key=lambda x: x[1]))
print(ordered)

#Add only the values ​​that meet a condition
sales = {"January": 20000, "February": 15000, "March": 30000, "April": 10000}

greater_than_2000 = [s for s in sales.values() if s > 20000]
print("Sales > 20000:", sum(greater_than_2000))

#------------------------------items()------------------------------

#Show all key-value pairs
person = {"name": "Juan", "age": 30, "city": "Córdoba"}

print(person.items())

#Traversing a dictionary with a loop
student = {"name": "Ana", "note": 9, "course": "Python"}

for ke_y, value in student.items():
    print(ke_y, "→", value)
    
#Convert items to a list of tuples
product = {"id": 101, "name": "Mouse", "price": 4500}

list_items = list(product.items())
print(list_items)

#Find a key based on its value
ages = {"ana": 20, "juan": 25, "pepe": 22}

for name, age in ages.items():
    if age == 25:
        print("The 25-year-old person is:", name)
        
#Create a new dictionary from another
prices = {"bread": 1200, "milk": 900, "cheese": 5500}

new = {product: price * 1.10 for product, price in prices.items()}
print(new)

#Filter a dictionary by values
sales = {"january": 20000, "february": 15000, "march": 30000, "april": 10000}

higher = {month: s for month, s in sales.items() if s > 15000}
print(higher)

#Find the maximum value and its key
qualifications = {"ana": 80, "juan": 50, "pepe": 90}

max_key, max_value = max(qualifications.items(), key=lambda x: x[1])

print("Máximum:", max_key, "with", max_value)

#Sort a dictionary by values
products = {"bread": 1200, "milk": 900, "cheese": 5500}

ordered = dict(sorted(products.items(), key=lambda x: x[1]))

print(ordered)

#Convert items into readable strings
person = {"name": "Sofía", "age": 25, "city": "Rosario"}

for ke_y, va_lue in person.items():
    print(f"{ke_y.upper()}: {va_lue}")
    
#Compare two dictionaries using items()
a = {"x": 1, "y": 2, "z": 3}
b = {"y": 2, "z": 5, "w": 0}

match = a.items() & b.items()

print("Same items:", match)

#------------------------------get()------------------------------

#Get an existing value
person = {"name": "Ana", "age": 25}

result = person.get("name")
print(result)

#Obtain a non-existent value without error
person = {"name": "Ana", "age": 25}

result = person.get("address")
print(result)

#Default cliente = {"nombre": "Lucas"}
customer = {"name": "Lucas"}

phone = customer.get("phone", "unregistered")
print(phone)

#Avoiding errors when data is missing
employee = {"name": "Laura", "position": "administrative"}

salary = employee.get("salary", 0)
print("Salary:", salary)

#get() with numbers (Get the grade for “mathematics”, or return -1 if it does not exist)
qualification = {"literature": 7, "history": 8}

qualification_mate = qualification.get("mathematics", -1)
print(qualification_mate)

#get() on optional data
product = {"id": 202, "name": "Keyboard", "price": 5000}

available = product.get("Available", "No data")
print(available)

#get() with nested dictionaries
user = {
    "name": "Mario",
    "address": {"city": "Rosario", "street": "Belgrano"}
}

city = user.get("address", {}).get("city", "Unknown")
print(city)

#Validate optional data
customer = {"name": "Paula", "phone": "12345678"}

email = customer.get("email", "Email not registered")
print(email)

#Check for existence without using “in”
user = {"name": "Roxana", "age": 40}

if user.get("premium") is None:
    print("Not a premium user")
else:
    print("He is a premium user")
    
#get() inside a loop
products = [
    {"name": "Mouse", "price": 5000},
    {"name": "Keyboard"},
    {"name": "Monitor", "price": 100000}
]

for p in products:
    print(p.get("name"), "-", p.get("price", "N/D"))    

#------------------------------update()------------------------------

#Add a new key to the dictionary
person = {"name": "Ana", "age": 25}

person.update({"city": "Córdoba"})
print(person)

#Update the value of an existing key
person = {"name": "Ana", "age": 25}

person.update({"age": 30})
print(person)

#Update multiple keys at once
person = {"name": "Laura", "age": 25}

person.update({"age": 28, "profession": "programmer"})
print(person)

#Merging two dictionaries
a = {"x": 1, "y": 2}
b = {"y": 100, "z": 3}

a.update(b)
print(a)

#Update with an empty dictionary
configuration = {"mode": "dark", "volume": 50}

configuration.update({})
print(configuration)

#Use update() with calculated values
player = {"name": "Leo", "qualification": 50}

player.update({"qualification": player["qualification"] + 10})
print(player)

#Update nested data (Change the "street" to "Belgrano 123" within a nested dictionary)
user = {
    "name": "Carlos",
    "address": {"city": "Rosario", "street": "San Juan 500"}
}

user["address"].update({"street": "Belgrano 123"})
print(user)

#Update a dictionary list (Use update() to increase the price of all products by 10%.)
products = [
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 7000}
]

for p in products:
    p.update({"price": p["price"] * 1.10})

print(products)

#Mini-project: Update user profile (Update incomplete user data)
users = [
    {"name": "Ana"},
    {"name": "Luis", "age": 30},
    {"name": "Marta", "country": "Chile"}
]

for u in users:
    u.update({"age": u.get("age", 0)})
    u.update({"country": u.get("country", "not specified")})

print(users)

#------------------------------pop()------------------------------

#Delete a key and get its value
person = {"name": "Ana", "age": 25}

removed_value = person.pop("age")

print("Removed Value:", removed_value)
print("Dictionary:", person)

#Delete a non-existent key with a default value
customer = {"name": "Lucas"}

result = customer.pop("phone", "not found")
print(result)
print(customer)

#Save the deleted value for later use
product = {"name": "Mouse", "price": 5000, "stock": 15}

stock = product.pop("stock")
print("Stock removed:", stock)

product.update({"available": stock > 0})
print(product)

#pop() with nested dictionaries
user = {
    "name": "Carlos",
    "address": {"city": "Rosario", "street": "Belgrano 500"}
}

removed_street = user["address"].pop("street")
print("Removed Street:", removed_street)
print(user)

#pop() in a loop
products = [
    {"name": "Keyboard", "price": 2000, "discount": 200},
    {"name": "Mouse", "price": 1000},
    {"name": "Monitor", "price": 80000, "discount": 5000}
]

for p in products:
    p.pop("discount", None)

print(products)

#pop() based on a condition (If a student scored less than 4 on an exam, drop the subject "history")
student = {"name": "Juan", "mathematics": 7, "history": 3}

if student["history"] < 4:
    removed = student.pop("history")
    print("Deleted note:", removed)

print(student)

#pop() to transfer data between dictionaries (Move the key "email" from one dictionary to another)
user = {"name": "Carlos", "email": "carlos@test.com"}
backup = {}

email = user.pop("email")
backup["email"] = email

print(user)
print(backup)

#Mini-project: Data cleaning. Leave only the name and price for each product (remove all other keys)
products = [
    {"name": "Mouse", "price": 5000, "color": "black", "stock": 15},
    {"name": "Keyboard", "price": 8000, "stock": 10, "type": "mecánico"},
]

for p in products:
    p.pop("color", None)
    p.pop("stock", None)
    p.pop("type", None)

print(products)

