# format specifiers = {value:flags} format a value based on what
# flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 12.99
price2 = 135.5015155
price3 = -99
price4 = 77
price5 = 12354411

print(f'Price 1 is ${price1: 10}') # make spaces
print(f'Price 2 is ${price2:.1f}') #round the number to 1 decimal
print(f'Price 3 is ${price3:+10}')
print(f'Price 4 is ${price4:^10}')
print(f'Price 5 is ${price5:,}')