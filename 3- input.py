# input is a function that prompt the user to enter data 
# Returns the enterned data as a string 

name = input('what is your name? ')

print(f"Hello {name}")

while True:
    age = int(input("How old are you? "))  # cast the input with int() Get user input and convert to integer

    if age >= 18:
        print("The door unlocks! You may enter. 🚪")
        break  # Exit the loop
    else:
        print("You're still too young! 🚫")
        break  # Exit the loopa

                                                       #exercise 
length = float(input('what is the length? '))
width = float(input('what is the width? '))

Area = length * width
print(f'the area is: {Area} cm')

                                                    #madlibs Game 

# Madlibs game
# word game where you create a story
# by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
