import matplotlib.pyplot as plt
import math
import numpy as np

# Given parameters
d = 35
d = 35
e = 1.1023  # Adjust this as needed
g = 0.75   # Gaiarate

# Temperature range from 20.5 to 21.5 with 0.1 increments
temperatures = np.arange(19.66, 23.00, 0.1)

# Compute emissions
endcoin_emissions = [math.exp(e * (d - T)) - 1 for T in temperatures]
gaiacoin_emissions = [math.exp(g * T) - 1 for T in temperatures]

# Create the plot
plt.figure(figsize=(10,6))
plt.plot(temperatures, endcoin_emissions, marker='o', label='Endcoin Emissions')
plt.plot(temperatures, gaiacoin_emissions, marker='s', label='Gaiacoin Emissions', color='orange')

# Add reference line at 21°C
plt.axvline(x=21.0, color='gray', linestyle='--', linewidth=2)

# Labels and Title
plt.title('Endcoin vs Gaiacoin Daily Emissions from 20.5°C to 21.5°C')
plt.xlabel('Temperature (°C)')
plt.ylabel('Tokens per Day')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
