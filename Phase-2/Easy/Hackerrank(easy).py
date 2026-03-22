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
"""
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, a.
The second line contains the second integer, b.

"""
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# Problem Statement 4
"""
The provided code stub reads two integers, a and b,from STDIN.
Add logic to print two lines. The first line should contain the result of integer division, 
a//b . The second line should contain the result of float division, a/b .
No rounding or formatting is necessary.
"""
a = int(input())
b = int(input())
if b == 0 and a != 0:
    print("Cannot divide by zero")
elif b != 0 and a == 0:
    print(0)
    print(0)
else:
    print(a//b)
    print(a/b)
    
# Problem Statemnent 5
"""
The provided code stub reads an integer,n,from STDIN. For all non-negative integers i < n, print i².
"""
n = int(input())
if n>=1 and n<=20:
    i = 0
    while i<n :
        print(i*i)
        i = i + 1
else:
    print("Follow the constraints")

# Problem Statement 6
"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
"""
def is_leap(year):
    if year>=1900 and year <= 10**5:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False
    else:
        return False
year = int(input())
print(is_leap(year))

#Problem Statement 7
"""
The included code stub will read an integer,n,from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
"""
n = int(input())
if n >= 1 and n <= 150:
    i = 1
    for i in range(1, n + 1):
        print(i, end="")
else: 
    print("Follow the Constraints")

#Problem Statement 8
"""
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.
Here, 0 ≤ i ≤ x; 0 ≤ j ≤ y; 0 ≤ k ≤ z. Please use list comprehensions rather than multiple loops, as a learning exercise.
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
