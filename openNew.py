import subprocess
import pyautogui
import time

url1 = 'https://www.twitch.tv/pokimane'
url2 = 'https://www.twitch.tv/popout/xqc/chat?popout='
#
subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe', url1, '--new-window'])
subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe', url2, '--new-window'])

time.sleep(1)

# MOVE, RESIZE, CLOSE CHAT AND SET TO THEATRE MODE

window1 = pyautogui.getWindowsWithTitle('pokimane - Twitch')[0]

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
