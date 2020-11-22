import tkinter as tk

import settings_config as config
import settings_db
import settings_service as service


def settings_window_setup():
    loaded_settings = settings_db.get_settings()
    program_list = set(loaded_settings[config.keyword_program_list])
    duration = loaded_settings[config.keyword_duration]
    periodicity = loaded_settings[config.keyword_periodicity]
    multimedia_boolean = loaded_settings[config.keyword_multimedia_pause]

    root = tk.Tk()
    root.resizable(False, False)
    root.title(config.settings_window_title)
    __window_to_center(root,
                       config.settings_window_width,
                       config.settings_window_height)

    gui_elements = service.gui_elements_setup(root, duration, periodicity, multimedia_boolean)
    service.update_current_programs(gui_elements["current_program_listbox"])
    service.set_pause_programs(gui_elements["ignore_list_listbox"], program_list)
    root.iconbitmap("icon.ico")
    return root


def __window_to_center(root, window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height,
                                       x_coordinate, y_coordinate))
