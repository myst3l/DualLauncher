import subprocess
from pywinauto import application

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
urls = ["https://www.youtube.com", "https://www.google.com"]

# Open the URLs in separate windows
for i, url in enumerate(urls):
    subprocess.Popen([chrome_path, url, "--new-window"])

# Wait for Chrome to open the windows
app = application.Application().connect(path=chrome_path)
while len(app.windows()) < len(urls):
    pass

# Resize and position the windows
windows = app.windows()
for i, window in enumerate(windows):
    if i == 0:
        window.move_window(0, 0, 800, 600)
    else:
        window.move_window(800, 0, 800, 600)
