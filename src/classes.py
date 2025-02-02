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
    Requires S0 and T0 which are the initial values of salinity and temperature
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity [-]
    Temp  :  NumPy array with size of modelrun representing Box temperature [deg C]
    Rho  :  Density calculated given the box temperature and salinity through the linear equation of state [kg/m3]
    HorConnection  :  List of boxes connected horizontally
    VerConnection  : List of boxes connected vertically
    Area  :  int, surface area of box [m2]
    dT  :  float, change of temperature at certain time step      
    dS  :  float, change of salinity at certain time step          
    
    
    """    


    def __init__(self, S0, T0):
        self.Name       = 'Atlantic'
        self.Level      = 0             # 0 = Surface, 1 = Intermediate, 2 = Deep 
        self.Number     = 0
        self.Salinity   = np.zeros((modelrun,1)) 
        self.Temp       = np.zeros((modelrun,1))  
        self.Rho        = np.zeros((modelrun,1)) 
        self.Salinity[0] = S0
        self.Temp[0]     = T0
        self.Rho[0]     = CalculateDensity(S0,T0) 
        self.HorConnection = ['WMed']
        self.VerConnection = [] 
        self.Area      = 0 # Set area to 0 because fresh water budget over Atlantic is not important
        self.dT        = 0 
        self.dS        = 0

class WMedSurface:
    
    """
    Box representing WMed Surface 
    Requires S0 and T0 which are the initial values of salinity and temperature
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity [-]
    Temp  :  NumPy array with size of modelrun representing Box temperature [deg C]
    Rho  :  Density calculated given the box temperature and salinity through the linear equation of state [kg/m3]
    HorConnection  :  List of boxes connected horizontally
    VerConnection  : List of boxes connected vertically
    Area  :  int, surface area of box [m2]
    dT  :  float, change of temperature at certain time step      
    dS  :  float, change of salinity at certain time step          
    
    
    """    
        
    def __init__(self, S0, T0):
        self.Name       = 'WMed'
        self.Number     = 1
        self.Level      = 0             # 0 = Surface, 1 = Intermediate, 2 = Deep 
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
    
    
    """
    Box representing WMed Intermediate 
    Requires S0 and T0 which are the initial values of salinity and temperature
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity [-]
    Temp  :  NumPy array with size of modelrun representing Box temperature [deg C]
    Rho  :  Density calculated given the box temperature and salinity through the linear equation of state [kg/m3]
    HorConnection  :  List of boxes connected horizontally
    VerConnection  : List of boxes connected vertically
    Area  :  int, surface area of box [m2]
    dT  :  float, change of temperature at certain time step      
    dS  :  float, change of salinity at certain time step          
    
    
    """    
    
    def __init__(self, S0, T0):
        self.Name       = 'WMedI' 
        self.Level      = 1             # 0 = Surface, 1 = Intermediate, 2 = Deep 
        self.Number     = 3             # Integer number in fluxes array
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
    
    
    """
    Box representing EMed Surface 
    Requires S0 and T0 which are the initial values of salinity and temperature
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity [-]
    Temp  :  NumPy array with size of modelrun representing Box temperature [deg C]
    Rho  :  Density calculated given the box temperature and salinity through the linear equation of state [kg/m3]
    HorConnection  :  List of boxes connected horizontally
    VerConnection  : List of boxes connected vertically
    Area  :  int, surface area of box [m2]
    dT  :  float, change of temperature at certain time step      
    dS  :  float, change of salinity at certain time step          
    
    
    """    
    
    def __init__(self, S0, T0):
        self.Name       = 'EMed'
        self.Level      = 0             # 0 = Surface, 1 = Intermediate, 2 = Deep 
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
    
    
    """
    Box representing EMed Intermediate
    Requires S0 and T0 which are the initial values of salinity and temperature
    
    Attributes
    ----------
    Name  :  str
        Name of the Box
    Number  :  int
        Number of the box
    Salinity  : NumPy array with size of modelrun representing Box salinity [-]
    Temp  :  NumPy array with size of modelrun representing Box temperature [deg C]
    Rho  :  Density calculated given the box temperature and salinity through the linear equation of state [kg/m3]
    HorConnection  :  List of boxes connected horizontally
    VerConnection  : List of boxes connected vertically
    Area  :  int, surface area of box [m2]
    dT  :  float, change of temperature at certain time step      
    dS  :  float, change of salinity at certain time step          
    
    
    """    
    
    def __init__(self, S0, T0):
        self.Name       = 'EMedI'
        self.Level      = 1             # 0 = Surface, 1 = Intermediate, 2 = Deep 
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

  
             