#------------------------------lower()------------------------------

#Convert a word to lowercase
word = "Python"
print(word.lower())

#Convert a phrase entered by the user
#phrase = input("Write a sentence: ")
#print(phrase.lower())

#Save lowercase words within a list
words = ["Hello", "World", "PYTHON"]
result = []

for palabra in words:
    result.append(palabra.lower())

print(result)

#Compare two words regardless of case
word1 = "Casa"
word2 = "casa"

if word1.lower() == word2.lower():
    print("Are the same")
else:
    print("Are different")
    
#Count how many times a word appears regardless of case
text = "Python is great. I love Python and learning Python."
text= text.lower()

print("The word 'python' appears:", text.count("python"), "times.")   

#Filter words that begin with a letter, regardless of the case
words = ["Car", "plane", "apple", "Ship", "Friend", "bicycle", "Art", "Age"]
with_a = []

for word in words:
    if word.lower().startswith("a"):
        with_a.append(word)

print(with_a) 

#Normalize usernames
user = ["Juan", "MARIA", "peDro", "LuIS"]
normalize_usernames = []

for u in user:
    normalize_usernames.append(u.lower())

print(normalize_usernames)

#Check if a letter is in a word (regardless of capitalization)
word = "Programming"
letter = "P"

if letter.lower() in word.lower():
    print("The letter is in the word.")
else:
    print("The letter is not in the word.")
    
#Count how many words contain a given letter (ignoring case)
words = ["Sun", "Chair", "Home", "River", "Path"]
letter = "s"
counter = 0

for w in words:
    if letter.lower() in w.lower():
        counter += 1
print("Number of words with the letter 's':", counter)
    
#Remove duplicates from a list of words ignoring case
words = ["Home", "home", "HOME", "Dog", "DOG", "cat"]
unique_words = []

for word in words:
    if word.lower() not in [w.lower() for w in unique_words]:
        unique_words.append(word)

print(unique_words)

#------------------------------upper()------------------------------

#Convert a word to uppercase
#word = input("Write a word: ")
#print(word.upper())

#Display fixed uppercase text
text = "Python is great"
print(text.upper())

#Ask for the user's name and display it in capital letters
#name = input("Your name: ")
#print("Your name in capital letters is:", name.upper())

#Convert each word in a list to uppercase
words = ["hello", "people", "python"]

cap = [w.upper() for w in words]
print(cap)

#Count how many capital letters a text has
#text = input("Write a text: ")
#cap = sum(1 for letter in text if letter.isupper())
#print("Number of capital letters:", cap)

#Compare texts regardless of case
#word1 = input("first word: ")
#word2 = input("Second word: ")

#if word1.upper() == word2.upper():
#    print("Are the same (ignoring upper/lower case)")
#else:
#    print("Are different")

#Detect keywords in a text regardless of the case
#text = input("Write a sentence: ")
#key = "PYTHON"

#if key in text.upper():
#    print("¡The sentence contains the word PYTHON!")
#else:
#    print("The word PYTHON was not found.")

#Capitalize only words that begin with a vowel
text = "Hello, this is an example with Python."

words = text.split()
result = [w.upper() if w[0].lower() in "aeiou" else w for w in words]
print(" ".join(result))

#Create a function that returns text that is all in uppercase
def convert_to_uppercase(text):
    return text.upper()

print(convert_to_uppercase("This text is in lowercase"))

#------------------------------strip()------------------------------

#Remove spaces at the beginning and end
text = "   Hello world   "
print(text.strip())

#Delete specific characters
text = "---Python---"
print(text.strip('-'))

#Clean up text with spaces and line breaks
text = "\n\t Hello world \n"
print(text.strip())

#Clear data entered by the user
name = input("Enter your name: ").strip()
print(f"Hello {name}!")

#Remove multiple types of characters
text = "///hello world***"
print(text.strip("/*"))

#Clean a list of texts
words = ["  dog ", " cat ", " mouse  "]

clean = [w.strip() for w in words]
print(clean)

#Compare texts without spaces
a = "  hello".strip()
b = "hello  ".strip()

print(a == b)

#------------------------------split()------------------------------

#Separating words in a sentence
text = "Hello, how are you today"

words = text.split()
print(words)

#Count how many words are in a sentence
#phrase = input("Write a sentence: ")
#amount = len(phrase.split())

#print("Number of words:", amount)

#Separate a list of user-entered items
#data = input("Enter names separated by commas: ")
#names = data.split(',')

#print(names)

#Clean the spaces when separating
text = "Juan, Ana , Luis , Pedro"

names = [n.strip() for n in text.split(',')]
print(names)

#Separate a date into parts
date = "2025-10-27"

year, month, day = date.split('-')
print("Year:", year, "Month:", month, "Day:", day)

#Separating values ​​from a CSV file
line = "Carlos,32,Argentina"

name, age, country = line.split(',')
print(name, age, country)

#Get the extension of a file
archive = "foto_perfil.jpg"  

name, extension = archive.split('.') 
print("Extensión:", extension)

#Separate an email address
email = "usuario@gmail.com"

user, domain = email.split('@')
print("User:", user)
print("Domain:", domain)

#Take only the name of a complete route
route = "C:/Usuarios/Exequiel/Documentos/archivo.txt"

parts = route.split('/')
print("file name:", parts[-1])

#Divide text with a limit of separations
text = "uno-dos-tres-cuatro"     

parts = text.split('-', 2)
print(parts)

#------------------------------join()------------------------------

#Combine a list of words into a sentence
words = ["Hello", "World", "Python"]

phrase = " ".join(words)
print(phrase)

#Create a comma-separated list
names = ["Juan", "Ana", "Pedro"]

result = ", ".join(names)
print(result)

#Format a list before saving it to a file
data = ["Carlos", "32", "Argentina"] 

line = ";".join(data)  
print(line)

#Create a string with line breaks
lines = ["Primera línea", "Segunda línea", "Tercera línea"]

text = "\n".join(lines)
print(text)
 
#Show numbered data
numbers = ["1", "2", "3", "4"]

string = " - ".join(numbers)
print("Numbers:", string)

#Join characters into a word
letters = ['P', 'y', 't', 'h', 'o', 'n']

word = ''.join(letters)
print(word)  

#Create a line to export user data
user = ["Exequiel", "Carcamo", "Argentina"]

record = ",".join(user)
print(record)

#Combine processed results
words= ["hello", "python", "join"]

cap = [w.upper() for w in words]
result = " | ".join(cap)
print(result)

#Join lines read from a file
# Suponé que leíste un archivo línea por línea:
lines = ["dato1\n", "dato2\n", "dato3\n"]

text = "".join(lines)
print(text)

#Create dynamically formatted text
words = ["Training", "in", "home"]

message = "💪 ".join(words)
print(message)

#------------------------------replace()------------------------------

#Replace a word in a sentence
phrase = "Python is hard"

new_phrase = phrase.replace("hard", "easy")
print(new_phrase)

#Correct typos
text = "Welcom@ to th@ Python cours@"

clean = text.replace("@", "e")
print(clean)

#Remove unwanted characters
text = "Hello!!! ¿How are you???"

without_signs = text.replace("!", "").replace("?", "")
print(without_signs)

#Change separators
data = "name;age;country"

new_data = data.replace(";", ",")
print(new_data)

#Censor words
message = "This product is rubbish"

filtered = message.replace("rubbish", "**")
print(filtered)

#Format numbers
price = "1.500,50"

new = price.replace(".", "").replace(",", ".")
print(new)

#Clear copied text
text = " \tHello World\n"

clean = text.replace("\n", "").replace("\t", "").strip()
print(clean)

#Replace multiple words in a string
phrase = "I like Java and PHP"

phrase = phrase.replace("Java", "Python").replace("PHP", "JavaScript")
print(phrase)

#Normalize uppercase/lowercase and correct text
text = "wELCOME TO THE Python cOURSE"

text = text.lower().replace("python", "Python").capitalize()
print(text)

#Replace spaces with hyphens or underscores
file_name = "monthly sales report"

new_name = file_name.replace(" ", "_")
print(new_name)

#------------------------------find()------------------------------

#Find a word in a sentence
phrase = "I'm learning Python and I really like it"
p = phrase.find("Python")

if p != -1:
    print(f"The word 'Python' appears in the position {p}")
else:
    print("The word 'Python' is not in the sentence.")
    
#Check if an email contains “@”
#mail = input("enter your email: ")

#if mail.find("@") != -1:
#    print("Valid email ✅")
#else:
#    print("Invalid email ❌")

#Search for a file extension
file = "final_report.xlsx"

if file.find(".xlsx") != -1:
    print("It's an Excel file")
else:
    print("It's not an Excel file.")
    
#Search for multiple occurrences in text
text = "Python is powerful. I like Python. Python is great.."

pos = text.find("Python")
while p != -1:
    print("Found in position:", p)
    p = text.find("Python", p + 1)
    
#Extract text after a word
message = "User: Exequiel - Role: Administrative"

start = message.find("Role:") + len("Role:")
role = message[start:].strip()
print("user role", role)

#Find out if a phone number has a country code
phone = "+54 9 11 2345 6789"

if phone.find("+54") == 0:
    print("Argentine phone number 🇦🇷")
else:
    print("another country 🌍")    
    
#Analyze whether a text mentions a forbidden word
message = "This product is rubbish"
prohibited = "rubbish"

if message.lower().find(prohibited) != -1:
    print("⚠️ Inappropriate language detected")    
    
#Check if a URL contains HTTPS
url = "http://misitio.com"

if url.find("https://") != -1:
    print("Secure connection 🔒")
else:
    print("Insecure connection ⚠️")  
    
#Search for a word within imported text
text = "Name: Ana | Age: 32 | City: Mendoza"

p = text.find("Age:")

if p != -1:
    Age = text[p + 5 : p + 7].strip()
    print("Age:", Age)      
    
#Search for keywords in a record
record = "2025-10-27 | ERROR | Archivo no encontrado"

if record.find("ERROR") != -1:
    print("⚠️ An error was detected in the record.")
    
#------------------------------index()------------------------------

#Find the position of a word
phrase = "I'm learning Python"

p = phrase.index("Python")
print("The word 'Python' begins at the index:", p)   

#Search for a specific letter
text = "program"
print("First 'r' in the position:", text.index("r"))

#Search from a specific position
text = "Python is fun and Python is useful"

p = text.index("Python", 10)
print("Second appearance of 'Python' in:", p)

#Avoiding errors with conditional statements
phrase = "Learning to program is fun"

if "Python" in phrase:
    p = phrase.index("Python")
    print("Found in position:", p)
else:
    print("The word 'Python' is not in the sentence.")
    
#Search and extract text from a word
message = "User: Exequiel | Role: administrator"

start = message.index("Role:") + len("Role:")
role = message[start:].strip()
print("user role:", role)

#Find file extension
file = "profile_photo.png"

point = file.index(".")
extension = file[point+1:]
print("Extensión:", extension)

#Find a delimiter in a list of data
data = "name;age;city;country"

in_dex = data.index(";")
print("The first semicolon is in position:", in_dex)

#Find the position of a repeated word
text = "Python, Java, C++, Python, JavaScript"

first = text.index("Python")
second = text.index("Python", first + 1)
print("first position:", first)
print("second position:", second)

#Find the first comma and break the string
phrase = "Apple, Orange, Banana"

coma = phrase.index(",")
first_word = phrase[:coma]
print("First word:", first_word)

#Search within formatted text
record = "ID: 245 | Name: Juan | Age: 31"

p = record.index("Name:") + len("Name:")
name = record[p : record.index("|", p)].strip()
print("Name:", name)
    
#------------------------------startswith()------------------------------   

#Check if a text begins with a specific word
message = "Python is a great technology"

if message.startswith("Python"):
    print("✅ The text begins with 'Python'")
else:
    print("❌ It doesn't start with 'Python'")
    
#Filter files by name or prefix
files = ["data_january.csv", "data_february.csv", "summary.txt", "data_march.csv"]

for file in files:
    if file.startswith("data_"):
        print("Data file:", file) 
        
#Validate secure URLs (HTTPS)
url = "https://miweb.com"

if url.startswith("https://"):
    print("🔒 Secure connection")
else:
    print("⚠️ It's not a secure connection.")
    
#Detect country codes in phone numbers
telephone_number = "+54 9 11 2345 6789"

if telephone_number.startswith("+54"):
    print("📞 This phone number belongs to Argentina")
elif telephone_number.startswith("+55"):
    print("📞 This phone number belongs to Brazil")
else:
    print("🌍 Another country")       
    
#Validate usernames or codes
code = "USR_1023"

if code.startswith("USR_"):
    print("User code detected")
else:
    print("Invalid code")       
    
#Check if an email starts with a name
mail = "admin@empresa.com"

if mail.startswith("admin"):
    print("📧 Administrator email") 
    
#Check several possible words at the beginning
log = "ERROR: lost connection"

if log.startswith(("ERROR", "WARNING", "FAILURE")):
    print("⚠️ Important record detected")    

#Using startswith() with indices (start and end) Buscar si hay un '1' a partir del cuarto carácter
texto = "00012345"

if texto.startswith("1", 3):
    print("The text has a 1 starting from position 3")
    
#Clean and validate text before using startswith()
name = "   Exequiel  ".strip()

if name.startswith("E"):
    print("The name begins with E")
    
#Filter a list based on specific prefixes
files = ["report_2025.pdf", "summary_2024.docx", "data_2025.csv", "pic.png"]

filtered = [f for f in files if a.startswith(("report_", "data_"))]
print("Leaked files:", filtered)   

#Check if a path belongs to a certain folder
route = "C:/Projects/Python/mi_script.py"

if route.startswith("C:/Proyectos/Python/"):
    print("📂 File inside the Python folder") 
    
#Validate if a log line with begins a date
line = "2025-10-27 | INFO | Process completed"

if line.startswith(("2025", "2024", "2023")):
    print("✅ Record with valid date format")    
    
#Validate the format of a label or command
command = "CMD_START"

if command.startswith("CMD_"):
    print("🟢 Recognized command:", command)    
    
#Identify messages of a specific type
messages = [
    "INFO: Everything works fine",
    "ERROR: Could not connect",
    "WARNING: Low memory",
]

errors = [m for m in messages if m.startswith("ERROR")]
print("Error messages:", errors)   

#Detect if a document is of a known type
document = "invoice_2025.pdf"

if document.startswith(("invoice_", "receipt_", "report_")):
    print("📄 Accounting document detected") 
    
#------------------------------endswith()------------------------------    

#Check the extension of a file
file = "reporte_2025.pdf"

if file.endswith(".pdf"):
    print("📄 It is a PDF file")
else:
    print("❌ It is not a PDF file")
    
#Validate images by extension
images = ["pic1.jpg", "icon.png", "banner.gif", "document.pdf"]

for img in images:
    if img.endswith((".jpg", ".png", ".gif")):
        print("🖼️ Valid image:", img)    
        
#Verify emails by domain
mail = "customer@gmail.com"

if mail.endswith("@gmail.com"):
    print("📧 Gmail mail")
else:
    print("📨 Other provider")    
    
#Check if a URL ends in a specific route
url = "https://miweb.com/contacto"

if url.endswith("/contact"):
    print("🔗 Contact page detected")    
    
#Validate backup names
file = "database_backup_2025.bak"

if file.endswith("_backup_2025.bak"):
    print("💾 Recognized backup file")       
    
#Filter for text files only
files = ["data.csv", "reporte.txt", "script.py", "document.txt"]

texts = [f for f in files if f.endswith(".txt")]
print("📂 Text files:", texts)

#Validate log records
line = "2025-10-27 | ERROR | File not found"

if line.endswith("not found"):
    print("⚠️ File error detected")
    
#Check if a string ends with a number
code = "USR1024"

if code.endswith("1024"):
    print("🆔 Code ending in 1024") 
    
#Using endswith() with index range
text = "12345_ABC"
print(text.endswith("45", 0, 5))    # Verifica solo la parte "12345"

#Validate if a path ends in a folder
rute = "C:/Usuarios/Exequiel/Documentos"

if rute.endswith("/Documents") or rute.endswith("\\Documents"):
    print("📁 Document path detected")   
    
#Detect file format before opening it
files = "data.xlsx"

if files.endswith((".csv", ".xlsx", ".xls")):
    print("📊 Supported file")      
    
#Validate URLs that end with specific parameters
url = "https://api.servicio.com/consulta?tipo=json"

if url.endswith("json"):
    print("🧩 Response in JSON format") 
    
#Detect specific versions or suffixes
software = "app_v2.3"

if software.endswith(("v2.3", "v2.4")):
    print("🧠 Supported version")     
    
#Validate report names
report = "october_monthly_sales_2025.csv"

if report.endswith("_2025.csv"):
    print("📈 Report for the year 2025 detected")      
    
#Check if a message ends with an emoji or symbol
message = "Thanks for your help 🙏"

if message.endswith(("🙏", "😊", "!")):
    print("💬 Positive message detected")

     
        