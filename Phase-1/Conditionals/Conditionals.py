x = int(input("What's x? ")) #take value from the user
y = int(input("What's y? "))

if x > y : #if statement to check the condition
	print(f"{x} is greater than {y}")
if x < y : 
	print(f"{x} is less than {y}")
if x == y:
	print(f"{x} is equal to {y}")

# Flow Diagram (for the code above)
# Color Legend: 🔵 Start/Input | 🟨 Decision | 🟩 Output | 🟥 End
#
# 🔵 Start
#   |
#   v
# 🔵 Input x and y
#   |
#   v
# 🟨 Is x > y ? ---- Yes ----> 🟩 Print "x is greater than y"
#   | No
#   v
# 🟨 Is x < y ? ---- Yes ----> 🟩 Print "x is less than y"
#   | No
#   v
# 🟨 Is x == y ? --- Yes ----> 🟩 Print "x is equal to y"
#   |
#   v
# 🟥 End

x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y :
	print("x is greater than y")
elif x < y :
	print("x is less than y")
elif x == y :
	print("x is equal to y")

# Flowchart for the above code
#            +-------------------+
#            |     🔵 Start      |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |  🔵 Input x and y |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |    🟨 x > y ?      |
#            +-------------------+
#               | Yes       | No
#               v           v
#   +-------------------+   +-------------------+
#   | 🟩 print "x > y"   |   |    🟨 x < y ?      |
#   +-------------------+   +-------------------+
#               |             | Yes       | No
#               |             v           v
#               |   +-------------------+ +-------------------+
#               |   | 🟩 print "x < y"   | | 🟩 print "x == y" |
#               |   +-------------------+ +-------------------+
#               |             |             |
#               +-------------+-------------+
#                             |
#                             v
#                    +-------------------+
#                    |      🟥 End       |
#                    +-------------------+

x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y :
	print(f"{x} is greater than {y}")
elif x < y :
	print(f"{x} is greater than {y}")
else:
	print(f"{x} is equal to {y}")

# Flowchart for lines 72-80
#            +-------------------+
#            |     🔵 Start      |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |  🔵 Input x and y |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |    🟨 x > y ?      |
#            +-------------------+
#               | Yes       | No
#               v           v
#   +-------------------+   +-------------------+
#   | 🟩 print "x > y"   |   |    🟨 x < y ?      |
#   +-------------------+   +-------------------+
#               |             | Yes       | No
#               |             v           v
#               |   +-------------------+ +-------------------+
#               |   | 🟩 print "x < y"   | | 🟩 print "x == y" |
#               |   +-------------------+ +-------------------+
#               |             |             |
#               +-------------+-------------+
#                             |
#                             v
#                    +-------------------+
#                    |      🟥 End       |
#                    +-------------------+

x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y or x < y:
	print("x is not equal to y")
else:
	print("x is equal to y")

# Flowchart for above code
#            +-------------------+
#            |     🔵 Start      |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |  🔵 Input x and y |
#            +-------------------+
#                      |
#                      v
#            +---------------------------+
#            | 🟨 (x > y) OR (x < y) ?    |
#            +---------------------------+
#               | Yes               | No
#               v                   v
#   +---------------------------+   +-----------------------+
#   | 🟩 print "x is not equal to y"| | 🟩 print "x is equal to y"|
#   +---------------------------+   +-----------------------+
#               |                   |
#               +---------+---------+
#                         |
#                         v
#                +-------------------+
#                |      🟥 End       |
#                +-------------------+



x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
	print("x is not equal to y")
else:
	print("x is equal to y")

# Flowchart for above code
#            +-------------------+
#            |     🔵 Start      |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |  🔵 Input x and y |
#            +-------------------+
#                      |
#                      v
#            +-------------------+
#            |    🟨 x != y ?     |
#            +-------------------+
#               | Yes       | No
#               v           v
#   +---------------------------+   +-----------------------+
#   | 🟩 print "x is not equal to y"| | 🟩 print "x is equal to y"|
#   +---------------------------+   +-----------------------+
#               |             |
#               +------+------+ 
#                      |
#                      v
#             +-------------------+
#             |      🟥 End       |
#             +-------------------+

# grade 
score = int(input("Enter your score(0-100): "))
if 90 <= score <= 100: #alternative syntax
	print("Your Grade is A")
elif 80 <= score < 90: #alternative syntax
	print("Your Grade is B")
elif 70 <= score < 80: #alternative syntax
	print("Your Grade is C")
elif 60 <= score < 70: #alternative syntax
	print("Your Grade is D")
else:
	print("Your Grade is F")

# Flowchart for grade code
# Color Legend: 🔵 Start/Input | 🟨 Decision | 🟩 Output | 🟥 End
#
#            +----------------------+
#            |      🔵 Start        |
#            +----------------------+
#                      |
#                      v
#            +----------------------+
#            | 🔵 Input score 0-100 |
#            +----------------------+
#                      |
#                      v
#            +----------------------+
#            | 🟨 90 <= score <=100? |
#            +----------------------+
#               | Yes          | No
#               v              v
#   +----------------------+   +----------------------+
#   | 🟩 Print Grade A     |   | 🟨 80 <= score < 90? |
#   +----------------------+   +----------------------+
#               |                  | Yes          | No
#               |                  v              v
#               |      +----------------------+   +----------------------+
#               |      | 🟩 Print Grade B     |   | 🟨 70 <= score < 80? |
#               |      +----------------------+   +----------------------+
#               |                  |                  | Yes          | No
#               |                  |                  v              v
#               |                  |      +----------------------+   +----------------------+
#               |                  |      | 🟩 Print Grade C     |   | 🟨 60 <= score < 70? |
#               |                  |      +----------------------+   +----------------------+
#               |                  |                  | Yes          | No
#               |                  |                  v              v
#               |                  |      +----------------------+   +----------------------+
#               |                  |      | 🟩 Print Grade D     |   | 🟩 Print Grade F     |
#               |                  |      +----------------------+   +----------------------+
#               |                  |                  |                  |
#               +------------------+------------------+------------------+
#                                                     |
#                                                     v
#                                            +----------------------+
#                                            |       🟥 End         |
#                                            +----------------------+

# score = int(input("Enter your score(0-100): "))
if score >= 90:
	print("Your Grade is A")
elif score >= 80:
	print("Your Grade is B")
elif score >= 70:
	print("Your Grade is C")
elif score >= 60:
	print("Your Grade is D")
else:
	print("Your Grade is F")

# Flowchart for grade code using >=
# Color Legend: 🔵 Start/Input | 🟨 Decision | 🟩 Output | 🟥 End
#
#            +----------------------+
#            |      🔵 Start        |
#            +----------------------+
#                      |
#                      v
#            +----------------------+
#            | 🔵 Input score 0-100 |
#            +----------------------+
#                      |
#                      v
#            +----------------------+
#            |    🟨 score >= 90?    |
#            +----------------------+
#               | Yes          | No
#               v              v
#   +----------------------+   +----------------------+
#   | 🟩 Print Grade A     |   |    🟨 score >= 80?   |
#   +----------------------+   +----------------------+
#               |                  | Yes          | No
#               |                  v              v
#               |      +----------------------+   +----------------------+
#               |      | 🟩 Print Grade B     |   |    🟨 score >= 70?   |
#               |      +----------------------+   +----------------------+
#               |                  |                  | Yes          | No
#               |                  |                  v              v
#               |                  |      +----------------------+   +----------------------+
#               |                  |      | 🟩 Print Grade C     |   |    🟨 score >= 60?   |
#               |                  |      +----------------------+   +----------------------+
#               |                  |                  | Yes          | No
#               |                  |                  v              v
#               |                  |      +----------------------+   +----------------------+
#               |                  |      | 🟩 Print Grade D     |   | 🟩 Print Grade F     |
#               |                  |      +----------------------+   +----------------------+
#               |                  |                  |                  |
#               +------------------+------------------+------------------+
#                                                     |
#                                                     v
#                                            +----------------------+
#                                            |       🟥 End         |
#                                            +----------------------+

x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
	print("Odd")

def main():
	x = int(input("What's x? "))
	if x % 2 == 0:
		print("Even")
	else:
		print("Odd")

def is_even(n):
	return n % 2 == 0

main()