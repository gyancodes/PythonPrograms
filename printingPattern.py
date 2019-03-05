#for printing following pattern
#A
#AB
#ABC
#ABCD
#ABCDE
#ABCDEF

for i in range(1,7):
    char = 65
    for j in  range(1,i+1):
        print (chr(char),end='')
        char+=1
    print ()