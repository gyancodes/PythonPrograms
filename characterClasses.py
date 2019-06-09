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