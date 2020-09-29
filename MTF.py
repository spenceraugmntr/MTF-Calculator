import matplotlib.pyplot as plt
import math 
import numpy as np 

#input variables for calculating gsd
focal_length = float(input("What is your focal length in millimeters?"))
aperture_diameter = float(input("What is your aperture diameter in millimeters?"))
central_wavelength = float(input("What is your central wavelength in nanometers?"))
lpmm = float(input("What is your sensor limiting resolution in lp/mm?"))

#converting variable to meters
focal_length = focal_length*.001
aperture_diameter = aperture_diameter*.001
central_wavelength = central_wavelength*1e-9


#equations
phi = math.acos(central_wavelength*lpmm*(focal_length/aperture_diameter))
MTF = (2/math.pi)*(phi-(math.cos(phi)*math.sin(phi)))

print('your phi is', phi, 'cyc/mrad')
print('Your MTF is', MTF,'lp/mm')            
                 
# setting the x - coordinates 
x = np.array([lpmm,500,500] ) 
# setting the corresponding y - coordinates 
y = np.array([MTF,0,1]) 
  
# potting the points 
plt.plot(x, y) 
  
# function to show the plot 
plt.show() 





