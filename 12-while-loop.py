# While loop= execute some code while some condition remain true 

name = input('what is your name: ')

                                                    # Example 1
while name == '':
    print('U didnt under your name')
    print('Please try again')
    name = input('what is your name: ') # we have to put some orders under the print or it will run forever

print(f"welcome : {name}")


                                                    # Example 2
age = int(input('How old are u? '))

while age <0 :
    print('تستهبل؟')
    age = int(input('How old are u?'))
    

print(f"your {age} years old")

                                                    # Example 3


food = str(input('what would u like to eat? (q to quit): '))

while not food == "q":

    print(f"{food} coming right up!!")
    food = str(input('what would u like to eat? (q to quit): '))
print('Bye 👋')

                                                    # Example 4

num = int(input('enter a number between 1 - 10 : '))

while num < 1 or num > 10 :
    print('Your number is not valid')
    num = int(input('enter a number between 1 - 10 : '))
print(f'Your Number is {num}')