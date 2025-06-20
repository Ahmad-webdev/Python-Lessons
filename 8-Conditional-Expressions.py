#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
                            #  Print or assign one of two values based on a condition
                            # X if condition else Y

num = 5
a = 6
b = 7
age = 13

print("Positive" if num > 0 else "Negative") 
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"

print(result)
print(max_num)
print(min_num)
print(status)