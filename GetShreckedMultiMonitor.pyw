import sys, subprocess
packages = ["Tk", "keyboard", "screeninfo", "pyautogui", "Pillow"]
for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
import getpass, tkinter, urllib.request, os, keyboard, time, winsound, screeninfo, pyautogui
from PIL import Image, ImageTk
def file_check(user):
    if not os.path.exists("C:\\Users\\"+user+"\\AppData\\Roaming\\get.png"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/get.png?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
    if not os.path.exists("C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.wav"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/Donkey.wav?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.wav")
user = os.getlogin()
file_check(user)
sound = "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.wav"
pilImage = Image.open("C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
imgWidth, imgHeight = pilImage.size
root = []
canvas = []
image = []
displays = screeninfo.get_monitors()
for i in range(0, len(screeninfo.get_monitors())):
    root.append("")
    canvas.append("")
    image.append("")
    if i == 0:
        root[i] = tkinter.Tk()
    else:
        root[i] = tkinter.Toplevel()
    w, h, x, y = displays[i].width, displays[i].height, displays[i].x, displays[i].y
    root[i].overrideredirect(1)
    root[i].geometry("%dx%d+%d+%d" % (w, h, x, y))
    root[i].bind("<Down>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas[i] = tkinter.Canvas(root[i],width=w,height=h)
    canvas[i].pack()
    canvas[i].configure(background='white')
    image[i] = ImageTk.PhotoImage(pilImage)
    canvas[i].create_image(w/2,h/2,image=image[i])
    root[i].attributes('-topmost', True)
while True:
    if keyboard.is_pressed("down"):
        break
    file_check(user)
    time.sleep(0.6)
    try:
        pyautogui.press('volumeup', 10)
    except FailSafeException:
        None
    winsound.PlaySound(sound, winsound.SND_ASYNC | winsound.SND_ALIAS)
    for i in range(0, len(screeninfo.get_monitors())):
        root[i].update()
