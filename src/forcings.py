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
    evap : Evaporation imposed on box; positive is net evaporation (E-(P+R) > 0). 
        Negative is net influx of fresh water (E-(P+R) < 0)

    """

    if Box == 'WMed':
        b = 2*np.pi/(modelrun*4) 
        evap = 1.0 * np.sin(b*i)

        
    elif Box == 'EMed':
        b = 2*np.pi/(modelrun*4) 
        evap = 1.0 * np.sin(b*i)


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


