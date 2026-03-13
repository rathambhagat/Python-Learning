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