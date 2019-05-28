catname=[]
while True:
    print('Enter the name of cat'+ str(len(catname)+1)+'  '+'or enter nothing to stop:')
    name=input()
    if name=='':
        break
    catname=catname+[name]     #list concatenation
print('catnames are here:')
for i in range(len(catname)):
    print(catname[i])
