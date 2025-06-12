import time

#my_time= int(input('Enter the time in seconds: ')) #Be sure to use int which allow user to type numbers only

#for x in reversed(range(0,my_time)):    #reverse func to count backwards
#    print(x)                            #to print the numbers in terminal
#    time.sleep(1)                       #sleep will pause the program for (...) time 
  
#print("times up")

Timer= int(input('Ender timer: '))
for x in range(Timer, 0, -1):    #another way to use reversed function
    seconds = x % 60             #[%] used to not allow the number go above 60
    minutes = int(x / 60) % 60   #[int] used to make true numbers without decimals
    hours = int(x/120)  %24      #[%24] to make the max 24 hours 
    print(f'{hours:02}:{minutes:02}:{seconds:02}')                            
    time.sleep(1)
print("times up")