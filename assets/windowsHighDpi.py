import ctypes

def windowsHighDpi():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)