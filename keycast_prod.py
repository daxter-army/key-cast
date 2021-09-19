# for making it an executable
import sys
from os import path

# tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

# pynput
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

# for windows
import ctypes

# because it wont work in linux and macos
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

ENV_VALUES = {
    'APP_WIDTH': 380,
    'APP_HEIGHT': 140,
    'FONT_NAME': 'TkDefaultFont',
    'FONT_COLOR': '#FFFFFF',
    'BG_COLOR': '#13274F',
    'ALPHA_VALUE': 0.8,
}

keyDirectory = {
    # small alphabets
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i',
    'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r',
    's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',
    # big alphabets
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
    'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
    'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
    'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
    'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', 'Z': 'Z',
    # Arrows
    'Key.up': 'Up ⬆️', 'Key.down': 'Down ⬇️', 'Key.left': 'Left ⬅️', 'Key.right': 'Right ➡️',
    # Operation Keys
    'Key.esc': 'Escape', 'Key.space': 'Space', 'Key.enter': 'Enter ↵', 'Key.backspace': 'Backspace ⌫', 'Key.tab': 'Tab ↹', 'Key.shift': 'L Shift ⇧', 'Key.shift_r': 'R Shift ⇧',
    'Key.ctrl': 'L Ctrl', 'Key.ctrl_l': 'L Ctrl', 'Key.ctrl_r': 'R Ctrl', 'Key.alt': 'L Alt ⎇', 'Key.alt_l': 'L Alt ⎇', 'Key.alt_r': 'R Alt ⎇', 'Key.alt_gr': 'R Alt ⎇',
    'Key.cmd': 'L Super Key', 'Key.cmd_r': 'R Super Key', 'Key.menu': 'Menu Key 𝌆',
    # Locks
    'Key.caps_lock': 'Caps Lock Toggle', 'Key.num_lock': 'Num Lock Toggle',
    # Function Keys
    'Key.f1': 'F1', 'Key.f2': 'F2', 'Key.f3': 'F3', 'Key.f4': 'F4', 'Key.f5': 'F5', 'Key.f6': 'F6',
    'Key.f7': 'F7', 'Key.f8': 'F8', 'Key.f9': 'F9', 'Key.f10': 'F10', 'Key.f11': 'F11', 'Key.f12': 'F12',
    # Other Functions
    'Key.print_screen': 'Print Screen',
    'Key.scroll_lock': 'Scroll Lock',
    'Key.pause': 'Pause',
    'Key.insert': 'Insert',
    'Key.home': 'Home ⤒',
    'Key.page_up': 'Page Up',
    'Key.delete': 'Delete',
    'Key.end': 'End ⤓',
    'Key.page_down': 'Page Down',
    'Key.media_volume_up': 'Volume Up',
    'Key.media_volume_down': 'Volume Down',
    'Key.media_volume_mute': 'Volume Mute/Unmute',
    # Special Characters
    '`': '`', '~': '~', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '&': '&', '*': '*', '(': '(', '*': '*',
    ')': ')', '-': '-', '_': '_', '=': '=', '+': '+', '[': '[', '{': '{', ']': ']', '}': '}', '\\\\': '\\', '/': '/',
    '|': '|', ';': ';', ':': ':', "'": "'", '"': '"', "''": "'", '""': '"', ',': ',', '<': '<', '.': '.', '>': '>', '?': '?', '/': '/',
    # Numbers
    '0': '0', '1': '1',
    '2': '2', '3': '3',
    '4': '4', '5': '5',
    '6': '6', '7': '7',
    '8': '8', '9': '9',
    # Special Bindings
    '<65056>': 'Tab', '<65437>': '5', '<65511>': 'Left Alt', '<96>': '0', '<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5', '<102>': '6',
    '<103>': '7', '<104>': '8', '<105>': '9', '<106>': '*', '<107>': '+', '<109>': '-', '<110>': '.', '<111>': '/', '<186>': ';', '<188>': ',', '<190>': '.', '<191>': '/', '<222>': "'",
    # other special bindings
    '\\x01': 'a', '\\x02': 'b', '\\x03': 'c', '\\x04': 'd',
    '\\x05': 'e', '\\x06': 'f', '\\x07': 'g', '\\x08': 'h',
    '\\t': 'i', '\\n': 'j', '\\x0b': 'k', '\\x0c': 'l',
    '\\r': 'm', '\\x0e': 'n', '\\x0f': 'o', '\\x10': 'p',
    '\\x11': 'q', '\\x12': 'r', '\\x13': 's', '\\x14': 't',
    '\\x15': 'u', '\\x16': 'v', '\\x17': 'w', '\\x18': 'x',
    '\\x19': 'y', '\\x1a': 'z', '\\x1b': '[', '\\x1d': ']',
    '\\x1c': '\\',
}


def filterKeys(key):
    # print('FILTER KEYS CALLED!')
    if 'f10' in key:
        return 'Key.f10'
    if 'f11' in key:
        return 'Key.f11'
    if 'f12' in key:
        return 'Key.f12'
    if 'f1' in key:
        return 'Key.f1'
    if 'f2' in key:
        return 'Key.f2'
    if 'f3' in key:
        return 'Key.f3'
    if 'f4' in key:
        return 'Key.f4'
    if 'f5' in key:
        return 'Key.f5'
    if 'f6' in key:
        return 'Key.f6'
    if 'f7' in key:
        return 'Key.f7'
    if 'f8' in key:
        return 'Key.f8'
    if 'f9' in key:
        return 'Key.f9'

    return key


# ? ---- TKINTER
root = tk.Tk()
root.columnconfigure(0, weight=1)
previousActionVal = tk.StringVar(value="Previous Action")
presentActionVal = tk.StringVar(value="Current Action")
mouseActionVal = tk.StringVar(value="Mouse Action")
# ? ----

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

# ? ----

# * ---- GUI
# ? ---- TKINTER FUNCTIONS
# exit function


def quitWindow(*args):
    root.quit()

# saving last position of the window


def saveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

# updating new position of the window


def newPosition(event):
    x = event.x - lastClickX + root.winfo_x()
    y = event.y - lastClickY + root.winfo_y()

    root.geometry(f'+{x}+{y}')
# ? ----


# ? ---- FOR LINUX (TRANSPARENT WINDOW)
# root.wait_visibility(root)
# root.wm_attributes('-alpha', ALPHA_VALUE)
# ? -----


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
try:
    bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    path_to_assets = path.join(
        bundle_dir, 'assets', 'icons', 'cross', 'times_solid_20_white.png')
    cross_btn_image = tk.PhotoImage(file=path_to_assets)
except:
    print('exception')
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
# ? ----

# ?---- CONFIGURING TKINTER
screen_length = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_offset = int(screen_length - screen_length*0.21)
y_offset = int(screen_height - screen_height*0.18)

# headless window
root.overrideredirect(True)

# disabling resizing of the window
root.resizable(False, False)

# always on top
root.attributes('-topmost', True)

# size of the window
root.geometry(
    '{}x{}+{}+{}'.format(ENV_VALUES['APP_WIDTH'], ENV_VALUES['APP_HEIGHT'], x_offset, y_offset))

# firing event listeners
listenInputEvents()

# binding mouse events for dragging window
root.bind('<Button-1>', saveLastClickPos)
root.bind('<B1-Motion>', newPosition)

# firing tkinter's event loop
root.mainloop()
# ?----
