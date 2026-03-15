print("Meow")
print("Meow")
print("Meow")
print("Meow")
# if we wanna print multiple time we cant go traditional way

i = 0
# Doc note: A `while` loop keeps running while its condition stays True.
while i <= 5:
    print("Meow!, Meow!")
    i = i + 1

# Flowchart for above code:
#
#   [Start]
#      |
#   [i = 0]
#      |                                
#  [i <= 5 ?] ---- No ----> [End]       
#      |                                
#     Yes                               
#      |                                
# [print("Meow!, Meow!")]               
#      |                                
# [i = i + 1]                           
#      |                                
#      +-------------> (back to [i <= 5 ?]) 

# Doc note: A `for` loop iterates over items in an iterable sequence.
for i in [0,1,2]:
    print("Meow")

# Doc note: String repetition (`str * N`) repeats a string N times. `end=""` in print() replaces the default trailing newline with nothing.
print("Meow\n"*3,end="")

while True:
    n = int(input("What's x?"))
    # Doc note: `break` exits the nearest loop immediately.
    if n < 0:
        break
    else:
        # Doc note: `continue` skips remaining statements in this iteration.
        continue

while True:
    n = int(input("What's n? "))
    if n > 0 :
        break
# Doc note: `range(start, stop)` generates integers from start up to stop-1.
for i in range(0,n):
    print("Meow!")

# List 
# Doc note: A list is an ordered, mutable collection indexed from 0.
student = ["P","R","T"]
print(student[2])
i = 1
for i in student:
    print(i)

# Dict 
# Doc note: A dict maps unique keys to values for fast key-based lookup.
Students = {
    "Hermione":"gryffindor", #keys on the left and values on the right
    "Ron":"gryffindor",
    "Draco":"Slytherine"
}
# print(Students)
# print(Students["Hermione"]) #in dict we can use actual name unlike list where we need index value 

for student in Students:
    # print(student) # it will print students keys only not values
    print(student,Students[student]) #it will print students keys along with its values 

Students = [
    {"name":"Herminone","house":"gryffindor","patrouns":"oturs"},
    {"name":"Harry","house":"gryffindor","patrouns":"stag"},
    {"name":"Draco","house":"slytherine","patrouns":None}
]
for students in Students:
    print(students["name"],students["house"],students["patrouns"],sep = ", ")




