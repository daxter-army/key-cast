import platform
from sys import exit
import os

# pruning second instance, if first is running
if not os.path.exists('./lockfile.txt'):
    lockFile_ = open('lockfile.txt', 'w')
    lockFile_.write(str(os.getpid()))
    lockFile_.close()
else:
    PID = str(os.getpid())
    f = open('lockfile.txt', 'r')
    file_PID = f.read()
    file_PID = int(file_PID.strip())

    if file_PID != PID:
        f.close()
        exit()

ENV_VALUES = {
    'PLATFORM': platform.system().lower(),
    'APP_WIDTH': 380,
    'APP_HEIGHT': 140,
    'FONT_NAME': 'TkDefaultFont',
    'FONT_COLOR': '#FFFFFF',
    'BG_COLOR': '#13274F',
    'ALPHA_VALUE': 0.5,
}