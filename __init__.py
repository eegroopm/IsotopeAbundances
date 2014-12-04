"""
Author: Evan Groopman
12/3/2014

Table of stable isotope abundances.

Includes human-readable table created by Frank Stadermann.
"""
import numpy as np
import pandas as pd
import os
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "", 'IsotopeAbundances.h5')
table = pd.read_hdf(DATA_PATH,'table')

def rel_abundance(element,masses=[],ref_mass=None):
    """Return the relative abundance of an isotope or list of isotopes.
    If ref_mass given, returns the ratio of their abundances."""
    e = element.capitalize() #capitalize first letter only
    if masses == []:
        return(table[e].dropna())
        
    if type(masses) == int or len(masses) == 1: #single mass
        if type(masses) == int:
            mass = masses
        elif type(masses) == list:
            mass = masses[0]
        abn = table[e].loc[mass]
        if np.isnan(abn):
            msg='Mass %i is not valid.\nTry mass(es) %s for %s instead.' % (mass,
            str(list(table[e].dropna().index)),e)
            raise ValueError(msg)
    
    elif type(masses) == list or type(masses) == np.ndarray:
        masses.sort() #reorder numerically
        abn = table[e].loc[masses]
        if np.isnan(abn).any():
            invalid = list(abn[np.isnan(abn)].index)
            print('Warning: These masses are not valid: %s!' % str(invalid))
    
    if type(ref_mass) == int:
        ref_abn = table[e].loc[ref_mass]
        if np.isnan(ref_abn):
            msg='Mass %i is not valid.\nTry mass(es) %s for %s instead.' % (ref_mass,
            str(list(table[e].dropna().index)),e)
            raise ValueError(msg)
        else:
            abn = abn/ref_abn
            #remake indices
            abn.index = [str(i)+e+'/'+str(ref_mass)+e for i in abn.index]
    else:
        print('Please enter an integer reference mass.')
        
    return(abn)