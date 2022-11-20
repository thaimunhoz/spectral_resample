# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:03:35 2022

@author: thain
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.font_manager as font_manager
from spectres import spectres

dataset = pd.read_excel('G:/Outros computadores/Meu modelo Laptop (1)/Documents/Mestrado/BEPE/atmospheric_correction/AC_comparison/PRISMA_04-09/no_glint/ac_comparison_python.xlsx',index_col=0,sheet_name="L1")

#%%

# Informations: https://spectres.readthedocs.io/en/latest/

new_wavs = dataset.index.values #new wavelenght sampling
spec_wavs = dataset.iloc[:,0].values #current wavelenght sampling

# spectral fluxes at the wavelengths specified in the current wavelenght sampling
spec_fluxes = dataset.loc[:,k].values


spec_fluxes_new = spectres(new_wavs, spec_wavs, spec_fluxes, spec_errs=None, fill=None, verbose=True)
    