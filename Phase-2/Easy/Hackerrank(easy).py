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

# Problem Statement 7
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

# Problem Statement 8
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

# Problem Statement 9
"""
You are given an integer,N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = alpha[i:size]
        row = "-".join(s[::-1] + s[1:])
        lines.append(row.center(4 * size - 3, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Problem Statement 10
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
"""
import os
def solve(s):
        words = s.split(" ")
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# Problem Statement 11
"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
"""
def student():
    records = []
    n = int(input())

    # Read all student records
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score]) # append function to add the name and score taken from user

    # Step 1: Find the lowest score
    lowest = float('inf') # setting the lowest variable to infinity cause every real score would be less than infinity This ensures that the first score we compare becomes the new lowest value. Think of it as Start with lowest = infinity. For each score, if it's less than the current lowest, update lowest.Since every real score is less than infinity, the first score will set the lowest correctly.
    for name, score in records: # loop to go through every score
        if score < lowest:
            lowest = score # storing the lowest score to variable lowest 
        # when the loops end we get the lowest score value stored in variable lowest
    # Step 2: Find the second lowest score
    second_lowest = float('inf')
    for name, score in records: # same as the upper one 
        if lowest < score < second_lowest:
            second_lowest = score
        # Initial value: We set second_lowest to infinity (float('inf')). This is like saying "I haven't found a candidate yet, so treat any real score as smaller than infinity." Loop through each student's score:The condition lowest < score ensures we only consider scores that are higher than the lowest score.The condition score < second_lowest checks whether this score is smaller than any candidate we have already found.If both conditions are true, we update second_lowest to this score.
    # Step 3: Collect names with the second lowest score
    names = []
    for name, score in records:
        if score == second_lowest:
            names.append(name)

    # Step 4: Sort names alphabetically and print
    names.sort()
    for name in names:
        print(name)


if __name__ == '__main__':
    student()

# Problem Statement 12
"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]          
    average = sum(marks) / len(marks)       
    print("{:.2f}".format(average))

# Problem Statement 13
"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        if op == "insert":
            i = int(cmd[1])
            e = int(cmd[2])
            lst.insert(i, e)
        elif op == "print":
            print(lst)
        elif op == "remove":
            e = int(cmd[1])
            lst.remove(e)
        elif op == "append":
            e = int(cmd[1])
            lst.append(e)
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()       

# Problem Statement 14
"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""
def swap_case(s):
    s.swapcase()
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Problem Statement 15 
"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Problem Statement 16
"""
You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.
"""
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Problem Statement 17
"""
Read a given string, change the character at a given index and then print the modified string.
"""
def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    return ''.join(lst)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Problem Statement 18
"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
"""
def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Problem Statement 19
"""
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# Problem Statement 20
"""
Complete the average function
"""
def average(array):
    distinct = set(array)
    avg = sum(distinct)/len(distinct)
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
