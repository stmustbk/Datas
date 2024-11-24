import matplotlib.pyplot as plt
import numpy as np

solar_intensity_at_1AU = 1361  
eta_m = 0.8
eta_t = 0.8
panel_size = 10  
AU_to_km = 1.496e8  


distances_AU = np.linspace(0.1, 1.5, 100)  
energy_earth = panel_size * eta_m * eta_t * solar_intensity_at_1AU * (10000000 / distances_AU**2) / 1e9 

plt.figure(figsize=(8, 6))
plt.plot(distances_AU, energy_earth, color='blue')
plt.title('Energy vs Distance from Sun')
plt.xlabel('Distance from Sun (AU)')
plt.ylabel('Energy Output (GW) for 10^7 panels of 10m^2 size')
plt.grid(True)
plt.show()
