                                                #Example 1
age = int(input("Enter your age: "))

if age>= 100:
    print('Prepare your grave')

elif age >= 18:
    print("You are now signed up!")

elif age<= 0:
    print('u are not born yet!!')

else:
    print("You must be 18+ to sign up")

#we should give attention to the order of if statements so we cant add (elif age >= 100:) after if age>= 100:
 
                                                # Example 2

response = input('would u like some food (y/n):')

if response == 'y': #we use == to check 2 values are equal while = will assign the value 
    print('here u go')
else:
    print("no food for you")

                                                # Example 3

name = input('what is your name?')

if name == '':
    print('U didnt type anything')
else:
    print(f'hello {name}')

                                                # Example 4

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")

