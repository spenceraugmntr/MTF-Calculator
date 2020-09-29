import matplotlib.pyplot as plt
import math 
import numpy as np 

#input variables for calculating gsd
focal_length = float(input("What is your focal length in millimeters?"))
aperture_diameter = float(input("What is your aperture diameter in millimeters?"))
central_wavelength = float(input("What is your central wavelength in nanometers?"))
lpmm = float(input("What is your sensor limiting resolution in lp/mm?"))

#converting variable to meters
central_wavelength = central_wavelength*1e-6


#equations
cutoff = 1/(central_wavelength*(focal_length/aperture_diameter))
phi = math.acos(central_wavelength*lpmm*(focal_length/aperture_diameter))
MTF = (2/math.pi)*(phi-(math.cos(phi)*math.sin(phi)))

print('your cutoff frequency is', cutoff, 'lp/mm')
print('your phi is', phi, 'lp/mm')
print('Your MTF is', MTF,'lp/mm')            
                 
# setting the x - coordinates 
x = np.linspace(0,500,500)
# setting the corresponding y - coordinates 
phi1 = np.arccos(central_wavelength*x*(focal_length/aperture_diameter))

y = (2/np.pi)*(phi1-(np.cos(phi1)*np.sin(phi1))) 
  
# potting the points 
plt.plot(x, y) 
  
# function to show the plot 
plt.show() 





