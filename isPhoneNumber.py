def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('222-325-2541  :is this a phone number')
print(isPhoneNumber('222-325-2541'))
print('mos-mos-mosi  :is this a phone number')
print(isPhoneNumber('mos-mos-mosi'))

message='Call me at 415-555-6541 tommorow. 415-541-6656 is my office'
for i in range(0,len(message)):
    check=message[i:i+12]
    if isPhoneNumber(check):
        print('phone number found  :'+check)
print('over,Done')