#used to make the code cleaner

friends= 2

# friends = friends + 1
friends += 1

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# friends = friends ** 2 #to the power
# friends **= 2

# remainder = friends % 2

print(f"you have {friends} friends")

x = 3.14
result = round(x) #Give the closest number and get rid of decimels 
print(result)

y = -4 
result = abs(y) #absoulte value
print(result)

result = pow(2, 3) #Power 
print(result)

result = max(x,y) 
print(result)
result = min(x,y) 
print(result)

import math #bring the math properties 

x= 9 

print(math.pi)
print(math.e)
print(math.sqrt(x))

math.ceil #round a number UP so 9.1 = 10
math.floor #round a number DOWN so 9.9 = 9

import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius #to calculate radius

print(f"The circumference is: {round(circumference, 2)}")


