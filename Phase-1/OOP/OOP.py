# a basic program
name = input("What's Name?")
house = input("What's House? ")
print(f"{name} from {house}")

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
def get_name():
    name = input("What's Name?")
    return name
def get_house():
    house = input("What's house? ")
    return house

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
def get_name():
    return input("What's Name?")
def get_house():
    return input("What's house? ")
if __name__ == "__main__":
    main()

def main():
    name, house = get_student()
    print(f"{name} from {house}")
def get_student():
    name = input("What's Name?: ")
    house = input("What's House?: ")
    return (name,house) #tuple 
if __name__ == "__main__":
    main()

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "RavenClaw" #error shows tuple immutability 
    print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("What's Name?: ")
    house = input("What's House?: ")
    return (name,house) #tuple 
if __name__ == "__main__":
    main() 

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "RavenClaw" # list are muttable  
    print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("What's Name?: ")
    house = input("What's House?: ")
    return [name,house] #we used list instead of tuple 
if __name__ == "__main__":
    main() 

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "RavenClaw" # list are muttable  
    print(f"{student['name']} from {student['house']}")
def get_student():
    student = {}
    student["name"] = input("What's Name?")
    student["house"] = input("What's House?")
    return student #we used list instead of tuple 
if __name__ == "__main__":
    main() 

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "RavenClaw"  
    print(f"{student['name']} from {student['house']}")
def get_student():
    name = input("What's Name?")
    house = input("What's House?")
    return {"name":name, "house":house} 
if __name__ == "__main__":
    main() 

"""
What if there was a specific data type already created by 
python developers name student making our work easy but if devs of python
started to create data types based on what every program is going to write is 
not possible so for this they created CLASSES - Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
"""

class Student:
    ...
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    student = Student()
    student.name = input("What's name?: ")
    student.house = input("What's house?: ")
    return student
if __name__ == "__main__":
    main()

class Student:
    # Doc note: A class is a user-defined blueprint for creating objects with related data and behavior.
    ...
def main():
    student = get_student()
    # Doc note: Dot notation accesses object attributes (e.g., student.name, student.house).
    print(f"{student.name} from {student.house}")
def get_student():
    # Doc note: `Student()` creates an instance (object) of the Student class.
    student = Student()
    # Doc note: Instance attributes store per-object state and can be assigned dynamically.
    student.name = input("What's name?: ")
    student.house = input("What's house?: ")
    return student
if __name__ == "__main__":
    # Doc note: This guard runs `main()` only when this file is executed directly.
    main()
class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    name = input("What's Your name?: ")
    house = input("What's Your House?: ")
    student = Student(name,house)
    return student 
if __name__ == "__main__":
    main()

