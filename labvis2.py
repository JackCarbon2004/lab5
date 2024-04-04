import matplotlib.pyplot as plt
import numpy as np

# Resistor data
resistor_1_data = np.array([[0.5, 0.52], [1.0, 1.04], [1.5, 1.56], [2.0, 2.08], [2.5, 2.60], 
                            [3.0, 3.12], [3.5, 3.64], [4.0, 4.16], [4.5, 4.68], [5.0, 5.20]])

resistor_2_data = np.array([[0.5, 51.2], [1.0, 107.1], [1.5, 154.4], [2.0, 219.0], [2.5, 258.0], 
                            [3.0, 308.0], [3.5, 360.0], [4.0, 292.0], [4.5, 448.0], [5.0, 526.0]])

resistor_3_data = np.array([[0.5, 0.05], [1.0, 0.09], [1.5, 0.16], [2.0, 0.22], [2.5, 0.27], 
                            [3.0, 0.28], [3.5, 0.33], [4.0, 0.39], [4.5, 0.43], [5.0, 0.49]])


# Graphite and incandescent bulb data
graphite_data = np.array([[0.5, 2.34], [1.0, 4.67], [1.5, 7.01], [2.0, 9.35], [2.5, 11.68], 
                          [3.0, 14.02], [3.5, 16.36], [4.0, 18.69], [4.5, 21.03], [5.0, 23.36]])

bulb_data = np.array([[0.2, 11.11], [0.4, 22.22], [0.6, 33.33], [0.8, 44.44], [1.0, 55.56], 
                      [1.2, 66.67], [1.4, 77.78], [1.6, 88.89], [1.8, 100.00], [2.0, 105.26], 
                      [2.2, 110.00], [2.4, 114.29], [2.6, 118.18], [2.8, 121.74], [3.0, 125.00]])

# LED data
led_red_data = np.array([[0.0, 0.00], [0.5, 0.00], [1.0, 0.00], [1.5, 0.00], [1.7, 0.61], 
                         [1.8, 2.44], [1.9, 6.10], [2.0, 12.20], [2.1, 18.29], [2.2, 24.39]])

led_yellow_data = np.array([[0.0, 0.00], [0.5, 0.00], [1.0, 0.00], [1.5, 0.00], [1.9, 0.55], 
                            [2.0, 2.20], [2.1, 5.49], [2.2, 10.99], [2.3, 16.48], [2.4, 21.98]])

led_green_data = np.array([[0.0, 0.00], [0.5, 0.00], [1.0, 0.00], [1.5, 0.00], [2.0, 0.00], 
                           [2.5, 0.42], [2.6, 1.67], [2.7, 4.17], [2.8, 8.33], [2.9, 12.50], [3.0, 16.67]])

led_blue_data = np.array([[0.0, 0.00], [0.5, 0.00], [1.0, 0.00], [1.5, 0.00], [2.0, 0.00], [2.5, 0.00], 
                          [2.9, 0.33], [3.0, 1.33], [3.1, 3.33], [3.2, 6.67], [3.3, 10.00], [3.4, 13.33]])

# Create subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Plot resistor data
axs[0, 0].plot(resistor_1_data[:, 0], resistor_1_data[:, 1], 'o-', label='Resistor 1 (1 kΩ)')
axs[0, 0].plot(resistor_2_data[:, 0], resistor_2_data[:, 1], 'o-', label='Resistor 2 (10 Ω)')
axs[0, 0].plot(resistor_3_data[:, 0], resistor_3_data[:, 1], 'o-', label='Resistor 3 (10 kΩ)')
axs[0, 0].set_xlabel('Voltage (V)')
axs[0, 0].set_ylabel('Current (mA)')
axs[0, 0].set_title('Resistor I-V Curves')
axs[0, 0].legend()

# Plot graphite and incandescent bulb data
axs[0, 1].plot(graphite_data[:, 1], graphite_data[:, 0], 'o-', label='Graphite')
axs[0, 1].plot(bulb_data[:, 1], bulb_data[:, 0], 'o-', label='Incandescent Bulb')
axs[0, 1].set_xlabel('Current (mA)')
axs[0, 1].set_ylabel('Voltage (V)')
axs[0, 1].set_title('Graphite and Incandescent Bulb I-V Curves')
axs[0, 1].legend()

# Plot LED data
axs[1, 0].plot(led_red_data[:, 1], led_red_data[:, 0], 'o-', color='red', label='Red LED')
axs[1, 0].set_xlabel('Current (mA)')
axs[1, 0].set_ylabel('Voltage (V)')
axs[1, 0].set_title('Red LED I-V Curve')
axs[1, 0].legend()

axs[1, 1].plot(led_yellow_data[:, 1], led_yellow_data[:, 0], 'o-', color='yellow', label='Yellow LED')
axs[1, 1].set_xlabel('Current (mA)')
axs[1, 1].set_ylabel('Voltage (V)')
axs[1, 1].set_title('Yellow LED I-V Curve')
axs[1, 1].legend()

axs[2, 0].plot(led_green_data[:, 1], led_green_data[:, 0], 'o-', color='green', label='Green LED')
axs[2, 0].set_xlabel('Current (mA)')
axs[2, 0].set_ylabel('Voltage (V)')
axs[2, 0].set_title('Green LED I-V Curve')
axs[2, 0].legend()

axs[2, 1].plot(led_blue_data[:, 1], led_blue_data[:, 0], 'o-', color='blue', label='Blue LED')
axs[2, 1].set_xlabel('Current (mA)')
axs[2, 1].set_ylabel('Voltage (V)')
axs[2, 1].set_title('Blue LED I-V Curve')
axs[2, 1].legend()

plt.tight_layout()
plt.show()