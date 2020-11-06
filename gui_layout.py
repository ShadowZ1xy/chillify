def get_layout(sg, current_program_list, ignore_list):
    return [
        [sg.Text("Продолжительность: "),
         sg.Slider(range=(3, 60),
                   orientation='h',
                   size=(30, 10),
                   default_value=20,
                   key="duration"),
         sg.Text("секунд.")],

        [sg.Text("Каждые: "),
         sg.Slider(range=(1, 60),
                   orientation='h',
                   size=(30, 10),
                   default_value=10,
                   key="periodicity"),
         sg.Text("минут.", )],

        [sg.Listbox(values=current_program_list,
                    size=(20, 10),
                    key="besides",
                    select_mode="multiple"),
         sg.Button(button_text=">"),
         sg.Listbox(values=ignore_list,
                    size=(20, 10),
                    select_mode="multiple",
                    key="ignore"),
         sg.Button(button_text="╳")],

        [sg.Submit(button_text="Сохранить"), sg.Cancel(button_text="Отменить")]
    ]
