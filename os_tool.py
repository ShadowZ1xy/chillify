import subprocess

cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Name'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


def get_program_list():
    program_list = []
    for line in proc.stdout:
        if line.rstrip():
            program_list.append(line.decode().rstrip())
    del program_list[:2]
    program_list = [x for x in program_list if "Windows" not in x]
    return program_list
