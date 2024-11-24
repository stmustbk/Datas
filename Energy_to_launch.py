import matplotlib.pyplot as plt
import numpy as np
import math


G = 6.67430e-11

planets = {
    'Earth': {'mass': 5.972e24, 'radius': 6.371e6},
    'Moon': {'mass': 7.347e22, 'radius': 1.737e6},
    'Mercury': {'mass': 3.301e23, 'radius': 2.439e6}
}

# Функция для расчета второй космической скорости
def escape_velocity(mass, radius):
    return math.sqrt(2 * G * mass / radius)

# Функция для расчета энергии
def energy_to_launch(mass, velocity):
    return 0.5 * mass * velocity ** 2

# Масса объекта (в кг)
object_mass = 100


planet_names = []
energy_values = []


for planet, data in planets.items():
    v_escape = escape_velocity(data['mass'], data['radius'])  
    energy = energy_to_launch(object_mass, v_escape)  
    planet_names.append(planet)
    energy_values.append(energy / 1e9)  # Переводим в гигаджоули

plt.figure(figsize=(8, 6))
plt.bar(planet_names, energy_values, color=['orange', 'green', 'blue'])
plt.title('Energy to Launch 100 kg Object from Different Planets (Escape Velocity)')
plt.xlabel('Planet')
plt.ylabel('Energy (GJ)')
plt.grid(True)
plt.show()
