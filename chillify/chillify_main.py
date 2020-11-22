import sys
import threading
import time

from PySide2 import QtWidgets, QtGui

from chillify import hint
from chillify import os_tool
from chillify import timer_config
from chillify import timer_gui as gui
from chillify import timer_settings

settings_vars = timer_settings.get_settings()
duration = settings_vars[timer_config.keyword_duration]
periodicity = settings_vars[timer_config.keyword_periodicity]
pause_multimedia = settings_vars[timer_config.keyword_multimedia_pause]
user_pause = False


def tray_start():
    global user_pause
    app = QtWidgets.QApplication()
    icon = QtGui.QIcon("icon.ico")

    main_widget = QtWidgets.QSystemTrayIcon(icon)
    main_widget.setToolTip('Chillify')
    menu = QtWidgets.QMenu(None)

    pause = menu.addAction("Не беспокоить")
    pause.triggered.connect(lambda: pause_toggle(pause))
    pause.setCheckable(True)

    update = menu.addAction("Обновить настройки")
    update.triggered.connect(lambda: update_settings())

    menu.addSeparator()

    exit_ = menu.addAction("Выход")
    exit_.triggered.connect(lambda: sys.exit())

    main_widget.setContextMenu(menu)

    main_widget.setVisible(True)
    main_widget.show()
    main_widget.show()
    sys.exit(app.exec_())


def timer_start():
    while True:
        time.sleep(periodicity * 60)
        if timer_continue() and not user_pause:
            if pause_multimedia:
                os_tool.play_pause_multimedia()
            gui.show_timer_window(duration, hint.get_random_hint())
            if pause_multimedia:
                os_tool.play_pause_multimedia()
        else:
            while not timer_continue() or user_pause:
                time.sleep(5)


def timer_continue():
    current_program_list = os_tool.get_program_list()
    pause_programs_list = timer_settings.get_settings()[timer_config.keyword_program_list]
    for program in current_program_list:
        for pause_program in pause_programs_list:
            if program == pause_program:
                return False
    return True


def pause_toggle(pause):
    global user_pause
    user_pause = not user_pause
    pause.setChecked(user_pause)


def update_settings():
    global settings_vars, duration, periodicity, pause_multimedia
    settings_vars = timer_settings.get_settings()
    duration = settings_vars[timer_config.keyword_duration]
    periodicity = settings_vars[timer_config.keyword_periodicity]
    pause_multimedia = settings_vars[timer_config.keyword_multimedia_pause]


if __name__ == '__main__':
    th1 = threading.Thread(target=tray_start)
    th2 = threading.Thread(target=timer_start)

    th1.start()
    th2.start()
