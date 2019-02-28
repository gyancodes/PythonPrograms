def eg():
    eggs=1890
    newegg()
    print(eggs)
    print(newEgg) #here global variable can be accessed inside of fumnction

def newegg():
    eggs=0   #this does not effect the local value of eggs in other function local variable
           #this eggs scope is inside this function only

newEgg=50
eg()
