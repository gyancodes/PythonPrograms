import pyautogui,time
time.sleep(5)

print('press ctrl+c to quit .')
try:
    while True:
        x,y=pyautogui.position()
        positionstr='X:' +  str(x).rjust(4)+ 'Y:' +str(y).rjust(4)
        print(positionstr, end='')
        print('\b'*len(positionstr),end='',flush=True)
        pyautogui.click(15,37)
        time.sleep(1)
        pyautogui.click(26,71)


except KeyboardInterrupt:
    print('\n Done')

