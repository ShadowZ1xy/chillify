import sys
import threading
import time

from PySide2 import QtWidgets, QtGui

import hint
import os_tool
import timer_config
import timer_gui as gui
import timer_settings

settings_vars = timer_settings.get_settings()
duration = settings_vars[timer_config.keyword_duration]
periodicity = settings_vars[timer_config.keyword_periodicity]
pause_multimedia = settings_vars[timer_config.keyword_multimedia_pause]
anyway_pause = None
user_pause = False
user_reset = False
paused = False
RESET_KEYWORD = "RESET"


def tray_start():
    app = QtWidgets.QApplication()
    icon = QtGui.QIcon("icon.ico")

    main_widget = QtWidgets.QSystemTrayIcon(icon)
    main_widget.setToolTip('Chillify')
    menu = QtWidgets.QMenu(None)

    pause = menu.addAction("Пауза")
    pause.triggered.connect(lambda: pause_toggle(pause))
    pause.setCheckable(True)

    update = menu.addAction("Обновить настройки")
    update.triggered.connect(lambda: update_settings())

    menu.addSeparator()

    media_pause = menu.addAction("Остановить медиа во время отдыха")
    media_pause.triggered.connect(lambda: media_pause_toggle(media_pause))
    media_pause.setCheckable(True)
    media_pause.setChecked(pause_multimedia)

    exit_ = menu.addAction("Выход")
    exit_.triggered.connect(lambda: sys.exit())

    main_widget.setContextMenu(menu)
    if pause_multimedia and os_tool.is_audio_playing() is None:
        warning_audio_driver()
    main_widget.setVisible(True)
    main_widget.show()
    sys.exit(app.exec_())


def timer_start():
    while True:
        if __countdown(periodicity * 60) == RESET_KEYWORD:
            continue
        if timer_continue():
            timer_proc()
        else:
            while not timer_continue():
                time.sleep(5)


def warning_audio_driver():
    global anyway_pause
    message = "В вашей системе не корректно работает аудио драйвер." \
              "\nИз за этого функция определения проигрывание аудио/видео не будет работать." \
              "\nХотите оставить функцию остановки воспроизведение во время отдыха включенным?" \
              "\n(если у вас будет аудио на паузе то во время отдыха оно будет включатся а в конце отключатся)"
    box = QtWidgets.QMessageBox()
    box.setWindowIcon(QtGui.QIcon("icon.ico"))
    box.setIcon(QtWidgets.QMessageBox.Warning)
    box.setWindowTitle('Предупреждение!')
    box.setText(message)
    box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    buttonY = box.button(QtWidgets.QMessageBox.Yes)
    buttonY.setText('Да')
    buttonN = box.button(QtWidgets.QMessageBox.No)
    buttonN.setText('Нет')
    box.exec_()

    if box.clickedButton() == buttonY:
        anyway_pause = True
    elif box.clickedButton() == buttonN:
        anyway_pause = False


def timer_proc():
    global paused
    if (pause_multimedia and os_tool.is_audio_playing() is True) or (anyway_pause is True):
        os_tool.play_pause_multimedia()
        paused = True
    gui.show_timer_window(duration, hint.get_random_hint())
    if (pause_multimedia and paused and os_tool.is_audio_playing() is False) or (anyway_pause is True):
        os_tool.play_pause_multimedia()
    paused = False


def __countdown(seconds):
    global user_reset
    while user_pause:
        time.sleep(1)
    if user_reset:
        user_reset = False
        return RESET_KEYWORD
    if seconds > 0:
        time.sleep(1)
        return __countdown(seconds - 1)


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


def media_pause_toggle(media):
    global pause_multimedia
    pause_multimedia = not pause_multimedia
    media.setChecked(pause_multimedia)


def update_settings():
    global settings_vars, duration, periodicity, pause_multimedia, user_reset
    settings_vars = timer_settings.get_settings()
    duration = settings_vars[timer_config.keyword_duration]
    pause_multimedia = settings_vars[timer_config.keyword_multimedia_pause]
    if periodicity != settings_vars[timer_config.keyword_periodicity]:
        user_reset = True
        periodicity = settings_vars[timer_config.keyword_periodicity]


if __name__ == '__main__':
    th1 = threading.Thread(target=tray_start)
    th2 = threading.Thread(target=timer_start)

    th1.start()
    th2.start()
