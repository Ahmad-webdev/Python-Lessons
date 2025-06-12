# for loops = execute a block of code a fixed number of times.
#               You can iterate over a range, string, sequance, etc.


            #reverse Function 
for x in reversed(range(1,11)):
    print(x)
print('happy birthday')

for x in range(1 ,11 , 2): #<--- third value for steps used for skipping 
    print(x)

for x in range(1,21):
    if x == 13:
        continue #Used to skip a value (The number 13 is skipped in this example)
    print(x)

for x in range(1,10):
    if x== 5:
        break #Will stop after reaching number 4 and break the loop
    print(x)

