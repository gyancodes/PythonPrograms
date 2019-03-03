def spam(divideBy):
   try:
       return 42/divideBy
   except ZeroDivisionError:
       print('Error: invalid argument')




print(spam(5))
print(spam(4))
print(spam(0))