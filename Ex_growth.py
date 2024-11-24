import matplotlib.pyplot as plt
import numpy as np

initial_panels = 1
doubling_time = 30  # Number of doublings
time_periods = np.arange(doubling_time)
solar_intensity_at_1AU = 1361  # Solar energy intensity (W/m²)
eta_m = 0.8
eta_t = 0.8
panel_size = 10  # m²

panel_growth = initial_panels * 2 ** time_periods
energy_growth = panel_growth * eta_m * eta_t * panel_size * solar_intensity_at_1AU / 1e9  # Energy in GW

plt.figure(figsize=(8, 6))
plt.plot(time_periods, energy_growth, color='purple')
plt.title('Exponential Growth of Energy')
plt.xlabel('Time (Doubling Periods)')
plt.ylabel('Energy Output (GW)')
plt.grid(True)
plt.show()
