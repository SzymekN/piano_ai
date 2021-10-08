#Set-ExecutionPolicy Unrestricted -Scope Process
import pyautogui
import keyboard
import time
import win32api
import win32con
from ctypes import windll

def click(pos):
    # click at given position
    win32api.SetCursorPos((pos[0],pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def calibration():
    # calibrete where are tiles 

    # get state of left mb
    state_left = win32api.GetKeyState(0x01)
    while True:
        # if left mb state change return mouse position
        clicked = win32api.GetKeyState(0x01)
        if clicked != state_left:
            time.sleep(0.1)
            return pyautogui.position()

def get_pixel(pos):
    # get pixel value
    return windll.gdi32.GetPixel(dc,pos[0],pos[1])



# default tiles positions
pos_1 = (970,500)
pos_2 = (1130,500)
pos_3 = (1300,500)
pos_4 = (1455,500)

# calibrate tiles position or use defaults
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

            # niefortunnie za wolno
            tile_1 = get_pixel(pos_1)
            color_1 = int(bin(tile_1)[-8:], 2) 
            if color_1 <20:
                click(pos_1)
                # print("1")
            else:
                tile_2 = get_pixel(pos_2)
                color_2 = int(bin(tile_2)[-8:], 2) 
                if color_2 <20:
                    click(pos_2)
                    # print("2")
                else:
                    tile_3 = get_pixel(pos_3)
                    color_3 = int(bin(tile_3)[-8:], 2) 
                    if color_3 <20:
                        click(pos_3)
                        # print("3")
                    else:
                        tile_4 = get_pixel(pos_4)
                        color_4 = int(bin(tile_4)[-8:], 2) 
                        if color_4 <20:
                            click(pos_4)
                            # print("4")
                        # else:
                            # print("none")

            end = time.time()
            print(end-start)
