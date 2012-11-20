""" Command line options handling """

import sys
import argparse

class Options:
    """ Command line options handling class """

    _args = None

    def __init__(self):
        parser = argparse.ArgumentParser(
                   description="littlesister, a host documenting tool for small networks",
                   formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-f', '--file', help='path to the machine information file', type=str, action='store')
        parser.add_argument('-c', '--config', help='path to the config file', type=str, action='store')
        parser.add_argument('-d', '--debug-level', help='values greater than 0 enable debug messages', type=int, action='store')
        parser.add_argument('-v', '--verbose', help='increase message verbosity level', action='store_true')
        parser.add_argument('-V', '--version', help='show version and exit', action='version', version=self._version_message)

        subparsers = parser.add_subparsers(help='machine info operations', dest='subcommand')

        parser_show = subparsers.add_parser('show', help='show this machine information')
        parser_show.add_argument('--raw', help='supress dynamic variable substitution', action='store_true')

        parser_register = subparsers.add_parser('register', help='register this machine on the server')
        parser_register.add_argument('--server', type=str, help='server to register on', action='store')

        parser_update = subparsers.add_parser('update', help='update this machine information on the server')

        parser_delete = subparsers.add_parser('delete', help='tell the server to forget this machine')

        # Print help if no arguments given
        if len(sys.argv)==1:
            parser.print_help()
            sys.exit(1)
        
        self._args = parser.parse_args()

    @property
    def file(self):
        """ Returns --file option value """
        return self._args.file

    @property
    def config_path(self):
        """ Returns --config option value """
        return self._args.config

    @property
    def debug_level(self):
        """ Returns --debug-level option value """
        return self._args.debug_level

    @property
    def verbose(self):
        """ Returns --verbose option value """
        return self._args.verbose

    @property
    def version(self):
        return self._args.version

    @property
    def subcommand(self):
        return self._args.subcommand

    @property
    def dump(self):
        return self._args

    _version_message = """littlesister 0.0.1

Copyright (C) 2012 SO(3) Group

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law. """
