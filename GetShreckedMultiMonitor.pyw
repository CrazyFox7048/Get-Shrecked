import tkinter, urllib.request, os, keyboard, time, screeninfo, pyautogui, pygame.mixer
from PIL import Image, ImageTk

def get_sound():
    if not os.path.exists(".\\donkey.wav"):
        urllib.request.urlretrieve("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/Donkey.wav?raw=true", filename= ".\\donkey.wav")
    return ".\\donkey.wav"

def start_shrek():
    pilImage = Image.open(urllib.request.urlopen("https://github.com/CrazyFox7048/Get-Shrecked/blob/main/get.png?raw=true"))
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
        canvas[i] = tkinter.Canvas(root[i],width=w,height=h)
        canvas[i].pack()
        canvas[i].configure(background='white')
        image[i] = ImageTk.PhotoImage(pilImage)
        canvas[i].create_image(w/2,h/2,image=image[i])
        root[i].attributes('-topmost', True)
        
        pygame.mixer.init()
        pygame.mixer.music.load(get_sound())
    
        while True:
            get_sound()
            time.sleep(0.6)
            try:
                pyautogui.press('volumeup', 100)
            except:
                pass
            pygame.mixer.music.play()
            for i in range(0, len(screeninfo.get_monitors())):
                root[i].update()

def block_keyboard():
    for i in range(150):
        keyboard.block_key(i)
        

if __name__ == "__main__":
    block_keyboard()
    start_shrek()
