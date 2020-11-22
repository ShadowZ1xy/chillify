import json

from settings import settings_config as config

__settings_template = '{"%s": 20, "%s": 10, "%s": [], "%s": true}' % (
    config.keyword_duration,
    config.keyword_periodicity,
    config.keyword_program_list,
    config.keyword_multimedia_pause
)

def get_settings():
    try:
        with open(config.path_to_json+'settings.json', 'r') as settings_file:
            settings = json.loads(settings_file.read())
    except (json.decoder.JSONDecodeError, IOError, FileNotFoundError):
        settings = __write_standard_json_values()
    return settings


def set_settings(settings):
    with open(config.path_to_json+'settings.json', 'w') as settings_file:
        settings_file.write(json.dumps(settings))


def get_settings_from_gui_then_save(setup):
    program_list = []
    for i in range(setup["program_listbox"].size()):
        program_list.append(setup["program_listbox"].get(i))

    settings_obj = {config.keyword_duration: setup[config.keyword_duration].get(),
                    config.keyword_periodicity: setup[config.keyword_periodicity].get(),
                    config.keyword_program_list: program_list,
                    config.keyword_multimedia_pause: setup[config.keyword_multimedia_pause].get()}
    set_settings(settings_obj)

def __write_standard_json_values():
    with open(config.path_to_json+'settings.json', 'w') as settings_file:
        settings_file.write(__settings_template)
    return json.loads(__settings_template)


