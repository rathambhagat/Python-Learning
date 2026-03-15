# print("Meow")
# print("Meow")
# print("Meow")
# print("Meow")
# # if we wanna print multiple time we cant go traditional way

# i = 0
# while i <= 5:
#     print("Meow!, Meow!")
#     i = i + 1

# # Flowchart for above code:
# #
# #   [Start]
# #      |
# #   [i = 0]
# #      |                                
# #  [i <= 5 ?] ---- No ----> [End]       
# #      |                                
# #     Yes                               
# #      |                                
# # [print("Meow!, Meow!")]               
# #      |                                
# # [i = i + 1]                           
# #      |                                
# #      +-------------> (back to [i <= 5 ?]) 

# for i in [0,1,2]:
#     print("Meow")

# print("Meow\n"*3,end="")

# while True:
#     n = int(input("What's x?"))
#     if n < 0:
#         break
#     else:
#         continue

# while True:
#     n = int(input("What's n? "))
#     if n > 0 :
#         break
# for i in range(0,n):
#     print("Meow!")

# # List 
# student = ["P","R","T"]
# print(student[2])
# i = 1
# for i in student:
#     print(i)

# # Dict 
# Students = {
#     "Hermione":"gryffindor", #keys on the left and values on the right
#     "Ron":"gryffindor",
#     "Draco":"Slytherine"
# }
# # print(Students)
# # print(Students["Hermione"]) #in dict we can use actual name unlike list where we need index value 

# for student in Students:
#     # print(student) # it will print students keys only not values
#     print(student,Students[student]) #it will print students keys along with its values 

# Students = [
#     {"name":"Herminone","house":"gryffindor","patrouns":"oturs"},
#     {"name":"Harry","house":"gryffindor","patrouns":"stag"},
#     {"name":"Draco","house":"slytherine","patrouns":None}
# ]
# for students in Students:
#     print(students["name"],students["house"],students["patrouns"],sep = ", ")




