import time

import keyboard
import pyautogui
import pygetwindow
import pyscreeze
from pyautogui import ImageNotFoundException, sleep
from pygetwindow import Win32Window

keep_running = True
bookmarks_found_this_run = 0
mystics_found_this_run = 0


def toggle_loop():
    global keep_running
    keep_running = not keep_running


# dont use win.maximize()

# matchingWindows = pygetwindow.getWindowsWithTitle("Epic Seven")
# win = matchingWindows[0]
# win.activate()
# print(f"{win.title} window found")
#
# if box:= pyautogui.locateOnWindow("images/secretShopTitle.png", "Epic Seven", confidence=0.7):
#     print("Secret shop found")
# else:
#     print("Secret shop not found")

def focus_epic_seven():
    matchingWindows = pygetwindow.getWindowsWithTitle("Epic Seven x Frieren")
    win: Win32Window = matchingWindows[0]
    if win.isMinimized or not win.isActive:
        win.minimize()
        win.restore()
    return win


def isBookmarkOnScreen():
    try:
        if pyautogui.locateOnWindow("images/covenantBookmarkIcon.png", "Epic Seven", confidence=0.7):
            return True
        else:
            return False
    except ImageNotFoundException:
        return False


def isMysticOnScreen():
    try:
        if pyautogui.locateOnWindow("images/mysticMedalIcon.png", "Epic Seven", confidence=0.7):
            return True
        else:
            return False
    except ImageNotFoundException:
        return False


def isSecretShopOnScreen():
    try:
        if pyautogui.locateOnWindow("images/secretShopTitle.png", "Epic Seven", confidence=0.7):
            return True
        else:
            return False
    except ImageNotFoundException:
        return False


def performRefresh():
    return None


# def move_right(box: pyscreeze.Box):
#     # pyautogui.moveTo(box.top+box.height, box.left+box.width)
#     # pyautogui.moveRel(500, 0)
#     pyautogui.click(box.top+box.height+500, box.left+box.width)

def buy_bookmark():
    print("Bookmark found, trying to buy it")
    # locate bookmark
    box: pyscreeze.Box = pyautogui.locateOnWindow("images/covenantBookmarkIcon.png", "Epic Seven", confidence=0.7)
    # press buy to the right of it
    pyautogui.click(box.left + box.width + 500, box.top + box.height - 20)
    # press confirm buy
    click_on_buy_button()
    global bookmarks_found_this_run
    bookmarks_found_this_run += 1


def click_on_buy_button():
    time.sleep(1.5)
    box = pyautogui.locateOnWindow("images/buyButton.png", "Epic Seven", confidence=0.9)
    pyautogui.click(box.left + box.width / 2, box.top + box.height / 2)
    time.sleep(0.5)


def buy_mystic():
    print("Mystic found, trying to buy it")
    # locate bookmark
    box: pyscreeze.Box = pyautogui.locateOnWindow("images/mysticMedalIcon.png", "Epic Seven", confidence=0.7)
    # press buy to the right of it
    pyautogui.click(box.left + box.width + 500, box.top + box.height - 20)
    # press confirm buy
    click_on_buy_button()
    global mystics_found_this_run
    mystics_found_this_run += 1


def scroll_down_a_bit(win, amount=500):
    # win = focus_epic_seven()

    x0, y0 = win.left, win.top
    w, h = win.width, win.height
    cx, cy = x0 + w // 2, y0 + h // 2
    pyautogui.moveTo(cx, cy)
    # pyautogui.dragRel(0,-amount)
    pyautogui.scroll(-amount, x=cx, y=cy)
    time.sleep(0.5)


def refresh_shop():
    box = pyautogui.locateOnWindow("images/refreshButton.png", "Epic Seven", confidence=0.7)
    pyautogui.click(box.left + box.width / 2, box.top + box.height / 2)
    time.sleep(0.5)
    confirm_box = pyautogui.locateOnWindow("images/confirmButton.png", "Epic Seven", confidence=0.6)
    pyautogui.click(confirm_box.left + confirm_box.width / 2, confirm_box.top + confirm_box.height / 2)
    time.sleep(1.5)


def main():
    global keep_running
    global bookmarks_found_this_run
    global mystics_found_this_run
    loop_counter = 0
    # add toggle off
    print("Press q to stop the loop. Or move mouse to display's corner")
    keyboard.add_hotkey("q", toggle_loop)
    print("Stop toggle set")
    # find and put on top epic seven window
    window = focus_epic_seven()
    time.sleep(1)
    print("Starting main loop")


    while keep_running:
        bookmark_found = False
        mystic_found = False
        # check if secret shop is even opened
        if not isSecretShopOnScreen():
            print("No secret shop found on screen")
            keep_running = False
            raise Exception("No secret shop on screen")
        #         check if bookmark found, then buy it
        if isBookmarkOnScreen():
            buy_bookmark()
            bookmark_found = True
        #         check if medal found, then buy it
        if isMysticOnScreen():
            buy_mystic()
            mystic_found = True
        #         scroll down
        scroll_down_a_bit(window)
        if not bookmark_found:
            if isBookmarkOnScreen():
                buy_bookmark()
        #         check if medal found, then buy it
        if not mystic_found:
            if isMysticOnScreen():
                buy_mystic()
        #         refresh shop
        refresh_shop()
        loop_counter += 1
        print(
            f"Refreshing shop. Stats this run: RFRSH: {loop_counter} - BKMRKS: {bookmarks_found_this_run * 5} - MSTCS: {mystics_found_this_run * 50}")


if __name__ == "__main__":
    main()
