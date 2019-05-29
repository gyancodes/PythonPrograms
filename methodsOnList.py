#methods
#index method

name=['abhay','shekhar','yadav','tanuj','chraborty']
print(name.index('shekhar'))    #it prints the index of desired list item

#append method
name.append('leon') #adds to the list item
print(name)

#insert method

name.insert(6,'patrick')    #inserts new list item in the desired index
print(name)

#remove method

name.remove('patrick')
print(name)

#sorting method
integer=[4,-1,19,2,0,8,1]
integer.sort()
print(integer)
integer.sort(reverse=True)
print(integer)  #sorting in reverse order