spam={'color':'red','age':'42'}
for i in spam.values():                    #value() method
    print(i)


for j in spam.keys():
    print(j)                               #keys() metod


for k,m in spam.items():
    print('key:'+k +' '+ 'value:'+m)       #using both methods together


#setdefault method
#if the key is not present in the dictionary then it sets th enew value otherwise does nothing

google={'name':'pooka','age':'5'}
if 'color' not in google:
    google['color']='black'     #first way to do
print(google)

#using setdefault method
google.setdefault('origin','India')
print(google)