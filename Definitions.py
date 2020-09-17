from configparser import SafeConfigParser
import os


class Definitions:
    definitions_file = ''
    definitions_dict = {}

    def __init__(self, definitions_file):
        self.definitions_file = definitions_file
        self.load()
        # load the file into dict

    def reload(self):
        print('Reloading definitions file: ' + self.definitions_file)
        self.definitions_dict = {}
        self.load()

    def load(self):
        print('Loading definitions file: ' + self.definitions_file)
        parser = SafeConfigParser()
        # parser.read(os.path.join(os.path.dirname(__file__), self.definitions_file))
        parser.read(self.definitions_file)

        # iterate over each section in the config file
        for section_name in parser.sections():
            # create a temporary dictionary to store sections
            tmp_dict = {}

            for name, value in parser.items(section_name):
                if 'args' == name:

                    if 'None' != value:
                        tmp_dict[name] = value.split(',')
                    else:
                        tmp_dict[name] = ''
                else:
                    tmp_dict[name] = value

            self.definitions_dict[section_name] = tmp_dict

        print(self.definitions_dict)

