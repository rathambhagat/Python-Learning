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
    # Problem Statement 21
"""
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Input Format:
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
Output the total number of distinct country stamps on a single line.
"""
n = int(input())
Stamps = set()
for i in range(n):
    Stamps.add(input())
print(len(Stamps))
    
# Problem Statement 22
"""
Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
Input Format
The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next V lines contains either pop, remove and/or discard commands followed by their associated value.
"""
if __name__ == '__main__':
    n = int(input())                          # number of elements in the set
    s = set(map(int, input().split()))        # read the set
    N = int(input())                          # number of commands
    for _ in range(N):
        command = input().split()
        if command[0] == 'pop':
            s.pop()                           # removes an arbitrary element
        elif command[0] == 'remove':
            s.remove(int(command[1]))         # removes the specified element; raises error if not present
        elif command[0] == 'discard':
            s.discard(int(command[1]))        # removes if present, does nothing otherwise
    print(sum(s))                             # output the sum of the remaining elements

# Problem Statement 23
"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
Input Format
The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
"""
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
s = len(english.union(french))
print(s)

# Problem Statement 24
"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to both the newspapers.
Input Format
The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
"""
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
print(len(english.intersection(french)))

# Problem Statement 25
"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to the english newspaper.
Input Format
The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
"""
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
print(len(english.difference(french)))

# Problem Statement 25
"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both..
Input Format
The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
"""
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
print(len(english.symmetric_difference(french)))
# Problem Statement 26
"""
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.
Output Format
Output the symmetric difference integers in ascending order, one per line.
"""
n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = set(map(int, input().split()))

# Symmetric difference: (N | M) - (N & M)
symmetric_diff = N.symmetric_difference(M)

# Print each element in ascending order, one per line
for value in sorted(symmetric_diff):
    print(value)

# Problem Statement 27
"""
TASK
You are given a set A and N number of other sets. These N number of sets have to
perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
Input Format
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2 * N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and
the length of the other set.
The second line of each part contains space separated list of elements in the other set.
0 < len(set(A)) < 1000
0 < len(otherSets) < 100
0 < N < 100
Output Format
Output the sum of elements in set A.
"""
if __name__ == '__main__':
    # Read the number of elements in A (not used directly)
    n = int(input())
    # Read set A
    A = set(map(int, input().split()))
    # Read number of operations
    N = int(input())

    for _ in range(N):
        # Read operation line: e.g., "update 5"
        op_line = input().split()
        operation = op_line[0]       # e.g., 'update'
        # The next line contains the other set elements
        other_set = set(map(int, input().split()))
        
        # Perform the appropriate mutation
        if operation == 'update':
            A.update(other_set)
        elif operation == 'intersection_update':
            A.intersection_update(other_set)
        elif operation == 'difference_update':
            A.difference_update(other_set)
        elif operation == 'symmetric_difference_update':
            A.symmetric_difference_update(other_set)
    
    # Output the sum of the remaining elements in A
    print(sum(A))

# Problem Statement 28
"""
Task
You are given a complex z. Your task is to convert it to polar coordinates.
Input Format
A single line containing the complex number z. Note: complex() function can be used in
python to convert the input as a complex number.
Constraints
Given number is a valid complex number
Output Format
Output two lines:
The first line should contain the value of r.
The second line should contain the value of .
"""
import cmath
z = complex(input())
r, phi = cmath.polar(z)
print(r)
print(phi)

# Problem Statement 29
"""
Task
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b (While using Python2 remember to import
division from __future__).
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.
Input Format
The first line contains the first integer, a, and the second line contains the second integer, b.
Output Format
Print the result as described above.
"""
a = int(input())
b = int(input())
res = divmod(a,b)
print(res[0])
print(res[1])
print(res)

# Problem Statement 30
"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
Input Format
The first line contains a, the second line contains b, and the third line contains m.
"""
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))

# Problem Statement 31
"""
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 231-1 (c++ int) or 263 1 (C++ long long int).
b As we know, the result of a grows really fast with increasing b.
Let's do some calculations on very large integers.
Task
Read four numbers, a, b, c, and d, and print the result of ab + c².
Input Format
Integers a, b, c, and d are given on four separate lines, respectively.
Constraints
1 ≤ a ≤ 1000
1 < b < 1000
1 ≤ c ≤ 1000
1 ≤ d ≤ 1000
Output Format
Print the result of ab + cd on one line.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

# Problem Statement 32
"""
Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x; amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and 2, the price of the shoe.
Constraints
0 < X < 103
0 < N < 103
20 < x < 100
2 < shoe size < 20
Output Format
Print the amount of money earned by Raghu.
"""
from collections import Counter

if __name__ == '__main__':
    # Read number of shoes
    X = int(input().strip())
    # Read shoe sizes
    shoe_sizes = list(map(int, input().strip().split()))
    # Count available shoes per size
    stock = Counter(shoe_sizes)
    
    # Read number of customers
    N = int(input().strip())
    total_earned = 0
    
    # Process each customer
    for _ in range(N):
        size, price = map(int, input().strip().split())
        if stock[size] > 0:
            total_earned += price
            stock[size] -= 1
    
    print(total_earned)

# Problem Statement 33
"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
Example
Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.
Expected output:
13
-1
Input Format
The first line contains integers, n and m separated by a space.
The next n. lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
Constraints
1 ≤ n ≤10000
1 ≤ m ≤ 100
1 length of each word in the input < 100
Output Format
Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
"""
# Read the first line containing n and m
n, m = map(int, input().split())

# Create a dictionary to store positions for each word in group A
positions = {}

# Read the next n lines for group A
for i in range(1, n + 1):          # i starts at 1 for 1-indexed positions
    word = input().strip()         # read the word, strip any extra whitespace
    if word not in positions:
        positions[word] = []       # initialize an empty list for new word
    positions[word].append(str(i)) # store the index as a string for later joining

# Process the m words of group B
for _ in range(m):
    word = input().strip()         # read a word from group B
    if word in positions:
        # Print the indices separated by spaces
        print(" ".join(positions[word]))
    else:
        print(-1)

# Problem Statement 34
"""
Task
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
Average score Sum of scores obtained in all subjects by a student Total number of subjects
Input Format
The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.
Constraints
0 < N < 100
0 < X < 100
Output Format
Print the averages of all students on separate lines.
The averages must be correct up to 1 decimal place.
"""
# Read number of students and subjects
N, X = map(int, input().split())

# Create a list to store marks per student (initialize with zeros)
student_marks = [0] * N

# Read marks for each subject
for _ in range(X):
    marks = list(map(float, input().split()))
    for i in range(N):
        student_marks[i] += marks[i]

# Compute averages and print each with one decimal place
for total in student_marks:
    average = total / X
    print(f"{average:.1f}")

# Problem Statement 35
"""
Task
You are given a date. Your task is to find what the day is on that date.
Input Format
A single line of input containing the space separated month, day and year, respectively, in  MM DD YYYY format.
Output Format
Output the correct day in capital letters.
"""
import calendar
M, D, Y = map(int,input().split())
# Get the weekday (0 = Monday, 6 = Sunday)
weekday = calendar.weekday(Y,M,D)

# Get the day name in uppercase
print(calendar.day_name[weekday].upper())

# Problem Statement 36
"""
Task
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of z and k. Your task is to verify if P(x) = k.
Constraints
All coefficients of polynomial P are integers.
x and y are also integers.
Input Format
The first line contains the space separated values of x and k.
The second line contains the polynomial P.
Output Format
Print True if P(x) = k. Otherwise, print False.
"""
# Read x and k
x, k = map(int, input().split())

# Read the polynomial expression
expr = input()

# Evaluate the expression with x replaced by its value
result = eval(expr, {"x": x})

# Print True if result equals k, otherwise False
print(result == k)

# Problem Statement 37
"""
Task
You are given two values a and b.
Perform integer division and print a/b.
Input Format
The first line contains T. the number of test cases.
The next T lines each contain the space separated values of a and b.
Constraints
0 <T<10
Output Format
Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.
"""
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    line = input().strip()
    try:
        a, b = map(int, line.split())
        print(a // b)  # integer division
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

# Problem Statement 38
"""
Task
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
Input Format
A single line containing the thickness value for the logo.
Constraints
The thickness must be an odd number.
Output Format
Output the desired logo.
Sample Input
5
Sample Output
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""
thickness = int(input()) # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Problem Statement 39
"""
Input Format
A single line containing the space separated values of  and .
Output Format
Output the design pattern.
Sample Input
9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
---------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
# N is height, M is width
N, M = map(int, input().split())

# Top Section
for i in range(1, N, 2):
    pattern = (".|." * i)
    print(pattern.center(M, '-'))

# Middle "WELCOME" Section
print("WELCOME".center(M, '-'))

# Bottom Section (Reverse of Top)
for i in range(N-2, -1, -2):
    pattern = (".|." * i)
    print(pattern.center(M, '-'))

# Problem Statement 40
"""
You are given a string and width.
Your task is to wrap the string S into a paragraph of width w.
Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to
Returns
string: a single string with newline characters ('\n') where the breaks should be
Input Format
The first line contains a string, String.
The second line contains the width, Width.
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ4
Sample Output 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
"""
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Problem Statement 41
"""
Task
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Average Sum of all marks Total Students
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
Input Format
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class, under their respective column names.
Constraints
0 < N < 100
Output Format
Print the average marks of the list corrected to 2 decimal places.
"""
n = int(input())
columns = input().split()
marks_index = columns.index('MARKS')
total_marks = 0
for _ in range(n):
    data = input().split()
    total_marks += int(data[marks_index])
average = total_marks / n
print(f"{average:.2f}")

# Problem Statement 42
"""

"""