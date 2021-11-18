# tkinter
from assets.envValues import ENV_VALUES, THEMES
from assets.keyUtils import keyDirectory, filterKeys
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import tkinter as tk
from tkinter import Text, ttk
from os import remove as removeFile
# from math import 
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
opacityVal = tk.DoubleVar(value=1.0)

screen_length = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

lastClickX = 0
lastClickY = 0

xOffset = 0
yOffset = 0

# selecting theme
CURR_THEME_VAL = tk.StringVar(value="DEFAULT")

# loading button images
exit_btn_image = tk.PhotoImage(file='./assets/icons/times_solid_20_tomato.png')
quit_btn_image_b = tk.PhotoImage(file='./assets/icons/times_solid_20_black.png')
quit_btn_image_w = tk.PhotoImage(file='./assets/icons/times_solid_20_white.png')
quit_btn_image_g = tk.PhotoImage(file='./assets/icons/times_solid_20_green.png')
pref_btn_image_b = tk.PhotoImage(file='./assets/icons/settings_solid_18_black.png')
pref_btn_image_w = tk.PhotoImage(file='./assets/icons/settings_solid_18_white.png')
pref_btn_image_g = tk.PhotoImage(file='./assets/icons/settings_solid_18_green.png')

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
#! not working in windows (trackpad only), dont know about mac

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
    x = event.x - lastClickX + root.winfo_x()
    y = event.y - lastClickY + root.winfo_y()

    # print('x: ', x, 'y: ', y)

    # if x > screen_length*0.5 and y < screen_height*0.5:
    #     print('1st Q')
    #     root.geometry(f'+{x}+{y}')
    # elif x < screen_length*0.5 and y < screen_height*0.5:
    #     print('2nd Q')
    #     root.geometry(f'+{x}+{y}')
    # elif x < screen_length*0.5 and y > screen_height*0.5:
    #     print('3rd Q')
    #     root.geometry('+{}+{}'.format(40, int(screen_height*0.85)))
    # else:
    #     print('4th Q')

    root.geometry(f'+{x}+{y}')


# ? ----

# ? ---------- FRONTEND ----------


# * ---------- Tkinter Gui Starts ----------
# Tkinter functions
def quitWindow(*args):
    # try:
    #     removeFile('./lockfile.txt')
    # except:
    #     pass

    root.quit()

#* Child Process Functions Starts
def openSettings(*args):
    # window config
    offspring = tk.Toplevel(root)
    settings_w = ENV_VALUES['SETTINGS_WIDTH']
    settings_h = ENV_VALUES['SETTINGS_HEIGHT']
    offspring.geometry(f'{settings_w}x{settings_h}+{str(int(screen_length/2 - (settings_w/2)))}+{str(int(screen_height/2 - (settings_h/2)))}')
    offspring.title('Preferences')
    # offspring.overrideredirect(True)
    offspring.resizable(False, False)
    # offspring.attributes('-toolwindow', True)

    # elements
    # order matters here, not names, (just for declaration)
    first_frame_offspring = tk.Frame(offspring)
    first_frame_offspring.pack(side="top", fill="both", expand=True, padx=10)

    second_frame_offspring = tk.Frame(offspring)
    second_frame_offspring.pack(side="top", fill="both", expand=True, padx=10, pady=5)

    # separator_frame = tk.Frame(offspring)
    # separator_frame.pack(side="top", fill="both", expand=True, padx=10)

    # separator_label = tk.Label(offspring)
    # separator_label.pack(fill='both', expand=True)

    third_frame_offspring = tk.Frame(offspring)
    third_frame_offspring.pack(side="top", fill="both", expand=True, padx=10)

    fourth_frame_offspring = tk.Frame(offspring)
    fourth_frame_offspring.pack(side="top", fill="both", expand=True, padx=10, pady=7)

    theme_label = tk.Label(
        first_frame_offspring,
        text='Themes',
        anchor='w',
        pady=7
    )
    theme_label.pack(side='left', fill='both', expand=True)

    # THEME STARTS
    default_theme_btn = tk.Button(
        second_frame_offspring,
        text='Default',
        command= lambda: changeTheme('DEFAULT'),
        bg=THEMES['DEFAULT']['BG_COLOR'],
        foreground=THEMES['DEFAULT']['FONT_COLOR'],
        highlightbackground=THEMES['DEFAULT']['BG_COLOR'],
        activebackground=THEMES['DEFAULT']['BG_COLOR'],
    )
    default_theme_btn.pack(side='left', fill='both', expand=True)

    vanilla_theme_btn = tk.Button(
        second_frame_offspring,
        text='Vanilla',
        command= lambda: changeTheme('VANILLA'),
        bg=THEMES['VANILLA']['BG_COLOR'],
        foreground=THEMES['VANILLA']['FONT_COLOR'],
        highlightbackground=THEMES['VANILLA']['BG_COLOR'],
        activebackground=THEMES['VANILLA']['BG_COLOR'],
    )
    vanilla_theme_btn.pack(side='left', fill='both', expand=True)

    hacker_theme_btn = tk.Button(
        second_frame_offspring,
        text='Hacker',
        command= lambda: changeTheme('HACKER'),
        bg=THEMES['HACKER']['BG_COLOR'],
        foreground=THEMES['HACKER']['FONT_COLOR'],
        highlightbackground=THEMES['HACKER']['BG_COLOR'],
        activebackground=THEMES['HACKER']['BG_COLOR'],
    )
    hacker_theme_btn.pack(side='left', fill='both', expand=True)
    # THEME ENDS

    opacity_label = tk.Label(
        third_frame_offspring,
        text='Opacity',
        anchor='w'
    )
    opacity_label.pack(side='left', fill='both', expand=True)

    # OPACITY STARTS
    opacity_changer = ttk.Scale(
        fourth_frame_offspring,
        from_=ENV_VALUES['ALPHA_VALUE_MIN'],
        to=ENV_VALUES['ALPHA_VALUE_MAX'],
        orient='horizontal',
        variable=opacityVal,
        command=changeOpacity,
    )
    opacity_changer.pack(side='left', fill='both', expand=True)
    # OPACITY ENDS

def changeOpacity(*args):
    alphaVal = round(opacityVal.get(), 1)
    root.wm_attributes('-alpha', alphaVal)
    ENV_VALUES['ALPHA_VALUE'] = alphaVal
    print(alphaVal)

def changeTheme(theme):
    CURR_THEME_VAL.set(theme)

    # change all the props here
    first_frame.configure(background=THEMES[theme]['BG_COLOR'])
    second_frame.configure(background=THEMES[theme]['BG_COLOR'])
    third_frame.configure(background=THEMES[theme]['BG_COLOR'])

    label1.configure(bg=THEMES[theme]['BG_COLOR'], foreground=THEMES[theme]['FONT_COLOR'])
    label3.configure(bg=THEMES[theme]['BG_COLOR'], foreground=THEMES[theme]['FONT_COLOR'])
    mouse_action_label.configure(bg=THEMES[theme]['BG_COLOR'], foreground=THEMES[theme]['FONT_COLOR'])

    if theme == "VANILLA":
        button_quit.configure(
            image=quit_btn_image_b,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )

        button_pref.configure(
            image=pref_btn_image_b,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )
    elif theme == "HACKER":
        button_quit.configure(
            image=quit_btn_image_g,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )

        button_pref.configure(
            image=pref_btn_image_g,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )
    else:
        button_quit.configure(
            image=quit_btn_image_w,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )
        button_pref.configure(
            image=pref_btn_image_w,
            bg=THEMES[theme]['BG_COLOR'],
            foreground=THEMES[theme]['FONT_COLOR'],
            highlightbackground=THEMES[theme]['BG_COLOR'],
            activebackground=THEMES[theme]['BG_COLOR'],
        )
    
    print(theme)

#* Child Process Functions Ends

# ? ---- FOR LINUX (TRANSPARENT WINDOW)
root.wait_visibility(root)
root.wm_attributes('-alpha', ENV_VALUES['ALPHA_VALUE'])
# ? -----


# setting font
# font.nametofont(ENV_VALUES['FONT_NAME'])).configure(size=12)


# ? ---- GUI ELEMENTS
# frames
first_frame = tk.Frame(root, background=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'])
first_frame.pack(side="top", fill="both", expand=True)

second_frame = tk.Frame(root, background=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'])
second_frame.pack(side="top", fill="both", expand=True)

third_frame = tk.Frame(root, background=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'])
third_frame.pack(side="top", fill="both", expand=True)

# previous action label
label1 = tk.Label(
    first_frame,
    textvariable=previousActionVal,
    bg=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    foreground=THEMES[CURR_THEME_VAL.get()]['FONT_COLOR'],
    anchor='w'
)
label1.pack(
    side='left',
    fill='both',
    expand=True,
    padx=10
)

# quit button
button_quit = tk.Button(
    first_frame,
    image=quit_btn_image_w,
    command=quitWindow,
    bg=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    foreground=THEMES[CURR_THEME_VAL.get()]['FONT_COLOR'],
    highlightbackground=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    activebackground=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    borderwidth=0,
    cursor="hand2"
)
button_quit.pack(
    side='right',
    fill='both',
    ipadx=7
)

# settings button
button_pref = tk.Button(
    third_frame,
    image=pref_btn_image_w,
    command=openSettings,
    bg=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    foreground=THEMES[CURR_THEME_VAL.get()]['FONT_COLOR'],
    highlightbackground=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    activebackground=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    borderwidth=0,
    cursor="hand2"
)
button_pref.pack(
    side='right',
    fill='both',
    ipadx=7
)
# children of left frame
# previous_action_label = tk.Label(left_frame, textvariable=previousActionVal, font=(FONT_NAME, 11))
# previous_action_label.pack(side="top", anchor="w", expand=True, fill="y", ipadx=10)

# current action
label3 = tk.Label(
    second_frame,
    textvariable=presentActionVal,
    bg=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    foreground=THEMES[CURR_THEME_VAL.get()]['FONT_COLOR'],
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
    bg=THEMES[CURR_THEME_VAL.get()]['BG_COLOR'],
    foreground=THEMES[CURR_THEME_VAL.get()]['FONT_COLOR'],
    anchor='w'
)
mouse_action_label.pack(
    side='top',
    fill='both',
    expand=True,
    padx=10
)

# ?---- CONFIGURING TKINTER

# setting up offsets wrt to platform
if ENV_VALUES['PLATFORM'] == 'windows':
    # global xOffset, yOffset
    xOffset = int(screen_length - ENV_VALUES['APP_WIDTH']*1.05)
    yOffset = int(screen_height - ENV_VALUES['APP_HEIGHT']*1.5)
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
root.bind('<Double-Button-1>', openSettings)

# firing tkinter's event loop
root.mainloop()