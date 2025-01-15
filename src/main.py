# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 08:28:51 2024

@author: SanderKeulers
"""

       
import warnings
warnings.filterwarnings("ignore")

from classes import (AtlanticSurface, 
                    WMedSurface, WMedIntermediate, 
                    EMedSurface, EMedIntermediate,
                    CalculateDensity
                    )

from fluxes import (DensityDrivenHorizontalFlux,
                    Convection,
                    VerticalMixing, 
                    dTdt, dSdt
                    )

from forcings import (Evapor,
                      VaryingAtlantic,
                      AirTemp
                      ) 

from constants import (heatc, modelrun, lammbda, lammbda2, dt) 

import numpy as np
    
def Main(config):
    """
    

    Parameters
    ----------
    config : int, either 1 or 2; defines set-up of model.

    Returns
    -------
    t : NumPy array of int, determines time 
    Boxes : Dictionary of defined boxes, including their properties.
    Fluxes : NumPy array of fluxes between boxes .
    FreshWaterBudget : NumPy array of freshwater budget over box
    AirTemperature : NumPy array of air temperature over box 

    """
    
    t = np.zeros((int(modelrun/dt),1))
    
    if config == 1:
  
        Boxes = {
            'Atlantic' : AtlanticSurface(34, 11),
            'WMed' : WMedSurface(34, 11)        
            }
    
        Boxes['WMed'].Area   = 2*10**12
        Fluxes               = np.zeros((modelrun,len(Boxes),len(Boxes)))
        Mixing               = np.zeros((modelrun,len(Boxes),len(Boxes)))
        FreshWaterBudget     = np.zeros((modelrun,len(Boxes)))
        AirTemperature       = np.zeros((modelrun,len(Boxes)))
        
        for i in range(0,len(t)-1): # Iterate over predefined time
            
            t[i+1] = t[i] + dt             
                    
            Boxes['Atlantic'].Salinity[i] = Boxes['Atlantic'].Salinity[i] + VaryingAtlantic(i) # keep Atlantic constant or not
            Boxes['Atlantic'].Temp[i] = Boxes['Atlantic'].Temp[i] + VaryingAtlantic(i)         # keep Atlantic constant or not 
                    
            for Box in Boxes: # Loop over all boxes
                Boxes[Box].Rho[i] = CalculateDensity(Boxes[Box].Salinity[i], Boxes[Box].Temp[i]) # Calculate density
                FreshWaterBudget[i,Boxes[Box].Number] = Evapor(i,Boxes[Box].Name)*Boxes[Box].Area 
                AirTemperature[i, Boxes[Box].Number] = AirTemp(i, Boxes[Box].Name)     
             
            #%% Density driven horizontal fluxes and convection     
            
            for Box1 in Boxes:
                for Box2 in Boxes: 
                    
                    if Box1 in ['WMed','EMed'] and Box2 in ['EMed','WMed']:
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += DensityDrivenHorizontalFlux(Boxes[Box1], Boxes[Box2], lammbda2, i)
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += Convection(Boxes[Box1], Boxes[Box2], i)
                        Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number] += VerticalMixing(Boxes[Box1],Boxes[Box2],i)
                    else: 
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += DensityDrivenHorizontalFlux(Boxes[Box1], Boxes[Box2], lammbda, i)
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += Convection(Boxes[Box1], Boxes[Box2], i)
                        Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number] += VerticalMixing(Boxes[Box1],Boxes[Box2],i)
            
            #%% Compensating fluxes           
           
            Fluxes[i,Boxes['Atlantic'].Number,Boxes['WMed'].Number] = ((FreshWaterBudget[i,Boxes['WMed'].Number]>0)*FreshWaterBudget[i,Boxes['WMed'].Number]
                                                                  + np.sum(Fluxes[i,Boxes['WMed'].Number,:]) 
                                                                  - np.sum(Fluxes[i, :,Boxes['WMed'].Number]))  
                       
            #%% dTdt and dSdt 
            
            for Box1 in Boxes: 
                for Box2 in Boxes:                 
                    Boxes[Box1].dT += dTdt(Boxes[Box2], Boxes[Box1], Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] + Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number],i)*dt                          
                    Boxes[Box1].dS += dSdt(Boxes[Box2], Boxes[Box1], Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] + Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number],i)*dt
            
            for Box1 in Boxes:     
                if Box1 in ['WMed','EMed']:
                    Boxes[Box1].Temp[i+1]          = Boxes[Box1].Temp[i] + heatc*(AirTemperature[i,Boxes[Box1].Number]-Boxes[Box1].Temp[i]) + Boxes[Box1].dT
                    Boxes[Box1].Salinity[i+1]      = Boxes[Box1].Salinity[i] + FreshWaterBudget[i,Boxes[Box1].Number]*35/Boxes[Box1].Volume + Boxes[Box1].dS
                    Boxes[Box1].dT = 0
                    Boxes[Box1].dS = 0
                else: 
                    Boxes[Box1].Temp[i+1]          = Boxes[Box1].Temp[i] + Boxes[Box1].dT
                    Boxes[Box1].Salinity[i+1]      = Boxes[Box1].Salinity[i] + Boxes[Box1].dS
                    Boxes[Box1].dT = 0
                    Boxes[Box1].dS = 0     
             
    
        return t, Boxes, Fluxes, FreshWaterBudget, AirTemperature
    
    if config == 0 :
           
        Boxes = {
            'Atlantic' : AtlanticSurface(34, 11),
            'WMed' : WMedSurface(34, 11),
            'EMed' : EMedSurface(34, 11),
         
            }
    
        Fluxes               = np.zeros((modelrun,len(Boxes),len(Boxes)))
        Mixing               = np.zeros((modelrun,len(Boxes),len(Boxes)))
        FreshWaterBudget     = np.zeros((modelrun,len(Boxes)))
        AirTemperature       = np.zeros((modelrun,len(Boxes)))
        
        for i in range(0,len(t)-1): # Iterate over predefined time 
            
            t[i+1] = t[i] + dt             
                    
            Boxes['Atlantic'].Salinity[i] = Boxes['Atlantic'].Salinity[i] + VaryingAtlantic(i) # keep Atlantic constant or not
            Boxes['Atlantic'].Temp[i] = Boxes['Atlantic'].Temp[i] + VaryingAtlantic(i) # keep Atlantic constant or not 
                    
            for Box in Boxes:
                Boxes[Box].Rho[i] = CalculateDensity(Boxes[Box].Salinity[i], Boxes[Box].Temp[i])
                FreshWaterBudget[i,Boxes[Box].Number] = Evapor(i,Boxes[Box].Name)*Boxes[Box].Area 
                AirTemperature[i, Boxes[Box].Number] = AirTemp(i, Boxes[Box].Name)     
             
            #%% Density driven horizontal fluxes and convection     
            
            for Box1 in Boxes:
                for Box2 in Boxes: 
                    
                    if Box1 in ['WMed','EMed'] and Box2 in ['EMed','WMed']:
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += DensityDrivenHorizontalFlux(Boxes[Box1], Boxes[Box2], lammbda2, i)
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += Convection(Boxes[Box1], Boxes[Box2], i)
                        Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number] += VerticalMixing(Boxes[Box1],Boxes[Box2],i)
                    else: 
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += DensityDrivenHorizontalFlux(Boxes[Box1], Boxes[Box2], lammbda, i)
                        Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] += Convection(Boxes[Box1], Boxes[Box2], i)
                        Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number] += VerticalMixing(Boxes[Box1],Boxes[Box2],i)
            
            #%% Compensating fluxes
            
            Fluxes[i,Boxes['WMed'].Number,Boxes['EMed'].Number] = ((FreshWaterBudget[i,Boxes['EMed'].Number]>0)*FreshWaterBudget[i,Boxes['EMed'].Number]
                                                                  + np.sum(Fluxes[i,Boxes['EMed'].Number,:]))             
            
            Fluxes[i,Boxes['Atlantic'].Number,Boxes['WMed'].Number] = ((FreshWaterBudget[i,Boxes['WMed'].Number]>0)*FreshWaterBudget[i,Boxes['WMed'].Number]
                                                                  + np.sum(Fluxes[i,Boxes['WMed'].Number,:]) 
                                                                  - np.sum(Fluxes[i, :,Boxes['WMed'].Number]))  
            
           
            #%% dTdt and dSdt 
            for Box1 in Boxes: 
                for Box2 in Boxes:                 
                    Boxes[Box1].dT += dTdt(Boxes[Box2], Boxes[Box1], Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] + Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number],i)*dt                          
                    Boxes[Box1].dS += dSdt(Boxes[Box2], Boxes[Box1], Fluxes[i,Boxes[Box1].Number,Boxes[Box2].Number] + Mixing[i,Boxes[Box1].Number,Boxes[Box2].Number],i)*dt
            
            for Box1 in Boxes:     
                if Box1 in ['WMed','EMed']:
                    Boxes[Box1].Temp[i+1]          = Boxes[Box1].Temp[i] + heatc*(AirTemperature[i,Boxes[Box1].Number]-Boxes[Box1].Temp[i]) + Boxes[Box1].dT
                    Boxes[Box1].Salinity[i+1]      = Boxes[Box1].Salinity[i] + FreshWaterBudget[i,Boxes[Box1].Number]*35/Boxes[Box1].Volume + Boxes[Box1].dS
                    Boxes[Box1].dT = 0
                    Boxes[Box1].dS = 0
                else: 
                    Boxes[Box1].Temp[i+1]          = Boxes[Box1].Temp[i] + Boxes[Box1].dT
                    Boxes[Box1].Salinity[i+1]      = Boxes[Box1].Salinity[i] + Boxes[Box1].dS
                    Boxes[Box1].dT = 0
                    Boxes[Box1].dS = 0
                    
        return t, Boxes, Fluxes, FreshWaterBudget, AirTemperature
    