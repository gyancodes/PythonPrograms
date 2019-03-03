#using getpass module to enter password without making pwd visible
import getpass

password=getpass.getpass(prompt='Enter the password:')
if password==oxford:            #enter oxford as a password just for trial
    print('Welcome to the world of python programming')
else:
    print('Incorrect password ...sorry you cannot read our book')