""" littlesister machineinfo file operations """

import yaml

class MachineInfo:
    """ machineinfo file operations class """
    _machineinfo = None

    def __init__(self, machineinfo_file):
        """ Loads and parses the machineinfo file """
        self._machineinfo = yaml.load(file(machineinfo_file, 'r'))

        # !!! TODO: Check the config against schema

    def register(self, server_address):
        """ Registers the machine on the server.
            The UUID obtained from the server is written to 
            the machineinfo file.
            If machineinfo file doesn't exist,
            creates a template too.
        """
        pass

    def update(self, server_address):
        """ Sends current version of the machineinfo file
            to the server """
        pass

    def delete(self, server_address):
        """ Tells server to forget this machine """
        pass

    def show(self):
        """ Performs dynamic variable substitution and
            dumps the machineinfo to stdout.
            We are going to implement this first to
            make the software useful without a server. """

        return yaml.dump(self._machineinfo, default_flow_style=False)
        # PyYAML dumper output looks, uhm, not human friendly at all.
        # Not nice at the very least.
        # This should be replaced with a simple recursive formatter
        # that is capable of doing proper indentation and stuff

        
