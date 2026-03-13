#PHASE - 1

#FUNCTIONS AND VARIABLES

name = input("What's your name?")
print("Hello,", name)

name = input("What's your name?")
print(f"Hello,{name}")

name = input("What's your name?")
name = name.strip() #Remove white spaces from str 
print(f"Hello, {name}")

name = input("Whats your name?")
name = name.strip()
name = name.capitalize() #Capitalize the str
print(f"Hello, {name}")

name = input("Whats your name?")
name = name.strip()
name = name.title() #Capitalize based on title(capitalize every word)
name = name.strip().title() # alternative syntax
name = input("What's your name?").strip().title() # alternative syntax
print(f"Hello, {name}")

name = input("What's your name?").strip().title()
first, last = name.split(" ") #Split the str with spaces 
print(f"Hello, {first}")

#calculator.py
a = int(input("Enter your first number: ")) # integer input from user as if not used it will always take a str form even if it is number
b = int(input("Enter your second number: "))
print(f"The sum of {a} and {b} is: {a + b}") 

#floats 
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x+y) # print float value 
z = round(x+y)
print(z) # rounding floats
print(f"{z:,}") # giving it a standard comma 
z = round(x/y,2) # rounding to 2 points the dividing value
z = x/y
print(f"{z:.2f}") # f-string method to round integer

#Defining your own function
def hello():
	print("Hello!")
name = input("What's Your name? ")
hello()
print(name)

# passing a value so we can create a custom output
def hello(to):
	print("Hello!,", to)
name = input("What's your name? ")
hello(name)

# we called function before 
def hello(to = "world"):
	print("Hello!,", to)
hello()
name = input("What's Your name? ")
hello(name)

#calculator function
def main():
	x = int(input("What's is x? "))
	print("x squared is ",square(x))
def square(n):
	return n*n
	return pow(2,n) # alternative syntax
main()

