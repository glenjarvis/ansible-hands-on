"""Data types explanation: YAML -> Python"""

import yaml
import pprint


def yaml_to_python():

    """Demonstrate YAML string parsed to Python"""

    some_string = """
name: Glen Jarvis
sex: Male
title: Senior Developer
hp: [32, 71]
sp: [1, 13]
gold: 423
inventory:
  - A laptop
  - Some code
  - A lot of hope
"""

    some_python = yaml.load(some_string)

    print "YAML -> Python Example"
    print "type(some_string): {0}".format(type(some_string))
    print "type(some_python): {0}".format(type(some_python))

    print "\n\nYAML (really string in Python):"
    pprint.pprint(some_string)
    print "\n\nPython:"
    pprint.pprint(some_python)

if __name__ == '__main__':
    yaml_to_python()
