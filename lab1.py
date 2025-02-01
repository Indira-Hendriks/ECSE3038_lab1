# Indira Hendriks 
# QUESTION 1
# Write a function, parallel(), that, when called, prints the effective resistance of
#  a network of resistors connected in parallel. 
# The function should be able to accept a single list as argument. 

def parallel(resistors):
    if not resistors:
        print("No values for the resistors were provided.")#Ensuring that values are imputed.
        return
    
    if any(r == 0 for r in resistors):
        print("Error: Resistance value cannot be zero.") #Checking for zero error.
        return
    
    else:
        equivalent_resistance = 1 / sum(1 / r for r in resistors) #Formula to calculate equivalent resistance in parallel.
        print(f"Effective Resistance: {equivalent_resistance:.3f} Ohms")
    

#Test Example:
parallel([330, 1000, 2200])


# QUESTION 2

#1. Write a function, `potential_divider()`, that takes **two values** as argument:
# a number that represents a voltage supply value, and a **list** of numbers that represent resistance values of resistors connected in series.
# The function should output the voltage drop across each resistor in your resistor list. 
# The function should be able to accept a **list** of any length. 


def potential_divider(supply_voltage,r_in_series):

    sum_of_r = sum(r_in_series)
    volt_drops = [(r / sum_of_r) * supply_voltage for r in r_in_series]

    index = 1
    for drop in volt_drops:
        print(f"Voltage drop across resistor {index} ({r_in_series[index - 1]} ohms): {drop} volts")
        index += 1
        
#Test Example
potential_divider(9, [3000, 1000])


# QUESTION 3

# 2. Write a function, `temperature_check()`, that accepts a single number, 
# a patient's body temperature, and a single character, the unit of temperature. 
# The function should output whether the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function.   
# The second value passed as argument should tell the function whether the condition should calculated in degrees celcius or degrees fahrenheit.  
# An appropriate message should be written to the screen with the result. You’re free to use what ever reasonable temperature limits you feel will adequately act as boundaries for these conditions.

def tempertature_check (temp, unit_temp):
    if not isinstance(temp, (int, float)): #Checking to see if variables other than float or integers are entered
        print("Error: Temperature must be a number.")
        return
    if not isinstance(unit_temp, str) or not unit_temp.isalpha(): #Ensuring that only a single letter is entered
        print("Error: Temperature unit must be a letter (C or F).")
        return
    
    unit_temp = unit_temp.upper()  # Converts the unit to an uppercase character for consistency

    # Normal body temperature: Around 37°C (98.6°F). 
    # Hypothermic: Body temperature below 35°C (95°F). 
    # Hyperthermic: Body temperature above 37°C (98.6°F). 

    # Checking for temperatures:
   # Celsius Temperature Check
    if unit_temp == 'C':  
        if temp < 35:
            print(f"Unfortunately... the patient's body temperature of {temp}°C is HYPOTHERMIC.")
        elif temp >= 35 and temp <= 37:
            print(f"The patient's body temperature of {temp}°C is NORMAL!")
        else:
            print(f"Alas... the patient's body temperature of {temp}°C is HYPERTHERMIC.")

    # Kelvin Temperature Check
    elif unit_temp == 'F':  
        if temp < 95:
            print(f"Unfortunately... the patient's body temperature of {temp}°F is HYPOTHERMIC.")
        elif temp >= 95 and temp <= 98.6:
            print(f"The patient's body temperature of {temp}°F is NORMAL!")
        else:
            print(f"Alas... the patient's body temperature of {temp}°F is HYPERTHERMIC.")

    else:
        print("Invalid temperature unit. Please use 'C' for Celsius or 'K' for Kelvin!")

# Test Example:
tempertature_check(35,'C')
tempertature_check(30,'C')
tempertature_check(40,'C')
tempertature_check(96,'F')
tempertature_check(92,'F')
tempertature_check(100,'F')
tempertature_check(35,'K')