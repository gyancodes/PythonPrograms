import re
phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #regular expression
mob=phoneNumberRegex.search('My number is 415-654-9874')    #search() searches for the given re in the entire string
print('Phone number found: '+mob.group())     #group(0 gives the matched string