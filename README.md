
# Readme file for project in Best-Practices-for-Writing-Reproducible-Code workshop

## What does this project do
Dependent on the chosen configuration, parameters and initial values, this project calculates the evolution of the water properties of any semi-enclosed sea. 
For this project, a box-model setup of the Mediterranean Sea is chosen, which is semi-enclosed and only connected to the Atlantic Ocean through the Strait of Gibraltar. 
The current parameters and initial values realistically present the current-day properties of the Mediterranean Sea. Given any initial values, the evolution of temperature and salinity of the Mediterranean Sea is modelled. 

## How do you run the project
First, make sure that you have Python==>3.0 installed and all requirements mentioned in requirements.in are installed in the environment. 
Calling main.py will run and calling plots.py will generate the plot in the ./results/ directory. 
The user may change initial temperature or salinity values, change the imposed forcing over the box, change the parameters. 

### Changes to project setup 
The current project is setup for 1-box or 2-box setup. The user may choose to add any arbritrary number of additional boxes. For this, the user should add a new class in the classes.py file for each new box that the user wants to add. The requirements of the boxes are clear from the docstrings of other, already defined classes. Next, in the main.py file, the user should create the class in the Boxes dictionary. 
Any additional box should likely obey conservation of volume:

$`\frac{dV_i}{dt} = 0`$ and therefore: 

$`\sum_{i=1}^{n} Q_{i,in} = \sum Q_{i,out} `$

and therefore, compensating fluxes to ensure conservation of volume should be added manually dependent on the chosen setup. 

