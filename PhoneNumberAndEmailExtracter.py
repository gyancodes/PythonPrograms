import re,pyperclip

phoneregex=re.compile(r'''(
          (.\d{2}|\(.\d{2}\))?    #area code  e.g. +91
          (\s|-|\.)?            #separator  e.g. -
          (\d{5})               #first 5 digit
          (\s|-|\.)             #separator
          (\d{5})               #last 5 digits
          (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension ext,x,ext.,followed by 2-5 digits
          )''',re.VERBOSE)

#text=str(pyperclip.paste())

emailregex=re.compile(r'''(
            [a-zA-Z0-9._%+-]+
            @
            [a-zA-Z0-9.-]+
            (\.[a-zA-Z]{2,4})
            )''',re.VERBOSE)

'''find matches in the clipboard text'''
text=str(pyperclip.paste())
matches=[]
for groups in phoneregex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

'''copy results to the clipboard'''
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('--Copied to the clipboard--')
    print('\n'.join(matches))
else:
    print('No phone number or email found ')


'''to execute the program first copy the text from where you want to extract(cntr+A &ctrl+C)
 and then run this program'''