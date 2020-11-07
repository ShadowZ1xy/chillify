import json

__settings_template = '{"duration": 20, "periodicity": 10, "program_list": []}'


def __write_standard_json_values(file):
    file.write(__settings_template)


def get_settings():
    with open('settings.json', 'w') as settings_file:
        try:
            settings = json.loads(settings_file.read())
        except (json.decoder.JSONDecodeError, IOError):
            __write_standard_json_values(settings_file)
            settings = json.loads(__settings_template)
    return settings


def set_settings(settings):
    with open('settings.json', 'w') as settings_file:
        settings_file.write(json.dumps(settings))
