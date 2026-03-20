# # a basic program
# name = input("What's Name?")
# house = input("What's House? ")
# print(f"{name} from {house}")

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
# def get_name():
#     name = input("What's Name?")
#     return name
# def get_house():
#     house = input("What's house? ")
#     return house

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
# def get_name():
#     return input("What's Name?")
# def get_house():
#     return input("What's house? ")
# if __name__ == "__main__":
#     main()


# class Student:
# 	# # Doc note: `__init__` is the constructor; it initializes each new object.
# 	def __init__(self,name,house):
# 		# # Doc note: Validation inside the class keeps object state consistent.
# 		if not name:
# 			raise ValueError("Missing Name!")
# 		self.name = name
# 		self.house = house


# def main():
# 	student = get_student()
# 	# # Doc note: Dot notation accesses instance attributes.
# 	print(f"{student.name} from {student.house}")


# def get_student():
# 	# # Doc note: Keep asking until valid input creates a Student object.
# 	while True:
# 		name = input("What's Your name?: ")
# 		house = input("What's Your House?: ")
# 		try:
# 			return Student(name,house)
# 		except ValueError as error:
# 			# # Doc note: `ValueError` indicates invalid constructor input.
# 			print(error)


# if __name__ == "__main__":
# 	# # Doc note: Entry-point guard runs `main()` only on direct execution.
# 	main()

# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")
# def get_student():
#     name = input("What's Name?: ")
#     house = input("What's House?: ")
#     return (name,house) #tuple 
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "RavenClaw" #error shows tuple immutability 
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("What's Name?: ")
#     house = input("What's House?: ")
#     return (name,house) #tuple 
# if __name__ == "__main__":
#     main() 

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "RavenClaw" # list are muttable  
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("What's Name?: ")
#     house = input("What's House?: ")
#     return [name,house] #we used list instead of tuple 
# if __name__ == "__main__":
#     main() 

# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "RavenClaw" # list are muttable  
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     student = {}
#     student["name"] = input("What's Name?")
#     student["house"] = input("What's House?")
#     return student #we used list instead of tuple 
# if __name__ == "__main__":
#     main() 

# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "RavenClaw"  
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     name = input("What's Name?")
#     house = input("What's House?")
#     return {"name":name, "house":house} 
# if __name__ == "__main__":
#     main() 

# """
# What if there was a specific data type already created by 
# python developers name student making our work easy but if devs of python
# started to create data types based on what every program is going to write is 
# not possible so for this they created CLASSES - Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
# """

# class Student:
#     ...
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     student = Student()
#     student.name = input("What's name?: ")
#     student.house = input("What's house?: ")
#     return student
# if __name__ == "__main__":
#     main()

# class Student:
#     # Doc note: A class is a user-defined blueprint for creating objects with related data and behavior.
#     ...
# def main():
#     student = get_student()
#     # Doc note: Dot notation accesses object attributes (e.g., student.name, student.house).
#     print(f"{student.name} from {student.house}")
# def get_student():
#     # Doc note: `Student()` creates an instance (object) of the Student class.
#     student = Student()
#     # Doc note: Instance attributes store per-object state and can be assigned dynamically.
#     student.name = input("What's name?: ")
#     student.house = input("What's house?: ")
#     return student
# if __name__ == "__main__":
#     # Doc note: This guard runs `main()` only when this file is executed directly.
#     main()

# class Student:
#     def __init__(self,name,house):
#         self.name = name
#         self.house = house
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("What's Your name?: ")
#     house = input("What's Your House?: ")
#     student = Student(name,house)
#     return student 
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("Missing Name!")
#         self.name = name
#         self.house = house
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("What's Your name?: ")
#     house = input("What's Your House?: ")
#     try:
#         return Student(name,house)
#     except ValueError:
#         # # Doc note: ValueError indicates invalid input; re-prompt the user.
#         pass
# if __name__ == "__main__":
#     main()

# class Students:
#     # # Doc note: Class variables (e.g., `class_year`, `num_students`) are shared by all instances.
#     class_year = 2024
#     num_students = 0
#     # # Doc note: `self` refers to the instance; `ClassName.variable` refers to the class.
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # # Doc note: Incrementing class variable tracks total instances created.
#         Students.num_students += 1


# # # Doc note: Each `Students(...)` call creates a new instance and increments the counter.
# student1 = Students("Pratham", 19)
# student2 = Students("Bhawan", 20)

# # # Doc note: Accessing class variables via `ClassName.attribute` (shared across all instances).
# print(Students.num_students)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} is eating! ")
#     def sleep(self):
#         print(f"{self.name} is sleeping! ")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass 
# class Mouse(Animal):
#     pass

# dog = Dog("sheru")
# cat = Cat("Persu")
# mouse = Mouse("Mickey")

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} is eating! ")
#     def sleep(self):
#         print(f"{self.name} is sleeping! ")
# class Dog(Animal):
#     def speak(self):
#         print("Bow!Bow!")
# class Cat(Animal):
#     def speak(self):
#         print("Meow!Meow!")
# class Mouse(Animal):
#     def speak(self):
#         print("cheese!cheese!")

# dog = Dog("sheru")
# cat = Cat("Persu")
# mouse = Mouse("Mickey")

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()
# mouse.speak()









