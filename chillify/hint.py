import json
import os
import random
import sys
import codecs

path = os.path.dirname(sys.argv[0]) + "\\"


def get_random_hint():
    hint_list = __get_hints()["hint"]
    random_hint = random.choice(hint_list)
    return random_hint


def __get_hints():
    try:
        with codecs.open(path + 'hints.json', 'r', "utf-8") as hint_file:
            hints = json.loads(hint_file.read())
    except (json.decoder.JSONDecodeError, IOError, FileNotFoundError):
        hints = {"hint": ["Пришло время отдыха."]}
    return hints
