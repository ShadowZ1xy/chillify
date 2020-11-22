import ctypes
import subprocess

cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Name"'
ignore_list = ["Windows", "python", "settings"]


def get_program_list():
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    program_list = []
    for line in proc.stdout:
        if line.rstrip():
            program_list.append(line.decode().rstrip())
    proc.terminate()
    del program_list[:2]
    program_list = [x for x in program_list if not __ignore_word(x)]
    return program_list


def play_pause_multimedia():
    SendInput(Keyboard(VK_MEDIA_PLAY_PAUSE))


def __ignore_word(string):
    for el in ignore_list:
        if el in string:
            return True
    return False


LONG = ctypes.c_long
DWORD = ctypes.c_ulong
ULONG_PTR = ctypes.POINTER(DWORD)
WORD = ctypes.c_ushort


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (('dx', LONG),
                ('dy', LONG),
                ('mouseData', DWORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (('wVk', WORD),
                ('wScan', WORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (('uMsg', DWORD),
                ('wParamL', WORD),
                ('wParamH', WORD))


class _INPUTunion(ctypes.Union):
    _fields_ = (('mi', MOUSEINPUT),
                ('ki', KEYBDINPUT),
                ('hi', HARDWAREINPUT))


class INPUT(ctypes.Structure):
    _fields_ = (('type', DWORD),
                ('union', _INPUTunion))


def SendInput(*inputs):
    nInputs = len(inputs)
    LPINPUT = INPUT * nInputs
    pInputs = LPINPUT(*inputs)
    cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
    return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)


INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
VK_MEDIA_PLAY_PAUSE = 0xB3  # Play/Pause Media key


def KeybdInput(code, flags):
    return KEYBDINPUT(code, code, flags, 0, None)


def Keyboard(code, flags=0):
    return Input(KeybdInput(code, flags))


def Input(structure):
    if isinstance(structure, MOUSEINPUT):
        return INPUT(INPUT_MOUSE, _INPUTunion(mi=structure))
    if isinstance(structure, KEYBDINPUT):
        return INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure))
    if isinstance(structure, HARDWAREINPUT):
        return INPUT(INPUT_HARDWARE, _INPUTunion(hi=structure))
    raise TypeError('Cannot create INPUT structure!')
