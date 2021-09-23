import tkinter as tk
from tkinter import ttk
from assets.envValues import ENV_VALUES
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.columnconfigure(0, weight=1)

TransparencyValue = tk.DoubleVar(value=ENV_VALUES['ALPHA_VALUE'])

# root.config(bg='systemTransparent')

# root.wait_visibility(root)
# root.wm_attributes('-alpha', ENV_VALUES['ALPHA_VALUE'])
# root.wm_attributes('-transparentcolor', root['bg'])

# frames
title_bar_frame = tk.Frame(root)
title_bar_frame.columnconfigure(0, weight=1)
title_bar_frame.grid(row=0, column=0, sticky='EW', pady=(2, 4))

content_frame = tk.Frame(root)
content_frame.columnconfigure(0, weight=1)
content_frame.grid(row=1, column=0, sticky='EW', padx=10, pady=2)

themes_frame = tk.Frame(content_frame, bg='orange')
themes_frame.columnconfigure(0, weight=1,)
themes_frame.columnconfigure(1, weight=1)
themes_frame.columnconfigure(2, weight=1)
themes_frame.columnconfigure(3, weight=1)
themes_frame.grid(row=3, column=0, sticky='EW', pady=10)

# third_frame = tk.Frame(root)
# third_frame.pack(side="top", fill="both", expand=True)

def quit_w():
    root.quit()

def changeTransparency(*args):
    value = round(TransparencyValue.get(), 1)
    ENV_VALUES['ALPHA_VALUE'] = value
    root.wm_attributes('-alpha', ENV_VALUES['ALPHA_VALUE'])

def changeTheme(theme_):
    print('theme: ', theme_)

# previous action label
title_label = tk.Label(
    title_bar_frame,
    text='Settings',
    font=(ENV_VALUES['FONT_NAME'], 11, 'bold'),
    # anchor='w',
)
title_label.grid(
    row=0,
    column=0,
    sticky='W',
    padx=(3,0)
)

# quit button
cross_btn_image = tk.PhotoImage(file='./assets/icons/cross/times_solid_20.png')
button_quit = tk.Button(
    title_bar_frame,
    image=cross_btn_image,
    borderwidth=0,
    cursor="hand2",
    command=quit_w
)
button_quit.grid(
    row=0,
    column=1,
    padx=(0,3)
)

transparency_logo = tk.PhotoImage(file='./assets/icons/cross/adjust-solid.png')
transparency_logo_label = tk.Label(content_frame, image=transparency_logo)
transparency_logo_label.grid(row=0, column=0, sticky='W', padx=(0, 1))

transparency_label = tk.Label(content_frame, text='Transparency')
transparency_label.grid(row=0, column=0, sticky='W', padx=(21, 0))

transparency_slider = ttk.Scale(content_frame, from_=0.3, to=1, orient='horizontal', variable=TransparencyValue, command=changeTransparency)
transparency_slider.grid(row=1, column=0, sticky='EW', pady=(5, 5))

paint_label_logo = tk.PhotoImage(file='./assets/icons/cross/paint-roller-solid.png')
theme_logo_label = tk.Label(content_frame, image=paint_label_logo)
theme_logo_label.grid(row=2, column=0, sticky='W', padx=(0, 1))

theme_label = tk.Label(content_frame, text='Theme')
theme_label.grid(row=2, column=0, sticky='W', padx=(21, 0))

theme_1 = tk.Label(themes_frame, text='Default', bg='#13274F', foreground='white', font=(ENV_VALUES['FONT_NAME'], 9, 'bold'))
theme_1.grid(row=0, column=0, sticky='NEWS', ipady=5)
theme_2 = tk.Label(themes_frame, text='Vanilla', bg='white', foreground='black', font=(ENV_VALUES['FONT_NAME'], 9, 'bold'))
theme_2.grid(row=0, column=1, sticky='NEWS', ipady=5)
theme_3 = tk.Label(themes_frame, text='Hacker', bg='#222222', foreground='#09f62c', font=(ENV_VALUES['FONT_NAME'], 9, 'bold'))
theme_3.grid(row=0, column=2, sticky='NEWS', ipady=5)
theme_4 = tk.Label(themes_frame, text='Invincible', foreground='black', font=(ENV_VALUES['FONT_NAME'], 9, 'bold'))
theme_4.grid(row=0, column=3, sticky='NEWS', ipady=5)

theme_1.bind('<Button>', lambda arg : changeTheme('default'))
theme_2.bind('<Button>', lambda arg : changeTheme('vanilla'))
theme_3.bind('<Button>', lambda arg : changeTheme('hacker'))
theme_4.bind('<Button>', lambda arg : changeTheme('invincible'))

root.overrideredirect(True)
root.geometry('400x180')
root.mainloop()