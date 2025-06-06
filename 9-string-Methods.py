name = input('Enter your full name: ')
phone_number = input('enter ur phone number : ')

                #Type the name Ali for example 

x= len(name) # lenght function to know lenght of a string (the spaces are also counted)

x= name.find(" ") # Method to find empty spaces (index start with 0 rather than 1)
x= name.rfind("i")  # same find but reverse
x= name.rfind("q")  # if the method could not find letter q will give -1

x= name.capitalize # well its obvious
x= name.upper #upper case
x= name.lower #lower case
x= name.isdigit #True only if there is digits which doesnt allow the user to type letters
x= name.isalpha #yes u got the idea


phone_number = phone_number.replace('-', " ")

print(x)
print(phone_number)

#ccprint(help(str)) # to know all the methods