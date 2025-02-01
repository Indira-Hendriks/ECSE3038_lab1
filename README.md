# Indira Hendriks - Lab#1

## Overview:

This project contains three Python functions designed to perform electrical and temperature calculations. 
The code was written for the purpose of an assignment to showcase proficiency in Python programming, 
specifically working with lists, mathematical calculations, and conditional statements.

## Functions:

### 1. 'parallel(resistors)'

This function calculates and prints the effective resistance of a network of resistors connected in parallel.
The function accepts a single list of resistor values as an argument.

**Expected Behavior:**
- Checks if the resistor list is empty.
- Ensures that none of the resistor values are zero.
- Calculates the equivalent resistance using the formula for resistors in parallel.
- Prints the effective resistance in ohms.

**Example Usage:**
parallel([330, 1000, 2200])
Output: Effective Resistance: 245.614 Ohms

### 2. 'potential_divider(supply_voltage,r_in_series)'

This function calculates and prints the voltage drop across each resistor in a series circuit. The function accepts:
-A numerical value representing the supply voltage (supply_voltage).
-A list of numerical values representing the resistances of resistors connected in series (r_in_series).

**Expected Behavior:**
-The function calculates the total resistance of the circuit.
-It determines the voltage drop across each resistor using the voltage division rule
-It prints the voltage drop across each resistor in the list.

**Example Usage:**
potential_divider(9, [3000, 1000])
Output: Voltage drop across resistor 1 (3000 ohms): 6.75 volts
        Voltage drop across resistor 2 (1000 ohms): 2.25 volts

### 3. 'tempertature_check (temp, unit_temp)'

This function determines whether a patient is hypothermic, hyperthermic, or has a normal body temperature based on input values.
The function accepts:
-A numerical value representing body temperature.
-A character ('C' for Celsius or 'F' for Fahrenheit) representing the temperature unit.

**Expected Behavior:**
-The function first validates the input to ensure:
-temp is a number (integer or float).
-unit_temp is a single character (either 'C' or 'F').

-It checks the temperature range and classifies the patient's condition based on the following criteria:
Celsius (C):
--Hypothermic: Below 35°C
--Normal: 35°C to 37°C
--Hyperthermic: Above 37°C

Fahrenheit (F):
--Hypothermic: Below 95°F
--Normal: 95°F to 98.6°F
--Hyperthermic: Above 98.6°F

-If an invalid unit is entered, an error message is displayed.

**Example Usage:**
temperature_check(35, 'C')
temperature_check(30, 'C')
temperature_check(40, 'C')
temperature_check(96, 'F')
temperature_check(92, 'F')
temperature_check(100, 'F')
temperature_check(35, 'K')

output: 
The patient's body temperature of 35°C is NORMAL!
Unfortunately... the patient's body temperature of 30°C is HYPOTHERMIC.
Alas... the patient's body temperature of 40°C is HYPERTHERMIC.
The patient's body temperature of 96°F is NORMAL!
Unfortunately... the patient's body temperature of 92°F is HYPOTHERMIC.
Alas... the patient's body temperature of 100°F is HYPERTHERMIC.
Invalid temperature unit. Please use 'C' for Celsius or 'F' for Fahrenheit!


## Short Joke:

"Life"
