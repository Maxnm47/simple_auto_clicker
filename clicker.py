import pyautogui
import keyboard

#finder pos:

def pos_finder():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if keyboard.is_pressed('enter'):
            break
    return (x, y)
pos = pos_finder()

x = pos[0]
y = pos[1]

pyautogui.moveTo(pos)
while pos == (x,y):
    x, y = pyautogui.position()
    pyautogui.click(x, y)


