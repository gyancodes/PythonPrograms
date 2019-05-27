import pyautogui, time

time.sleep(5)

print('press ctrl+c to quit .')
try:
    for i in range(5):
        x, y = pyautogui.position()
        positionstr = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
        print(positionstr, end='')
        print('\b' * len(positionstr), end='', flush=True)
        pyautogui.click(100,100)       #open any editor in top left corner so that it will type it there
        pyautogui.typewrite('\t\t Hello World!  ',0.25)


except KeyboardInterrupt:
    print('\n Done')

