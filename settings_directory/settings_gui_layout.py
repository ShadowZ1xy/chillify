import config


def get_layout(sg, current_program_list, ignore_list,
               default_value_duration, default_value_periodicity):
    return [
        [sg.Text("Продолжительность: "),
         sg.Slider(range=(3, 60),
                   orientation='h',
                   size=(30, 10),
                   default_value=default_value_duration,
                   key=config.keyword_duration),
         sg.Text("секунд.")],

        [sg.Text("Каждые: "),
         sg.Slider(range=(1, 60),
                   orientation='h',
                   size=(30, 10),
                   default_value=default_value_periodicity,
                   key=config.keyword_periodicity),
         sg.Text("минут.", )],

        [sg.Text()],
        [sg.Listbox(values=current_program_list,
                    size=(27, 10),
                    key="current_programs",
                    select_mode="multiple"),
         sg.Button(button_text=config.settings_add_program_button_name),
         sg.Listbox(values=ignore_list,
                    size=(27, 10),
                    select_mode="multiple",
                    key=config.keyword_program_list),
         sg.Button(button_text=config.settings_delete_program_button_name)],

        [sg.Text()],
        [
            sg.Submit(button_text=config.settings_ok_button_name),
            sg.Cancel(button_text=config.settings_close_button_name),
            sg.Submit(button_text=config.settings_save_button_name)
        ]

    ]