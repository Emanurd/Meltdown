"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature: int or float, neutrons_emitted: int or float):
  
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
        
        
    


def reactor_efficiency(voltage: int or float, current: int or float, theoretical_max_power: int or float):
 
    generated_power = voltage * current
    percentage_value = (generated_power/ theoretical_max_power) * 100 

    if percentage_value >= 80:
        return "green"
    if percentage_value >= 60:
        return "orange"
    if percentage_value >= 30:
        return "red"
    return "black"


def fail_safe(temperature: int or float, neutrons_produced_per_second: int or float, threshold: int or float):
 
    if temperature * neutrons_produced_per_second < (0.9 * threshold):
        return "LOW"
    if temperature * neutrons_produced_per_second < (1.1 * threshold):
        return "NORMAL"
    return "DANGER"
    