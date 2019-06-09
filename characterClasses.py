import re
print('---Using the character set \d \s \w---')
regex=re.compile(r'\d+\s\w+')
print(regex.findall('12 Aplles, 23 chocos,4 ball,6 bat'))

print('---Making own character set---')
vowelregex=re.compile(r'[aeiouAEIOU]')
print(vowelregex.findall('I love you so much'))

print('---Range of letters using hyphen in the character set---')
regx=re.compile(r'[a-zA-Z0-9]')         #it will match lowercase letters,uppercase letters and numbers
print(regx.findall('I love you so much saalu'))

print('---Negative character set---')               #it excludes that character set (^)caret character for negation
negreg=re.compile(r'[^aeiouAEIOU]')                 #here space is also printed as character
print(negreg.findall('I love you so much saalu'))
print('--removing spaces--')
negregex=re.compile(r'[^aeiouAEIOU\s]')             #here space is not taken
print(negregex.findall('I love you so much saalu'))

print('---using caret ^ and dollar $ sign character---')
'''^ sign is used to match the string that begins with ...'''
beginswithHello=re.compile(r'^Hello')
print(beginswithHello.findall('Hello world!'))

'''$ dollar sign is used to match the string that ends with ...'''
endswith=re.compile(r'\d+$')                               # plus + is for one or more
print(endswith.findall('I love you 3000'))

'''beginswith and endswith'''
print('-begins with digit and ends with digit-')
beginswithandendswith=re.compile(r'^\d+$')                  #plus is for one or more
print(beginswithandendswith.findall('13148941168443'))

print('---using wildcard character (.)---')
wildcard=re.compile(r'.at')                             #matches any character except new line
print(wildcard.findall('The cat in the hat sat on the flat mat'))

print('---matching everything with dot star---')
nameregex=re.compile(r'Firstname:(.*) Lastname:(.*)')
bb=nameregex.search('Firstname:Abhay Lastname:Shekhar')
print(bb.group(1))
print(bb.group(2))

print('---Case insensitive matching---')
reg=re.compile(r'robocop',re.I)         #passing re.I as argument to re.compile to ignore the case of matched string
pr=reg.search('RoboCop protects the innoncent')
print(pr.group())
