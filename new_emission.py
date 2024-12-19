import matplotlib.pyplot as plt
import math
import numpy as np

# Parameters
T0 = 21.0              # Center temperature
centerEmission = 1_000_000  # Emission level at T=21°C (choose any value)
C = 0                  # Offset, can be zero for simplicity
M = centerEmission      # Since C=0, M=centerEmission
H = 1.125                # Controls steepness of the exponential curve

def E(T):
    # Endcoin emission: decreases as T increases beyond T0
    return M * math.exp(H * (T0 - T)) - C

def G(T):
    # Gaiacoin emission: increases as T increases beyond T0
    return M * math.exp(H * (T - T0)) - C

# Temperature range for plotting (20°C to 22°C as an example)
temperatures = np.arange(T0 - 2, T0 + 2, 0.1)

# Compute emissions
endcoin_emissions = [E(T) for T in temperatures]
gaiacoin_emissions = [G(T) for T in temperatures]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(temperatures, endcoin_emissions, label='Endcoin Emissions', marker='o', markevery=2)
plt.plot(temperatures, gaiacoin_emissions, label='Gaiacoin Emissions', marker='s', markevery=2, color='orange')

# Vertical line at T=T0
plt.axvline(x=T0, color='gray', linestyle='--', linewidth=1)

# Labels and Title
plt.title('Symmetrical Endcoin vs Gaiacoin Emissions Around T0={}°C'.format(T0))
plt.xlabel('Temperature (°C)')
plt.ylabel('Tokens per Day')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
