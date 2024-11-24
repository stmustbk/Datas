import matplotlib.pyplot as plt
import numpy as np
import math as m

solar_intensity = 1361 
eta_m = 0.8  
eta_t = 0.8  

# Panel sizes in square meters
panel_sizes = [5, 10, 20, 50, 100]

panel_counts = np.linspace(1e3, 1e7, 100)  # From 1,000 to 10,000,000


def calculate_energy(num_panels, panel_size):
    return num_panels * eta_m * eta_t * panel_size * solar_intensity


energies = {size: calculate_energy(panel_counts, size) for size in panel_sizes}


plt.figure(figsize=(10, 6))
for size, energy in energies.items():
    plt.plot(panel_counts, energy / 1e9, label=f'Panel Area: {size} m²')

plt.title('Energy Output vs. Number of Panels', fontsize=16)
plt.xlabel('Number of Panels', fontsize=14)
plt.ylabel('Energy Output (GW)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Panel Size", fontsize=12)
plt.tight_layout()

plt.show()
