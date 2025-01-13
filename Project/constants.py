# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:26:29 2024

@author: sande
"""

import numpy as np


modelrun = 800

lammbda  = 3.9*10**(5) *365.25*24*3600           # Strait efficiency Gibraltar & WMed
lammbda2 = 3.9*10**(5) *365.25*24*3600           # Strait efficiency WMed & EMed
heatc    = 0#12.9*10**(-10) *365.25*24*3600      # Heat relaxation constant between atmosphere and boxes
                                                 # Following Table 1 in Scott, Marotzke & Stone, 1999

kappa_conv   = 5*10**(6)*365.25*24*3600                 # Vertical convection flux constant
kappa_mixing = 4*10**(-5)*365.25*24*3600         # Vertical mixing constant
kappa_str    = 4*10**(-4)*365.25*24*3600            # Vertical mixing dependent on density difference 

