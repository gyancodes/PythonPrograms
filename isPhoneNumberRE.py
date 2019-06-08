import re
phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #regular expression compiles
mobject=phoneNumberRegex.search('My number is 415-654-9874')    #search() searches for the given re in the entire string
print('Phone number found: '+mobject.group())     #group(0 gives the matched string


phnregex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  #first parenthesis is for first group(1) and second parnhesis for second
mob=phnregex.search('My number is 415-654-9874')
print('Area :'+mob.group(1)+'\t Main Phone number :'+mob.group(2))

'''since mob.groups returns tuple we can use as'''
a,b=mob.groups()
print(a,b)

batregex=re.compile(r'Bat(man|mobile|copter)')  #re for batman,batmobile,batcopter
mobj=batregex.search('Batmobile lost a wheel')
print(mobj.group())