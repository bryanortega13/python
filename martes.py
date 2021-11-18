# Bryan Ortega

# Tuesday Nov. 16 

y= 6
x = [1,2]

# create list

print("---> Everything in my possesion")

inventory = ["bike","warm-up pants","car","lunch" ]

# print variables

print(y)
print(x)

print(inventory)
print(inventory[2])

# first loop

print("---> regular loop")

count = 0

while count < 4:
    print(inventory[count])
    count = count + 1

# second loop

print("--->Backwards loop")

count = 3

while count > 4:
    print(inventory[count])
    count = count - 1

# for loop

print("--->The inventory for loop")

for count in inventory :
    print (count)

    
