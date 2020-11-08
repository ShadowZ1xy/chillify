import PySimpleGUI as sg

import config
import os_tool
from settings_directory import settings
from settings_directory import settings_controller as controller
from settings_directory import settings_gui_layout as gui_layout

if __name__ == "__main__":
    loaded_settings = settings.get_settings()
    program_list = loaded_settings[config.keyword_program_list]
    layout = gui_layout.get_layout(sg, os_tool.get_program_list(),
                                   program_list,
                                   loaded_settings[config.keyword_duration],
                                   loaded_settings[config.keyword_periodicity])
    window = sg.Window(config.settings_window_title, layout)
    controller.event_controller(window, program_list)
