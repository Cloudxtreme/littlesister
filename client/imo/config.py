""" Config operations module """

import imo.defaults
import yaml

class Config:
    """ Config file operations class """

    _config = None

    def __init__(self, options):
        """ Loads and parses the config
            Command line options have higher priority
            than config statements in case of conflict.
        """
        config_path = imo.defaults.config_prefix + \
                      imo.defaults.config_file
        # Overwrite config file path if set in options
        if options.config_path:
            config_path = options.config_path
        self._config = yaml.load(file(config_path, 'r'))

        # !!! TODO: Check the config against schema

        # Overwrite debug level if set in options
        if isinstance(options.debug_level, int):
            self._config['debug_level'] = options.debug_level

        # Overwrite machineinfo file path if set in options
        if options.file:
            self._config['file'] = options.file

    @property
    def file(self):
        """ Returns path to the machine info file """
        if self._config.has_key('file'):
            return self._config['file']
        else:
            return None

    @property
    def server(self):
        """ Returns the information gathering server address """
        if self._config.has_key('server'):
            return self._config['server']
        else:
            return None

    @property
    def debug_level(self):
        """ Returns debug level """
        if self._config.has_key('debug_level'):
            return self._config['debug_level']
        else:
            return None

    @property
    def dump(self):
        """ Dumps the data structure associated with config for debug """
        return self._config
