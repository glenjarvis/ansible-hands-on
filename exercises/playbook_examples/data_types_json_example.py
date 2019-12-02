"""Data types explanation: Python <-> JSON"""

import json
import pprint


def python_to_json():

    """Demonstrate Python converted to JSON string"""

    some_python = {
        'minecraft_obsidian': 423,
        'hp': [32, 71],
        'inventory': ['A laptop', 'Some code', 'A lot of hope'],
        'name': 'Glen Jarvis',
        'sex': 'Male',
        'sp': [1, 13],
        'title': 'Senior Developer'
    }

    some_json = json.dumps(some_python)

    print "Python -> JSON Example"
    print "type(some_python): {0}".format(type(some_python))
    print "type(some_json): {0}".format(type(some_json))
    print "\n\nPython:"
    pprint.pprint(some_python)
    print "\n\nJSON:"
    pprint.pprint(some_json)


def json_to_python():

    """Demonstrate json string parsed to Python"""

    some_string = '{"apple": 1, "pear": 2}'
    some_python = json.loads(some_string)

    print "JSON Example -> Python Example"
    print "type(some_string): {0}".format(type(some_string))
    print "type(some_python): {0}".format(type(some_python))

    print "\n\nJSON (really string in Python):"
    pprint.pprint(some_string)
    print "\n\nPython:"
    pprint.pprint(some_python)

if __name__ == '__main__':
    python_to_json()
    # json_to_python()
