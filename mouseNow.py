import pyautogui,time
time.sleep(5)

print('press ctrl+c to quit .')
try:
    while True:
        x,y=pyautogui.position()
        positionstr='X:' +  str(x).rjust(4)+ 'Y:' +str(y).rjust(4)
        print(positionstr, end='')
        print('\b'*len(positionstr),end='',flush=True)
        pyautogui.click(x,y)
except KeyboardInterrupt:
    print('\n Done')

