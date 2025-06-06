# logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)


# or example
temp = 25
if temp > 30 or temp < 10:
    print("Extreme temperature")
else:
    print("Temperature is moderate")

# and example
age = 20
has_ID = True
if age >= 18 and has_ID:
    print("Access granted")
else:
    print("Access denied")

# not example
is_raining = False
if not is_raining:
    print("Go outside")
else:
    print("Stay inside")
