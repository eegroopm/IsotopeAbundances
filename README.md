IsotopeAbundances
=================

A small Python module that consists of a table of stable isotope abundances. Module may easily be imported and accessed via:

import IsotopeAbundances as IA  

table = IA.table\n

Calculate relative abundances of isotopes.\n
e.g., Oxygen (O)\n
In[]:\n
IA.rel_abundance('O', masses= [17,18], ref_mass= 16)\n
Out[]: \n
17O/16O    0.000401\n
18O/16O    0.002004\n
Name: O, dtype: float64\n



Requires:
=================
Python
Pandas (numpy)
