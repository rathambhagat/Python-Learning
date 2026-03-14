print("Meow")
print("Meow")
print("Meow")
print("Meow")
# if we wanna print multiple time we cant go traditional way

i = 0
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

for i in [0,1,2]:
    print("Meow")

print("Meow\n"*3,end="")

while True:
    n = int(input("What's x?"))
    if n < 0:
        break
    else:
        continue










