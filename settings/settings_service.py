import tkinter as tk

import os_tool
import settings_config as config
import settings_db


def gui_elements_setup(root, duration, periodicity, multimedia_boolean):
    duration_label = tk.Label(root, text="Продолжительность в секундах:")
    duration_slider = tk.Scale(root, from_=5, to=90, orient=tk.HORIZONTAL,
                               length=170, sliderlength=20)
    periodicity_label = tk.Label(root, text="Периодичность в минутах:")
    periodicity_slider = tk.Scale(root, from_=5, to=60, orient=tk.HORIZONTAL,
                                  length=170, sliderlength=20)

    multimedia = tk.BooleanVar()
    multimedia_checkbox = tk.Checkbutton(root, text="Пауза мультимедии во время отдыха",
                                         variable=multimedia,
                                         onvalue=1, offvalue=0)

    current_program_label = tk.Label(root, text="Текущие программы")
    current_program_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    ignore_list_label = tk.Label(root, text="Программы паузы")
    ignore_list_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    add_btn = tk.Button(root,
                        text=config.settings_add_program_button_name,
                        command=lambda: __add_to_list(current_program_listbox,
                                                      ignore_list_listbox))
    update_btn = tk.Button(root,
                           text="@",
                           command=lambda: update_current_programs(current_program_listbox))
    delete_btn = tk.Button(root,
                           text=config.settings_delete_program_button_name,
                           command=lambda: __delete_from_list(ignore_list_listbox))

    ok_btn = tk.Button(root, text=config.settings_ok_button_name,
                       command=lambda: __ok_button_handler(root, setup))
    apply_btn = tk.Button(root, text=config.settings_save_button_name,
                          command=lambda: settings_db.get_settings_from_gui_then_save(setup))
    cancel_btn = tk.Button(root, text=config.settings_close_button_name,
                           command=lambda: root.destroy())

    duration_slider.set(duration)
    periodicity_slider.set(periodicity)
    multimedia.set(1 if multimedia_boolean else 0)

    duration_label.place(x=10, y=28)
    duration_slider.place(x=195, y=10)
    periodicity_label.place(x=10, y=68)
    periodicity_slider.place(x=195, y=50)
    multimedia_checkbox.place(x=8, y=94)
    current_program_label.place(x=8, y=120)
    ignore_list_label.place(x=190, y=120)
    current_program_listbox.place(x=10, y=140, width=150)
    ignore_list_listbox.place(x=192, y=140, width=150)
    add_btn.place(x=164, y=190, width=25, height=25)
    update_btn.place(x=164, y=218, width=25, height=25)
    delete_btn.place(x=346, y=210, width=25, height=25)
    ok_btn.place(x=10, y=318, width=40)
    apply_btn.place(x=120, y=318)
    cancel_btn.place(x=60, y=318)

    setup = {"root": root,
             config.keyword_duration: duration_slider,
             config.keyword_periodicity: periodicity_slider,
             "program_listbox": ignore_list_listbox,
             config.keyword_multimedia_pause: multimedia}
    return {"current_program_listbox": current_program_listbox,
            "ignore_list_listbox": ignore_list_listbox}


def update_current_programs(listbox):
    program_list = os_tool.get_program_list()
    listbox.delete(0, listbox.size())
    for program in program_list:
        listbox.insert(0, program)


def set_pause_programs(listbox, list_):
    for program in list_:
        listbox.insert(0, program)


def __ok_button_handler(window, setup):
    settings_db.get_settings_from_gui_then_save(setup)
    window.destroy()


def __add_to_list(main_listbox, secondary_listbox):
    select = list(main_listbox.curselection())
    select.reverse()
    for i in select:
        selected_str = main_listbox.get(i)
        list2str = secondary_listbox.get(0, secondary_listbox.size())
        if selected_str not in list2str:
            secondary_listbox.insert(0, selected_str)
    main_listbox.selection_clear(0, main_listbox.size())


def __delete_from_list(listbox):
    select = list(listbox.curselection())
    select.reverse()
    for i in select:
        listbox.delete(i)
