import time

import keyboard
import pyautogui
import pygetwindow
from pygetwindow import Win32Window

# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
keep_running = True
def move_right():
    pyautogui.moveRel(500, 0)

def toggle_loop():
    global keep_running
    keep_running = not keep_running

# for purchase on ItemFound
# need to move 13 cm right

# def move_from_item_to_buy(box: Box):


def scroll_down_a_bit(amount = 500):
    win = focus_epic_seven()


    x0, y0 = win.left, win.top
    w, h = win.width, win.height
    cx, cy = x0 + w // 2, y0 + h // 2
    pyautogui.moveTo(cx, cy)
    # pyautogui.dragRel(0,-amount)
    pyautogui.scroll(-amount, x=cx, y=cy)


def perform_refresh():
    pass

def perform_buy():
    pass


def focus_epic_seven():
    matchingWindows = pygetwindow.getWindowsWithTitle("Epic Seven")
    win: Win32Window = matchingWindows[0]
    if win.isMinimized or not win.isActive:
        win.minimize()
        win.restore()
        # time.sleep(1000)
    return win

# TOGGLE_KEY = 'shift'
# keyboard.add_hotkey('shift', move_right)
# keyboard.add_hotkey("s", toggle_loop)
# keyboard.add_hotkey("w", scroll_down_a_bit)
#
# while keep_running:
#     pass

print()