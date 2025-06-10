# Indexing = accessing element of a sequance using [] (indexing operator)
#                         z 

credit_num = "1234-5244-2347-0813"

print(credit_num[0]) # zero is the first number 
print(credit_num[0:3]) # first 3 numbers
print(credit_num[::2]) # second number of every step
print(credit_num[-1]) # last number

last_digits = credit_num[-4:] #Start 4 from the end, and go to the end of the string.
print(f"xxxx-xxxx-xxxx-{last_digits}") # will print only the last digits or credit card

letters = "abcdef"
print(letters[-4:]) # so it start backwards from (f) then end with (c) 


    #Quiz

    #here are a few quick questions:

#What does "hello"[1:4] return? ell ---> e is first and o is last but exluded

#What does "python"[-3:] return?  hon ---> Goes to the end of the string

#What does "abcdef"[::2] return?  ace ---> Takes every 2nd character starting from index 0

#What does "abcdef"[1::2] return?  bdf ---> Takes every 2nd character starting from index 1

#What does "abcdef"[:3] return?  abc ---> Starts from index 0 (default)

