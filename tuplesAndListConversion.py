#tuples are similar to list but it is written in small bracket and its values cannot be modified

name=('Abhay','Shekhar','Yadav')   #tuple format

#using list function to convert tuple into list

name=list(('abhay','shekhar'))
print(name)
print('after appending')
name.append('yadav')
print(name)    #now slicing can be done after making tuple as a list

# using tuple function to convert list into tuple
name1=tuple(('abhay','shekhar'))
#name1.append('yadav')    now it cannot be appended or removed