# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:46:10 2024

@author: sande
"""

import matplotlib.pyplot as plt
import numpy as np
from main import Main 

fig, axes = plt.subplots(2,2)
fig.set_figheight(10)
fig.set_figwidth(18)


for i in range(0,2):
    
    ax = axes[0,i]
    
    if i ==1:
        t, Boxes, Fluxes, FreshWaterBudget, AirTemperature = Main(i) 
        ax.set_title('Salinity of Atlantic and Mediterranean (1 box setup)', weight='bold')
        
        lns1 = ax.plot(t,Boxes['Atlantic'].Salinity,color='tab:blue',label='$S_{A}$')
        lns2 = ax.plot(t,Boxes['WMed'].Salinity,color='tab:green',label='$S_{WMed}$')

        
        ax.set_ylim(33.5,41)
        ax.set_xticklabels([])

        lns = lns1+lns2
        labs = [l.get_label()    for l in lns]
        ax.legend(lns, labs, loc=4)
        
        
        ax2 = axes[1,i]
        ax3 = ax2.twinx()
        ln1 = ax2.plot(t[:-1],Fluxes[:,Boxes['Atlantic'].Number,Boxes['WMed'].Number][:-1]/(3600*24*365 * 10**6), color='tab:green',label='$Q_{in, W}$')
       
        ax2.set_ylim(0.0,0.8)
        
        ln3 = ax3.plot(t[:-1],np.array(FreshWaterBudget[:-1,1]/Boxes['WMed'].Area)*-1,color='red',label='(P-E)')
        ls = ln1+ln3
        labs = [l.get_label() for l in ls]
        ax3.legend(ls, labs, loc=4)    
        ax2.set_xlabel('Time [yrs]', fontweight='bold')
        
        
        ax.set_yticklabels([])
        ax2.set_yticklabels([])

        ax3.set_ylabel(r'(P-E) [m yr$^{-1}$] ',fontweight='bold', color='red')
        
            
        ax.grid(axis='y')
        ax2.grid(axis='y')
        ax3.grid(axis='y',)
        

        
        
    if i ==0:  
        t, Boxes, Fluxes, FreshWaterBudget, AirTemperature = Main(i) 
        ax.set_title('Salinity of Atlantic, WMed and EMed (2 box setup)', weight='bold')
        
        lns1 = ax.plot(t,Boxes['Atlantic'].Salinity,color='tab:blue',label='$S_{A}$')
        lns2 = ax.plot(t,Boxes['WMed'].Salinity,color='tab:green',label='$S_{WMed}$')
        lns3 = ax.plot(t,Boxes['EMed'].Salinity,color='orange',label='$S_{EMed}$')
        
        ax.set_ylim(33.5,41)
        ax.set_xticklabels([])

        lns = lns1+lns2+lns3
        labs = [l.get_label()    for l in lns]
        ax.legend(lns, labs, loc=4)
        
        
        ax2 = axes[1,i]
        ax3 = ax2.twinx()
        ln1 = ax2.plot(t[:-1],Fluxes[:,Boxes['Atlantic'].Number,Boxes['WMed'].Number][:-1]/(3600*24*365 * 10**6), color='tab:green',label='$Q_{in, W}$')
        ln2 = ax2.plot(t[:-1],Fluxes[:,Boxes['WMed'].Number,Boxes['EMed'].Number][:-1]/(3600*24*365 * 10**6), color='orange',label='$Q_{in, E}$')

        ax2.set_ylim(0.0,0.8)
        
        ln3 = ax3.plot(t[:-1],FreshWaterBudget[:-1,1]/Boxes['WMed'].Area*-1,color='red',label='(P-E)')
        ls = ln1+ln2+ln3
        labs = [l.get_label() for l in ls]
        ax3.legend(ls, labs, loc=4)    
        ax2.set_xlabel('Time [yrs]', fontweight='bold')
        ax3.set_yticklabels([])
        ax.set_ylabel('Salinity [-]',fontweight='bold')
        ax2.set_ylabel(r'$\mathbf{Q_{in} \  [Sv]}$ ',fontweight='bold')
    
    
        ax.grid(axis='y')
        ax2.grid(axis='y')
        ax3.grid(axis='y',)

        
    plt.tight_layout(h_pad=1.12,w_pad=1.12)
    plt.close() 
#plt.savefig('./../results/1 box versus 2 boxes.png')
