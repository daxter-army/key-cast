keyDirectory = {
    # small alphabets
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    # big alphabets
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'H': 'H',
    'I': 'I',
    'J': 'J',
    'K': 'K',
    'L': 'L',
    'M': 'M',
    'N': 'N',
    'O': 'O',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z',
    # Arrows
    'Key.up': 'Up ⬆️',
    'Key.down': 'Down ⬇️',
    'Key.left': 'Left ⬅️',
    'Key.right': 'Right ➡️',
    # Operation Keys
    'Key.esc': 'Escape',
    'Key.space': 'Space',
    'Key.enter': 'Enter ↵',
    'Key.backspace': 'Backspace ⌫',
    'Key.tab': 'Tab ↹',
    'Key.shift': 'L Shift ⇧',
    'Key.shift_r': 'R Shift ⇧',
    'Key.ctrl': 'L Ctrl',
    'Key.ctrl_r': 'R Ctrl',
    'Key.alt': 'L Alt ⎇',
    'Key.alt_r': 'R Alt ⎇',
    'Key.cmd': 'L Super Key',
    'Key.cmd_r': 'R Super Key',
    'Key.menu': 'Menu Key 𝌆',
    # Locks
    'Key.caps_lock': 'Caps Lock Toggle',
    'Key.num_lock': 'Num Lock Toggle',
    # Function Keys
    'Key.f1': 'F1',
    'Key.f2': 'F2',
    'Key.f3': 'F3',
    'Key.f4': 'F4',
    'Key.f5': 'F5',
    'Key.f6': 'F6',
    'Key.f7': 'F7',
    'Key.f8': 'F8',
    'Key.f9': 'F9',
    'Key.f10': 'F10',
    'Key.f11': 'F11',
    'Key.f12': 'F12',
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
    '`': '`',
    '~': '~',
    '!': '!',
    '@': '@',
    '#': '#',
    '$': '$',
    '%': '%',
    '^': '^',
    '&': '&',
    '*': '*',
    '(': '(',
    ')': ')',
    '-': '-',
    '_': '_',
    '=': '=',
    '+': '+',
    '[': '[',
    '{': '{',
    ']': ']',
    '}': '}',
    '\\\\': '\\',
    '|': '|',
    ';': ';',
    ':': ':',
    "'": "'",
    '"': '"',
    "''": "'",
    '""': '"',
    ',': ',',
    '<': '<',
    '.': '.',
    '>': '>',
    '?': '?',
    '/': '/',
    '/': '/',
    '*': '*',
    # Numbers
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    # Special Bindings
    '<65056>': 'Tab',
    '<65437>': '5',
    '<65511>': 'Left Alt',
}


def filterKeys(key):
    # print('FILTER KEYS CALLED!')
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
    if 'f10' in key:
        return 'Key.f10'
    if 'f11' in key:
        return 'Key.f11'
    if 'f12' in key:
        return 'Key.f12'

    return key