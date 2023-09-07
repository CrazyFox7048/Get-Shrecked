import sys, subprocess
packages = ["Tk", "keyboard", "pyautogui", "Pillow"]
for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
import getpass, tkinter, urllib.request, os, subprocess, keyboard, time, winsound
from PIL import Image, ImageTk
def file_check(user):
    if not os.path.exists("C:\\Users\\"+user+"\\AppData\\Roaming\\get.png"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/get.png?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
    if not os.path.exists("C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/Donkey.wav?raw=true", filename= "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.wav")
user = getpass.getuser()
file_check(user)
sound = "C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3"
pilImage = Image.open("C:\\Users\\"+user+"\\AppData\\Roaming\\get.png")
root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.bind("<Down>", lambda e: (e.widget.withdraw(), e.widget.quit()))
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='white')
imgWidth, imgHeight = pilImage.size
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(w/2,h/2,image=image)
while True:
    if keyboard.is_pressed("down"):
        break
    file_check(user)
    time.sleep(0.6)
    pyautogui.press('volumeup', 10)
    winsound.PlaySound("C:\\Users\\"+user+"\\AppData\\Roaming\\donkey.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS)
    root.update()
