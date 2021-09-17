# tkinter
from assets.envValues import ENV_VALUES
from assets.keyUtils import keyDirectory, filterKeys
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import tkinter as tk
from tkinter import ttk
# import tkinter.font as font

# for windows
from assets.windowsHighDpi import windowsHighDpi

# because it wont work in linux and macos
try:
    windowsHighDpi()
except:
    pass

# initialising tkinter
root = tk.Tk()
root.columnconfigure(0, weight=1)
previousActionVal = tk.StringVar(value="Previous Action")
presentActionVal = tk.StringVar(value="Current Action")
mouseActionVal = tk.StringVar(value="Mouse Action")

lastClickX = 0
lastClickY = 0

xOffset = 0
yOffset = 0

# ? ---- BACKEND
# event listeners

SEMAPHORE = False
PREV_KEY = ''
# HISTORY_STRING = ''

# activates on keydown


def keyboardButtonDown(key):
    global PREV_KEY

    SEMAPHORE = True

    # print("SEMAPHORE (Down): ", SEMAPHORE)
    # print("PREV KEY: ", PREV_KEY)

    key = str(key).replace("'", "").strip()
    filteredKey = filterKeys(key)

    # print('key: ', key)
    # print('filtered key: ', filteredKey)

    # displaying previous events
    # if(not(presentActionVal.get() == "Let's Start")):
    #     previousActionVal.set(presentActionVal.get())

    if presentActionVal.get() == "Current Action":
        presentActionVal.set("")

    if SEMAPHORE:
        # previously key is pressed
        try:
            if PREV_KEY == keyDirectory[filteredKey]:
                pattern = presentActionVal.get() + keyDirectory[filteredKey]
                # count = pattern.count(keyDirectory[filteredKey])
                # print(count)
                presentActionVal.set(pattern)
                return

            if presentActionVal.get() == '':
                presentActionVal.set(keyDirectory[filteredKey])
            else:
                presentActionVal.set(
                    f'{presentActionVal.get()} + {keyDirectory[filteredKey]}')

            PREV_KEY = keyDirectory[filteredKey]
        except:
            if PREV_KEY == key:
                presentActionVal.set(f'{presentActionVal.get()} + {key}')
            else:
                presentActionVal.set(f'{presentActionVal.get()} + {key}')

            PREV_KEY = key
    # else:
    #     presentActionVal.set('')

    #     try:
    #         presentActionVal.set(keyDirectory[filteredKey])

    #         PREV_KEY = keyDirectory[filteredKey]
    #     except:
    #         presentActionVal.set(key)

    #         PREV_KEY = key
    # to catch platform dependent anomalies
    # try:
    #     presentActionVal.set(keyDirectory[filteredKey])
    #     PREV_KEY = keyDirectory[filteredKey]
    # except:
    #     presentActionVal.set(key)
    #     PREV_KEY = key


# activates on keyup, not registered right now
def keyboardButtonUp(key):
    global PREV_KEY

    key = str(key).replace("'", "")
    filteredKey = filterKeys(key)

    SEMAPHORE = False

    try:
        PREV_KEY = keyDirectory[filteredKey]
    except:
        PREV_KEY = key

    # storing prev value
    if(presentActionVal.get() != ''):
        previousActionVal.set(presentActionVal.get())

    #! trying to avoid this
    presentActionVal.set('')

    # print("SEMAPHORE (Up): ", SEMAPHORE)


# activates on mouse button pressed
def mouseButtonPressed(x, y, button, pressed):
    buttonType = str(button).replace('Button.', '')

    if pressed:
        mouseActionVal.set(f'{buttonType.capitalize()} Mouse Button')

# activates on mouse scroll
#! not working in windows, dont know about mac


def mouseScrolled(x, y, dx, dy):
    # print(x, y, dx, dy)
    if(dy == 1):
        mouseActionVal.set('Scroll Up ⬆️')
    else:
        mouseActionVal.set('Scroll Down ⬇️')

# firing up the listeners


def listenInputEvents():
    mouseListener = MouseListener(
        on_click=mouseButtonPressed, on_scroll=mouseScrolled)
    mouseListener.start()

    keyboardListener = KeyboardListener(
        on_press=keyboardButtonDown, on_release=keyboardButtonUp)
    keyboardListener.start()

# move windows


def saveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def newPosition(event):
    print('fired')
    x = event.x - lastClickX + root.winfo_x()
    Xpos = int(root.winfo_screenwidth() - ENV_VALUES['APP_WIDTH'])
    y = event.y - lastClickY + root.winfo_y()
    root.geometry(f'+{Xpos}+{y}')

# ? ----

# ? ---------- FRONTEND ----------


# * ---------- Tkinter Gui Starts ----------
FONT_NAME = "TkDefaultFont"
ALPHA_VALUE = 1
BG_COLOR = '#13274F'
FONT_COLOR = '#FFFFFF'

# Tkinter functions


def quitWindow(*args):
    root.quit()

# ? ---- FOR LINUX (TRANSPARENT WINDOW)
# root.wait_visibility(root)
# root.wm_attributes('-alpha', ENV_VALUES['ALPHA_VALUE'])
# ? -----


# setting font
# font.nametofont(ENV_VALUES['FONT_NAME'])).configure(size=12)


# ? ---- GUI ELEMENTS
# frames
first_frame = tk.Frame(root, background=ENV_VALUES['BG_COLOR'])
first_frame.pack(side="top", fill="both", expand=True)

second_frame = tk.Frame(root, background=ENV_VALUES['BG_COLOR'])
second_frame.pack(side="top", fill="both", expand=True)

third_frame = tk.Frame(root, background=ENV_VALUES['BG_COLOR'])
third_frame.pack(side="top", fill="both", expand=True)

# previous action label
label1 = tk.Label(
    first_frame,
    textvariable=previousActionVal,
    bg=ENV_VALUES['BG_COLOR'],
    foreground=ENV_VALUES['FONT_COLOR'],
    anchor='w'
)
label1.pack(
    side='left',
    fill='both',
    expand=True,
    padx=10
)

# quit button
cross_btn_image = tk.PhotoImage(
    file='./assets/icons/cross/times_solid_20_white.png')
button_quit = tk.Button(
    first_frame,
    image=cross_btn_image,
    command=quitWindow,
    bg=ENV_VALUES['BG_COLOR'],
    foreground=ENV_VALUES['FONT_COLOR'],
    highlightbackground=ENV_VALUES['BG_COLOR'],
    activebackground=ENV_VALUES['BG_COLOR'],
    borderwidth=0,
    cursor="hand2"
)
button_quit.pack(
    side='right',
    fill='both',
    ipadx=5
)

# children of left frame
# previous_action_label = tk.Label(left_frame, textvariable=previousActionVal, font=(FONT_NAME, 11))
# previous_action_label.pack(side="top", anchor="w", expand=True, fill="y", ipadx=10)

# current action
label3 = tk.Label(
    second_frame,
    textvariable=presentActionVal,
    bg=ENV_VALUES['BG_COLOR'],
    foreground=ENV_VALUES['FONT_COLOR'],
    font=(ENV_VALUES['FONT_NAME'], 16),
    anchor='w'
)
label3.pack(
    side='top',
    fill='both',
    expand=True,
    padx=10
)

# present_action_label = tk.Label(left_frame, textvariable=presentActionVal, font=(FONT_NAME, 18, 'bold'))
# present_action_label.pack(side="top", anchor="w", expand=True, fill="y", ipadx=10)

# mouse action
mouse_action_label = tk.Label(
    third_frame,
    textvariable=mouseActionVal,
    bg=ENV_VALUES['BG_COLOR'],
    foreground=ENV_VALUES['FONT_COLOR'],
    anchor='w'
)
mouse_action_label.pack(
    side='top',
    fill='both',
    expand=True,
    padx=10
)

# ?---- CONFIGURING TKINTER
screen_length = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# setting up offsets wrt to platform
if ENV_VALUES['PLATFORM'] != 'windows':
    # global xOffset, yOffset
    xOffset = int(screen_length - ENV_VALUES['APP_WIDTH']*1.1)
    yOffset = int(screen_height - ENV_VALUES['APP_HEIGHT']*1.7)
else:
    # global xOffset, yOffset
    xOffset = int(screen_length - ENV_VALUES['APP_WIDTH']*1.1)
    yOffset = int(screen_height - ENV_VALUES['APP_HEIGHT']*1.3)

# headless window
root.overrideredirect(True)

# disabling resizing of the window
root.resizable(False, False)

# always on top
root.attributes('-topmost', True)

# size of the window
root.geometry(
    '{}x{}+{}+{}'.format(ENV_VALUES['APP_WIDTH'], ENV_VALUES['APP_HEIGHT'], xOffset, yOffset))
# ?----

# firing event listeners
listenInputEvents()

# binding mouse events for dragging window
root.bind('<Button-1>', saveLastClickPos)
root.bind('<B1-Motion>', newPosition)

# firing tkinter's event loop
root.mainloop()

# for building from source file
# windows
# pyinstaller keycast_onefile.py --onefile --add-data "assets;assets" --windowed

# linux/macos
# pyinstaller keycast_onefile.py --onefile --add-data "assets:assets"
