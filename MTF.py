import matplotlib.pyplot as plt
import math 
import numpy as np 

#input variables for calculating gsd
focal_length = float(input("What is your focal length in millimeters?"))
aperture_diameter = float(input("What is your aperture diameter in millimeters?"))
central_wavelength = float(input("What is your central wavelength in nanometers?"))
lpmm = float(input("What spatial resolution are you wishing to find a value for (lp/mm)?"))

#converting variable to mm
central_wavelength = central_wavelength*1e-6

#equations/outputs
cutoff = 1/(central_wavelength*(focal_length/aperture_diameter))
phi = math.acos(central_wavelength*lpmm*(focal_length/aperture_diameter))
MTF = (2/math.pi)*(phi-(math.cos(phi)*math.sin(phi)))

print('your cut-off frequency is', cutoff, 'lp/mm')
print('your phi is', phi, 'lp/mm')
print('Your MTF is', MTF,'lp/mm')            
                 
# setting the x - coordinates 
x = np.linspace(0,cutoff,500)
# setting the corresponding y - coordinates 
y = (2/np.pi)*(np.arccos(x/cutoff)-(np.cos(np.arccos(x/cutoff))*np.sin(np.arccos(x/cutoff)))) 
  
# plotting the points 
plt.plot(x, y) 

#axis titles
plt.title('MTF (lp/mm)')
plt.xlabel('Spatial Resolution (lp/mm)')
plt.ylabel('MTF')
  
# function to show the plot 
plt.show() 




