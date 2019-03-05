while(1):
    print ('Enter Your Name')
    name=input()
    if name.isalpha()==False:
        print ('Sorry You Cannnot proceed')
        break
    else:
        print ('Enter your PAn Card number')
        Pan=input()
        if Pan.isalnum()==False:
            print ('Invalid Pan number ! Sorry You Cannot Proceed')
            break
        print ('Please '+name+' check ,your Pan number is :'+Pan)
        break
