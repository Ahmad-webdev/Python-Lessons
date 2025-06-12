# python compound interest calculator 

# Formula : A = p (1 + r/n)^t 
                            #A = final amount (after interest)
                            #P = principal (initial money)
                            #r = annual interest rate (decimal)
                            #n = number of times interest is compounded per year
                            #t = time in years

principle = 0
rate = 0
time = 0

while True:
    principle = float(input('enter your principle amount: '))
    if principle < 0:
        print('Principle cant be less than zero')
    else:
        break
        
while True :
    rate = float(input('enter your rate amount: '))
    if rate < 0:
        print('rate cant be less than zero')
    else:
        break

while True :
    time = float(input('enter the time in years: '))
    if time < 0:
        print('time cant be less than zero')
    else:
        break

total = principle * pow((1 + rate/100), time)

print(f'Balance after {time} year/s: ${total:.2f}')


#The reason we add (while [true]) is to make the loop continue no matter what until we break it.
# The benfit of that we can now add 0 values 