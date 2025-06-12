#Nested loops = a loop within another loop (outer, inner)

for x in range(3):
    for y in range(3, 0, -1):
        print(y, end="") #[end=""] to make the terminal run Horizontally 
    print() # Empty prin() will make a new line between loops


rows = int(input('Enter the rows: '))
columns = int(input('Enter the columns: '))
symbol = input('Enter the symbol: ')

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") 
    print() 