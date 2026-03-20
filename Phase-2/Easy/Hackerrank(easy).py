# In this File we have solved all the easy problems from the hackerrank along with the question, Algorithm and explanation 

# Problem 1: Print "Hello, World!"
print("Hello, World!")

# Problem 2: 
"""
Task
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""
n = int(input())
if n < 1 or n > 100:
    print("Please enter a number between 1 and 100.")
else:
    if n % 2 == 1:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# Problem Statemnt 3:

