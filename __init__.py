"""
Author: Evan Groopman
12/3/2014

Table of stable isotope abundances.

Includes human-readable table created by Frank Stadermann.
"""
import numpy as np
import pandas as pd
import os
_this_dir, _this_filename = os.path.split(__file__)
_DATA_PATH = os.path.join(_this_dir, "", 'IsotopeAbundances.h5')
_EL_PATH = os.path.join(_this_dir, "", 'elements.txt')
table = pd.read_hdf(_DATA_PATH,'table')
#elements = pd.read_hdf(_EL_PATH,'table')
elements = pd.read_csv(_EL_PATH, delimiter=' - ', index_col=0)

def rel_abundance(element,masses=[],ref_mass=None):
    """Return the relative abundance of an isotope or list of isotopes.
    If ref_mass given, returns the ratio of their abundances.
    
    Can enter element as an integer (Z number), Symbol, or Name."""
    if type(element) == str:
        element = element.capitalize() #capitalize first letter only
        print(element)
        index = elements[elements.isin([element])].dropna(how='all').index[0]#return element symbol for feeding into abundance table
        print(index)
        e = elements.loc[index]['Symbol']
    elif type(element) == int:
        e = elements.loc[element]['Symbol']
    else:
        raise ValueError('Not a valid element.')
    
    
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
            try:
                abn.index = [str(i)+e+'/'+str(ref_mass)+e for i in abn.index]
            except AttributeError:
                pass
    elif ref_mass != None:
        print('Please enter an integer reference mass.')
        
    return(abn)