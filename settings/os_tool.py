import subprocess

__cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Name"'
__ignore_list = ["Windows", "python", "settings"]


def get_program_list():
    proc = subprocess.Popen(__cmd, shell=True, stdout=subprocess.PIPE)
    program_list = []
    for line in proc.stdout:
        if line.rstrip():
            program_list.append(line.decode().rstrip())
    proc.terminate()
    del program_list[:2]
    program_list = [x for x in program_list if not __ignore_word(x)]
    return program_list


def __ignore_word(string):
    for el in __ignore_list:
        if el in string:
            return True
    return False
