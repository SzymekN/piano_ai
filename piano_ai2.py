#Set-ExecutionPolicy Unrestricted -Scope Process
import pyautogui
import keyboard
import time
import win32api
import win32con
from ctypes import windll


pos_1 = (970,500)
pos_2 = (1130,500)
pos_3 = (1300,500)
pos_4 = (1455,500)


def is_black(tile):
    if tile_1[0] <50 and tile[1] < 50 and tile[2] < 50:
        return True
    return False

def click(pos):
    win32api.SetCursorPos((pos[0],pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def calibration():
    state_left = win32api.GetKeyState(0x01)
    while True:
        clicked = win32api.GetKeyState(0x01)
        if clicked != state_left:
            time.sleep(0.1)
            return pyautogui.position()

def get_pixel(pos):
    return windll.gdi32.GetPixel(dc,pos[0],pos[1])

choice = input("Calibrate?")
if choice == 'y':
    print("Click on tile 1")
    pos_1 = calibration()
    print(pos_1[0])
    print("Click on tile 2")
    pos_2 = calibration()
    print("Click on tile 3")
    pos_3 = calibration()
    print("Click on tile 4")
    pos_4 = calibration()
    print("Calibrated")


dc = windll.user32.GetDC(0)

print("click to start, q to break loop")
# get the state of left mouse button
state_left = win32api.GetKeyState(0x01)
time.sleep(0.1)

# continue until q wasn't pressed
while keyboard.is_pressed('q') == False:

    # start on mouse click
    clicked = win32api.GetKeyState(0x01)
    if clicked != state_left:

        while keyboard.is_pressed('q') == False: 
            start = time.time()
            img = pyautogui.screenshot()

            # niefortunnie za wolno
            # tile_1 = get_pixel(pos_1)
            # tile_2 = get_pixel(pos_2)
            # tile_3 = get_pixel(pos_3)
            # tile_4 = get_pixel(pos_4)

            # color_1 = int(bin(tile_1)[-8:], 2) 
            # color_2 = int(bin(tile_2)[-8:], 2) 
            # color_3 = int(bin(tile_3)[-8:], 2) 
            # color_4 = int(bin(tile_4)[-8:], 2) 

            end = time.time()
            print(end-start)

            tile_1 = img.getpixel(pos_1)
            tile_2 = img.getpixel(pos_2)
            tile_3 = img.getpixel(pos_3)
            tile_4 = img.getpixel(pos_4)

            if tile_1[0] <20:
                click(pos_1)
            if tile_2[0] <20:
                click(pos_2)
            if tile_3[0] <20:
                click(pos_3)
            if tile_4[0] <20:
                click(pos_4)
                
        
print(tile_1)

#x 50,160,270,360
#y 500

