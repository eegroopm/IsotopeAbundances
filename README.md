IsotopeAbundances
=================

A small Python module that consists of a table of stable isotope abundances. Module may easily be imported and accessed via:  

import IsotopeAbundances as IA  
table = IA.table  

Calculate relative abundances of isotopes.  
e.g., Oxygen (O)  
In[]:  
IA.rel_abundance('O', masses= [17,18], ref_mass= 16)  
Out[]:   
17O/16O    0.000401  
18O/16O    0.002004  
Name: O, dtype: float64  



Requires:
=================
Python
Pandas (numpy)
