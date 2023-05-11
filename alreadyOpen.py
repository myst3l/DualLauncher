import subprocess
import pyautogui
import time

# get title of current window and get string of streamer name
# change url of chat-box to add name of current open stream
# or pop-out chat


# COPY FROM STREAM URL
pyautogui.doubleClick(x=2406, y=-195)
pyautogui.hotkey('ctrl', 'c')
pyautogui.leftClick(x=2300, y=100)
pyautogui.hotkey('alt', 't', 'r')


# -------------------------------------------------------------------------
# Add if statement to check if window is open

# OPEN CHAT
pyautogui.leftClick(x=2406, y=500)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite("https://www.twitch.tv/popout/")
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite("/chat?popout=")
pyautogui.hotkey('enter')
