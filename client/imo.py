#!/usr/bin/env python

import os
import sys

EXIT_FAILURE = 1

try:
    import yaml
    import imo.defaults
    import imo.options
    import imo.config
    import imo.machineinfo
except ImportError as e:
    print "Fatal: can not import a required library!"
    print e
    sys.exit(EXIT_FAILURE)

# Parse command line options
options = imo.options.Options()
if options.debug_level > 0:
    print "Options passed: ", options.dump

# Load the config
try:
    config = imo.config.Config(options)
except IOError as e:
    print "Fatal: error loading configuration file!"
    print e
except yaml.YAMLError as e:
    print "Fatal: error parsing configuration file!"
    print e

# Dump the config data structure
if config.debug_level > 0:
    print "Config: ", config.dump

# Initialize machine info object
try:
    machine_info = imo.machineinfo.MachineInfo(config.file)
except IOError as e:
    print "Fatal: error loading machine information file!"
    print e
except yaml.YAMLError as e:
    print "Fatal: error parsing machine information file!"
    print e


# Perform the operation
if options.subcommand == "show":
    print machine_info.show()

elif options.subcommand == "register":
    machine_info.register(config.server)

elif options.subcommand == "update": 
    machine_info.update(config.server)

elif options.subcommand == "delete":
    machine_info.delete(config.server)
