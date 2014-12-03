"""
Author: Evan Groopman
12/3/2014

Table of stable isotope abundances.

Includes human-readable table created by Frank Stadermann.
"""

import pandas as pd
import os
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "", 'IsotopeAbundances.h5')
table = pd.read_hdf(DATA_PATH,'table')