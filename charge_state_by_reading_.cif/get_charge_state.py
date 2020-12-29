#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:54:26 2019

@author: Hemanta
"""
'''
Get charge state by using Bond valance analyzer in pymatgen and store them in pandas dataframe
As a single element can have different values in multiple compounds, It will be in different rows
'''

import time
start = time.time()
from pymatgen import Structure
from collections import defaultdict
from pymatgen.analysis.bond_valence import BVAnalyzer
import pandas as pd

def get_valances():
    from pymatgen.analysis.bond_valence import BVAnalyzer
    val = BVAnalyzer()
    return val.get_valences(structure_from_cif)

#read the list of file containing ".cif files"
#you can just pass a single .cif file if needed
    
file = open("file_data.dat", "r")
charge_state_dict = defaultdict(dict)
empty_df = pd.DataFrame(columns = [i for i in range(100)])
for lines in file:
        try:
                line = lines.split()[0]
                structure_from_cif = Structure.from_file(str(line))
                val = BVAnalyzer()
                y = val.get_valences(structure_from_cif)
                z = structure_from_cif.atomic_numbers
                comp = structure_from_cif.composition
                element_in_comp = structure_from_cif.species
                element_in_comp = [str(element_in_comp[i])+str(i) for i in range(len(element_in_comp))]
	        #if you want to get all the elements at the output one can do
                #element_in_comp=[str(element_in_comp[i])+str(i) for i in range(len(element_in_comp))]

                #element_in_comp = [ str(i) for i in comp]
                
                for k, v in zip(element_in_comp, y):
                        charge_state_dict[str(line)][k] = v
        except:
                pass
            
df = pd.DataFrame.from_dict(charge_state_dict).T

writer = pd.ExcelWriter('charge_state_df_element.xlsx',
                           engine='xlsxwriter',
                            options={'strings_to_urls': False})
df.to_excel(writer,  sheet_name = 'Sheet1' , na_rep = 'Nan')
writer.save()
end = time.time()
print("time taken is", end - start)


