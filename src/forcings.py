# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:59:13 2024

@author: sande
"""


import numpy as np
from constants import modelrun

def Evapor(i,Box):
    """
    

    Parameters
    ----------
    i : int, time after t0 

    Returns
    -------
    evap : Evaporation imposed on box

    """

    if Box == 'WMed':
        evap = 0.6
        
    elif Box == 'EMed':
        evap = 0.6

    else:
        evap = 0

    
    return evap

def AirTemp(i, Box): 
    """
    

    Parameters
    ----------
    i : int, time after t0 

    Returns
    -------
    evap : Air temperature imposed on atmosphere above box

    """

    if Box == 'WMed':
        T_air = 14
        
    elif Box == 'EMed':
        T_air = 14

    else:
        T_air = 14

    
    return T_air

def VaryingAtlantic(i):
    
    """"
    Functions that changes the water properties of the Atlantic; 
    For now, no changes are imposed
    """
    
    return 0 


