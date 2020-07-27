# python 3

# imports

import sys
sys.path.insert(0, '/home/ubuntu/eds/lib/')
import eds # Edge Data Store functions


eds.remove_container("rpi_core", "rpi_core")
eds.remove_type("rpi_core")
