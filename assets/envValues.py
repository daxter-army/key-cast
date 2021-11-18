import platform
from sys import exit
import os

# pruning second instance, if first is running
# if not os.path.exists('./lockfile.txt'):
#     lockFile_ = open('lockfile.txt', 'w')
#     lockFile_.write(str(os.getpid()))
#     lockFile_.close()
# else:
#     PID = str(os.getpid())
#     f = open('lockfile.txt', 'r')
#     file_PID = f.read()
#     file_PID = int(file_PID.strip())

#     if file_PID != PID:
#         f.close()
#         exit()

ENV_VALUES = {
    'PLATFORM': platform.system().lower(),
    'APP_WIDTH': 380,
    'APP_HEIGHT': 140,
    'SETTINGS_WIDTH': 300,
    'SETTINGS_HEIGHT': 180,
    'FONT_NAME': 'TkDefaultFont',
    'ALPHA_VALUE': 1.0,
    'ALPHA_VALUE_MIN': 0.3,
    'ALPHA_VALUE_MAX': 1.0
}

THEMES = {
    'DEFAULT': {
        'BG_COLOR': '#13274F',
        'FONT_COLOR': '#FFFFFF'
    },
    'HACKER': {
        'BG_COLOR': '#222222',
        'FONT_COLOR': '#08EC11'
    },
    'VANILLA': {
        'BG_COLOR': '#FFFFFF',
        'FONT_COLOR': '#222222'
    },
}