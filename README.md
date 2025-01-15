
# Readme file for project in Best-Practices-for-Writing-Reproducible-Code workshop

## What does this project do
Dependent on the chosen configuration, parameters and initial values, this project calculates the evolution of the water properties of any semi-enclosed sea. 
For this project, a box-model setup of the Mediterranean Sea is chosen, which is semi-enclosed and only connected to the Atlantic Ocean through the Strait of Gibraltar. 
The current parameters and initial values realistically present the current-day properties of the Mediterranean Sea. Given any initial values, the evolution of temperature and salinity of the Mediterranean Sea is modelled. 

![Example sketch of simple box model setup](/assets/images/Simple_1box.drawio.png)


## How do you run the project
* Make sure that you have Python==>3.0 installed 
* Clone this repository
* You can either call main.py to run the model or plots.py to create a figure in ./results/ directory. Make sure you run from the /src/ directory. 
* The user may change initial temperature or salinity values, change the imposed forcing over the box, change the parameters. For this, the user must make changes in the main, constants, classes or forcing file. 

### Changes to project setup 
The current project is setup for 1-box or 2-box setup. The user may choose to add any arbritrary number of additional boxes. For this, the user should add a new class in the classes.py file for each new box that the user wants to add. The requirements of the boxes are clear from the docstrings of other, already defined classes. Next, in the main.py file, the user should create the class in the Boxes dictionary. 
Any additional box should likely obey conservation of volume:

$`\frac{dV_i}{dt} = 0`$ and therefore: 

$`\sum_{i=1}^{n} Q_{i,in} = \sum Q_{i,out} `$

and therefore, compensating fluxes to ensure conservation of volume should be added manually dependent on the chosen setup. 

### Important final notes
This setup is currently only configured for a realistic configuration, that is, the Atlantic Ocean will always have a lower density than the Mediterranean Sea and there is always a net evaporation. This is important because the compensating fluxes are calculated manually and any changes in forcing or properties of the Atlantic Ocean will lead to unphysical results. 

