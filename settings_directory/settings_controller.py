import config
from settings_directory import settings_service as service

running = True


def event_controller(window, program_list):
    global running
    while running:
        event, values = window.read()
        print("Event: ", event)
        print("Values", values)
        print()
        if event in (None, config.settings_close_button_name):
            running = False
        elif event == config.settings_ok_button_name:
            service.settings_save(values, program_list)
            running = False
        elif event == config.settings_save_button_name:
            service.settings_save(values, program_list)
        elif event == config.settings_add_program_button_name:
            service.program_add(window, values, program_list)
        elif event == config.settings_delete_program_button_name:
            service.program_delete(window, values, program_list)
