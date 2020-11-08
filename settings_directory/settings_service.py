import config
from settings_directory import settings


def settings_save(values, program_list):
    settings_to_save = {
        config.keyword_duration: values[config.keyword_duration],
        config.keyword_periodicity: values[config.keyword_periodicity],
        config.keyword_program_list: program_list
    }
    settings.set_settings(settings_to_save)


# def settings_close():
#     pass


def program_add(window, values, program_list):
    for el in values["current_programs"]:
        if el not in program_list:
            program_list.append(el)
    window.Element(config.keyword_program_list).Update(values=program_list)


def program_delete(window, values, program_list):
    for el in values["program_list"]:
        del program_list[program_list.index(el)]
    window.Element(config.keyword_program_list).Update(values=program_list)
