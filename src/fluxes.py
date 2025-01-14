# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:49:24 2024

@author: sande
"""

import numpy as np
from constants import kappa_conv, kappa_mixing, kappa_str

def Convection(Box1, Box2,i):
    
    """ 
    
    If density in upper box exceeds density in lower box, convection occurs.
    
    Parameters
    ----------
    Box1 : Upper box
    
    Box2 : Lower box

    Returns
    -------
    

    """
    q = 0 # Set q to zero so function always returns something, either 0 or other value of q
    
    if Box1.Name in Box2.VerConnection: # Or the other way around, should not matter    
    
        if Box1.Rho[i] >= Box2.Rho[i]:
        
            q =  kappa_conv*(Box1.Rho[i]-Box2.Rho[i]) 
            
    return q
   
  
   
def DensityDrivenHorizontalFlux(Box1, Box2,lammbda,i):
    """
    

    Parameters
    ----------

    Returns
    -------
    None.

    """
    if Box1.Name in Box2.HorConnection:
    
        if Box1.Rho[i] > Box2.Rho[i]: # Flow is from Box1 to Box2 as density in Box1 exceeds density in Box2
        
            if Box1.Name == 'Atlantic' or 'WMed' and Box2.Name == 'Atlantic' or 'WMed': 
                q = lammbda * (np.sqrt(Box1.Rho[i] - Box2.Rho[i])) # Box1 > Box2 

            if Box1.Name == 'Atlantic' or 'WMedI' and Box2.Name == 'Atlantic' or 'WMedI': 
                q = lammbda * (np.sqrt(Box1.Rho[i] - Box2.Rho[i])) # Box1 > Box2 

            else:
                q = lammbda * (Box1.Rho[i] - Box2.Rho[i])  

            return q
        
        
        else:
            q = 0
            return q
    else:
        q = 0
        return q

    
def VerticalMixing(Box1, Box2, i):
    
    """
    Box1 == Upper box
    Box2 == Lower box
    """
    if Box1.Name in Box2.VerConnection: 

        if Box1.Rho[i] > Box2.Rho[i]:
    
            return abs(max(kappa_mixing, kappa_str*(Box1.Rho[i] - Box2.Rho[i]) + kappa_mixing) * 2 * Box1.Area /(Box1.Depth + Box2.Depth))
    
        else: 
            return abs( max(kappa_mixing, kappa_str*(Box1.Rho[i] - Box2.Rho[i]) + kappa_mixing) * 2 * Box1.Area /(Box1.Depth + Box2.Depth))

    else:
        return 0 
    
def dTdt(Box1,Box2,q,i):   
    
    """
    
    Parameters
    ----------
    Box1  : First Box with its properties.
    Box2  : Second Box with its properties.
    q     : Flow between Box1 and Box2 as driven by density differences; absolute value is taken here

    Returns
    -------
    Change in temperature of Box1 as a result of flow between Box1 and Box2

    """
    
   
    if Box2.Name == 'Atlantic':
        return 0 # Assumes no change in temperature for the Atlantic ocean as result of flow 
    
    else:   
        return (1/Box2.Volume)*abs(q)*(Box1.Temp[i]-Box2.Temp[i])
    

def dSdt(Box1,Box2,q,i):
    
        
    """    

    Parameters
    ----------
    Box1  : First Box with its properties.
    Box2  : Second Box with its properties.
    q     : Flow between Box1 and Box2 as driven by density differences; absolute value is taken here
  
    
    Returns
    -------
    Change in salinity of Box1 as a result of flow between Box1 and Box2

    """
    

    
    if Box2.Name == 'Atlantic':
        return 0  # Assumes no change in salinity for the Atlantic ocean as result of flow
    
    else:
        return (1/Box2.Volume)*(abs(q)*(Box1.Salinity[i]-Box2.Salinity[i]))
    
               



