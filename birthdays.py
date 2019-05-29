
birthdays={'abhay':'april 3','tanuj':'may 2'}

while True:
    print('Enter the name ______ or dont enter anything for exit')
    name=input()
    if name=='  ':
        break
    if name in birthdays:
        print(birthdays[name]+' '+'is the birthday of '+name)
    else:
        print('i dont have birthday details of'+name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('birthday database updated')