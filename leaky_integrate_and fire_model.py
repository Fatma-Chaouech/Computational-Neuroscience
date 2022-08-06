# Leaky Integrate and Fire Model : Neuron equivalent to RC circuit

import matplotlib.pyplot as plt
import math
import numpy as np


constants = {
    "Rm" : 10,
    "Tm" : 10,
    "Vthreshold" : -55,
    "Vreset" : -75,
    "Vspike" : -20,
    "Em" : -70
}


simulation_time = 500
increment_time = 0.05
first_batch_time = (0,100)
first_injected_current = 0.5
second_batch_time = (125,200)
second_injected_current = 1.3
third_batch_time = (250,350)
third_injected_current = 2.0


def compute_next_voltage(previous_voltage, time) :

    if first_batch_time[0] <= time <= first_batch_time[1] :
        current = first_injected_current
    elif second_batch_time[0] <= time <= second_batch_time[1] :
        current = second_injected_current
    elif third_batch_time[0] <= time <= third_batch_time[1] :
        current = third_injected_current
    else :
        current = 0
    Voo = constants['Rm'] * current + constants['Em']
    
    if previous_voltage == constants['Vspike'] :
        return constants['Vreset']
    elif previous_voltage >= constants['Vthreshold'] :
        return constants['Vspike']
    return Voo + (previous_voltage - Voo) * math.exp(-increment_time / constants['Tm'])

voltage = constants['Em']
results = {"time" : [], "voltage" : []}
for time in np.arange(0,simulation_time, increment_time) : 
    voltage = compute_next_voltage(voltage, time)
    results["time"].append(time)
    results["voltage"].append(voltage)

plt.plot(results["time"], results["voltage"])
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.show()