# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:59:09 2024

@author: sande
"""

import numpy as np
from constants import modelrun



def CalculateDensity(S,T):
    """
    
    Parameters
    ----------
    S : Input salinity

    T : TYPE
        DESCRIPTION.
        
    Constants
    ----------        
    T_0 = 10 degrees
    S_0 = 35 
           

    Returns
    -------
    Rho : TYPE
        DESCRIPTION.

    """
    T_0        = 10
    S_0        = 35 
    Rho        = (-0.15 *(T-T_0) + 0.78 *(S-S_0)) + 1027 # Linear eq. of state 
    return Rho

class AtlanticSurface:

    """
    Box representing Atlantic Surface 
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity
    Temp  :  NumPy array with size of modelrun representing Box temperature
        
    
    
    """    


    def __init__(self, S0, T0):
        self.Name       = 'Atlantic'

        self.Number     = 0
        self.Salinity   = np.ones((modelrun,1)) * S0 # keep salinity constant
        self.Temp       = np.ones((modelrun,1)) * T0 # keep temperature constant 
        Rho             = CalculateDensity(S0,T0)
        self.Rho        = np.ones((modelrun,1)) * Rho # As a result, keep rho constant
        self.HorConnection = ['WMed']
        self.VerConnection = [] 
        self.Area      = 0 # Set area to 0 because fresh water budget over Atlantic is not important
        self.dT        = 0 
        self.dS        = 0

class WMedSurface:
        
    def __init__(self, S0, T0):
        self.Name       = 'WMed'
        self.Number     = 1
        self.Area       = 1*10**12 #0.8475*10**12
        self.Depth      = 500 
        self.Volume     = self.Area * self.Depth 
        self.Salinity   = np.zeros((modelrun,1))
        self.Temp       = np.zeros((modelrun,1))
        self.Rho        = np.zeros((modelrun,1))         
        self.Salinity[0] = S0
        self.Temp[0]     = T0
        self.Rho[0]      = CalculateDensity(S0,T0)
        self.HorConnection = ['Atlantic', 'EMed']
        self.VerConnection = ['WMedI'] 
        self.dT        = 0 
        self.dS        = 0
  
class WMedIntermediate:
    
    def __init__(self, S0, T0):
        self.Name       = 'WMedI'
        self.Number     = 3
        self.Area       = 0.8475*10**12 ##0.8475*10**12
        self.Depth      = 1000 
        self.Volume     = self.Area * self.Depth 
        self.Salinity   = np.zeros((modelrun,1))
        self.Temp       = np.zeros((modelrun,1))
        self.Rho        = np.zeros((modelrun,1))         
        self.Salinity[0] = S0
        self.Temp[0]     = T0
        self.Rho[0]      = CalculateDensity(S0,T0)
        self.HorConnection = []
        self.VerConnection = ['WMed'] 
        self.dT        = 0 
        self.dS        = 0
        
       
class EMedSurface:
    
    def __init__(self, S0, T0):
        self.Name       = 'EMed'

        self.Number     = 2
        self.Area       = 1*10**12# 1.6963*10**12
        self.Depth      = 500 
        self.Volume     = self.Area * self.Depth 
        self.Salinity   = np.zeros((modelrun,1))
        self.Temp       = np.zeros((modelrun,1))
        self.Rho        = np.zeros((modelrun,1))        
        self.Salinity[0] = S0
        self.Temp[0]     = T0
        self.Rho[0]      = CalculateDensity(S0,T0)
        self.HorConnection = ['WMed']
        self.VerConnection = ['EMedI'] 
        self.dT        = 0 
        self.dS        = 0
        
class EMedIntermediate:
    
    def __init__(self, S0, T0):
        self.Name       = 'EMedI'

        self.Number     = 4
        self.Area       = 1.6963*10**12##1.6963*10**12
        self.Depth      = 1000 
        self.Volume     = self.Area * self.Depth 
        self.Salinity   = np.zeros((modelrun,1))
        self.Temp       = np.zeros((modelrun,1))
        self.Rho        = np.zeros((modelrun,1))        
        self.Salinity[0] = S0
        self.Temp[0]     = T0
        self.Rho[0]      = CalculateDensity(S0,T0)
        self.HorConnection = []
        self.VerConnection = ['EMed'] 
        self.dT        = 0 
        self.dS        = 0

  
             