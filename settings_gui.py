import PySimpleGUI as sg
import config
import settings_gui_layout as gui_layout
import os_tool
import settings

if __name__ == "__main__":
    loaded_settings = settings.get_settings()
    program_list = loaded_settings[config.keyword_program_list]
    layout = gui_layout.get_layout(sg, os_tool.get_program_list(),
                                   program_list,
                                   loaded_settings[config.keyword_duration],
                                   loaded_settings[config.keyword_periodicity])
    window = sg.Window('File Compare', layout)
    while True:
        event, values = window.read()
        print(event, values)
        if event == "Сохранить":
            settings_to_save = {
                config.keyword_duration: values[config.keyword_duration],
                config.keyword_periodicity: values[config.keyword_periodicity],
                config.keyword_program_list: program_list
            }
            settings.set_settings(settings_to_save)
        elif event in (None, 'Отменить'):
            break
        elif event in ">":
            for el in values["current_programs"]:
                if el not in program_list:
                    program_list.append(el)
            window.Element(config.keyword_program_list).Update(values=program_list)
