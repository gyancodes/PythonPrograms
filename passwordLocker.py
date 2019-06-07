#not safe to use ,just for try

#save this file in C:\Python34 folder
#save the  file passwordLocker.bat in C:Windows folder
"""
#passwordLocker.bat

@py.exe C:Python34\passwordLocker.py %*
@pause
"""

PASSWORDS={'email':'dajbdjbwb',
           'facebook':'svcajvjbk',
           'instagram':'cbjkasbci'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: passwordLocker.py [account]-copy account password')
    sys.exit()
account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account +'copied to clipboard')
else:
    print('There is no account named '+account)

