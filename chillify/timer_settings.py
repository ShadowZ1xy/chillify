import json

import timer_config

__settings_template = '{"%s": 20, "%s": 10, "%s": [], "%s": true}' % (
    timer_config.keyword_duration,
    timer_config.keyword_periodicity,
    timer_config.keyword_program_list,
    timer_config.keyword_multimedia_pause
)


def get_settings():
    try:
        with open(timer_config.path_to_json + 'settings.json', 'r') as settings_file:
            settings = json.loads(settings_file.read())
    except (json.decoder.JSONDecodeError, IOError, FileNotFoundError):
        settings = __write_standard_json_values()
    return settings


def __write_standard_json_values():
    with open(timer_config.path_to_json + 'settings.json', 'w') as settings_file:
        settings_file.write(__settings_template)
    return json.loads(__settings_template)
