import json

import config

__settings_template = '{"%s": 20, "%s": 10, "%s": []}' % (
    config.keyword_duration,
    config.keyword_periodicity,
    config.keyword_program_list
)


def __write_standard_json_values():
    with open('settings.json', 'w') as settings_file:
        settings_file.write(__settings_template)
    return json.loads(__settings_template)


def get_settings():
    try:
        with open('settings.json', 'r') as settings_file:
            settings = json.loads(settings_file.read())
    except (json.decoder.JSONDecodeError, IOError, FileNotFoundError):
        settings = __write_standard_json_values()
    return settings


def set_settings(settings):
    with open('settings.json', 'w') as settings_file:
        settings_file.write(json.dumps(settings))
