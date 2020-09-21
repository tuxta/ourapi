from configparser import ConfigParser


class Definitions:
    def __init__(self, definitions_file):
        self.definitions_file = definitions_file
        self.definitions_dict = {}

    def load(self):
        self.definitions_dict = {}
        with open(self.definitions_file) as file:
            parser = ConfigParser()
            parser.read_file(file)
            self.definitions_dict = {}
            parser = ConfigParser()
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

