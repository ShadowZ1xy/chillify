import PySimpleGUI as sg

import config
import os_tool
from settings_directory import settings
from settings_directory import settings_controller as controller
from settings_directory import settings_gui_layout as gui_layout


def settings_window_run():
    loaded_settings = settings.get_settings()
    current_program_list = os_tool.get_program_list()
    program_list = loaded_settings[config.keyword_program_list]
    duration = loaded_settings[config.keyword_duration]
    periodicity = loaded_settings[config.keyword_periodicity]

    layout = gui_layout.get_layout(sg, current_program_list,
                                   program_list, duration, periodicity)

    window = sg.Window(config.settings_window_title, layout)
    controller.event_controller(window, program_list)

if __name__ == "__main__":
    settings_window_run()