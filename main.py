import subprocess
import pyautogui
import time
from pywinauto import application
import win32gui
import win32con


url1 = 'https://www.twitch.tv/forsen'
url2 = 'https://www.twitch.tv/popout/xqc/chat?popout='
#
subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe', url1, '--new-window'])
subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe', url2, '--new-window'])

time.sleep(1)

# ------------------------------------------------------------------------------------

# MOVE, RESIZE, CLOSE CHAT AND SET TO THEATRE MODE

window1 = pyautogui.getWindowsWithTitle('forsen - Twitch')[0]

window1.moveTo(1912, -250)
pyautogui.moveTo(2479, -225)
pyautogui.dragRel(0, -100, duration=0.4)

window1.moveTo(1912, -250)
window1.resizeTo(1096, 685)

time.sleep(0.1)

# CHAT WINDOW

window2 = pyautogui.getWindowsWithTitle('Chat')[0]

window2.moveTo(1912, 427)
pyautogui.moveTo(2479, 445)
pyautogui.dragRel(0, -100, duration=0.4)

window2.moveTo(1912, 427)
window2.resizeTo(1096, 800)

# -------------------------------------------------------------------

# pyautogui.leftClick(x=2300, y=100)
# pyautogui.hotkey('alt', 't')
# pyautogui.hotkey('alt', 'r')

time.sleep(0.04)
pyautogui.leftClick(x=2644, y=166)                                  # Theatre Mode
time.sleep(0.04)
pyautogui.leftClick(x=2716, y=-150)                                 # Collapse Chat

# --------------------------------------------------------------------------------

# screen_width, screen_height = pyautogui.size()
#
# window_width = screen_width // 2
# window_height = screen_height
# window1_pos = (0, 0)
# window2_pos = (window_width, 0)
#
# for i in range(2):
#     window = pyautogui.getWindowsWithTitle('Google Chrome')[i]
#     window.resizeTo(window_width, window_height)
#     window.moveTo(*window1_pos if i == 0 else window2_pos)

# ------------------------------------------------------------------------------------


# print(pyautogui.size())
# print(pyautogui.position())
# # pyautogui.click(x=2645, y=-173, clicks=1, button=2)
# # pyautogui.leftClick(x=2645, y=-173)
# # pyautogui.leftClick(x=2714, y=-516)
#
# # pyautogui.leftClick(x=2794, y=-217)
#
# # pyautogui.leftClick(pyautogui.position())
# # pyautogui.typewrite('Hello world!')
#
#
# pyautogui.leftClick(pyautogui.position())
# pyautogui.hotkey('alt', 't')
# # Point(x=2678, y=-110)

# ------------------------------------------------------------------
# app = application.Application().start("notepad.exe")

# Connect to the main window
# window = app.UntitledNotepad

# # Resize the window
# window.SetSize(500, 500)
#
# # Move the window
# window.MoveWindow(100, 100)

# window.print_control_identifiers()

# --------------------------------------------------------------------------


#
