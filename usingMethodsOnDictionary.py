spam={'color':'red','age':42}
for i in spam.values():         #value() method
    print(i)

for j in spam.keys():
    print(j)        #keys() metod


for k,m in spam.items():
    print('key:'+k +' '+ 'value:'+str(m))       #using both methods together
