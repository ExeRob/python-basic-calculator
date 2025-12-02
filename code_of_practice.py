#creating a function that generates a random password:
def create_random_password(numb):
    chars = "abcdhijk"
    whole_number = str(numb)
    numb = int(whole_number[0])
    c1 = numb - 2
    c2 = numb
    c3 = numb - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{numb*2}" 
    return password

passw = create_random_password(23) 
phrase = f"your new password is: {passw}"
print(phrase)

#creating a function that adds two numbers (a + b):
def summation(a,b):
    return a + b

result = summation(25,80)
print(result)

#creating a function that name, last name and adjective:
def phrase(name,last_name,adjective):
    return f"Hello {name} {last_name} you are very {adjective}"

resulting_phrase = phrase("exe","Carcamo","intelligent")
print(resulting_phrase)

#creating a function that name, last name and adjective:
def phrase(name,last_name,adjective):
    return f"Hello {name} {last_name} you are very {adjective}"

resulting_phrase = phrase("exe","Carcamo","intelligent")
print(resulting_phrase)

#creating a function that name, last name and adjective:
def phrase(name,last_name,adjective):
    return f"Hello {name} {last_name} you are very {adjective}"

resulting_phrase = phrase("exe","Carcamo","intelligent")
print(resulting_phrase)

#creating a function that name, last name and adjective:
def phrase(name,last_name,adjective):
    return f"Hello {name} {last_name} you are very {adjective}"

resulting_phrase = phrase("exe","Carcamo","intelligent")
print(resulting_phrase)
