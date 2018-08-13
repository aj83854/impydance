impydance
==========

A simple program that takes character impedance (Zo), normalized load impedance (Zl), and wavelength (L) values as input and calculates either normalized or complex values for Input Impedance (Zin) at any point on a transmission line.

Background
----------

This was inspired by an EE university assignment given to a colleague of mine which I am using as a learning tool for Python, as well as some basic electrical engineering mathematics.

It has been verified for accuracy by the student and professor both; however, you should probably go ahead and independetly verify the math just in case you decide to use this for yourself.


What this script actually does
------------------------------

The first function, norm_or_comp(), asks you if the calculation to be preformed should output complex or normalized values.

impedance(comp) then takes a boolean value as an arguement and calculates complex input impedance for True, and normalized input impedance for False. 

You are then asked if you'd like to run another calculation, to which anything other than 'y' or 'yes' will exit the program.

Note: norm_or_comp() returns a boolean value, so it can be passed in as an arguement to impedance(comp).

*I had to be careful not to use 'complex' so that it did not interfere with the built-in type!*

Example test cases to try:

1. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/8

2. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/4

3. cimpedance (Zo) = 100, norm_load_imp (zL) = 1, wave_len (L) = 1/4

4. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/2


Relevant Equation(s)
--------------------

Zin.(NORMALIZED or COMPLEX) =
 * Zin.COMPLEX = ((Zl + j*tan(bL)) / (1 + j*Zl*tan(bL))
 * Zin.NORMALIZED = Zo * Zin.COMPLEX

(note: (bL) in the above equation references phase angle, and a simplified equation is used in its place)

Variable Translations:

mathematical variable = python variable = type = input OR output

Zo = cimpedance = CHARECTER IMPEDANCE = complex() = *INPUT*

Zl = norm_load_imp = NORMALIZED LOAD IMPEDANCE = complex() = *INPUT*

L = wave_len = wavelength = float(Fraction()) = *INPUT*

Zin = (input_imp_norm OR input_imp_comp) = INPUT IMPEDANCE = *EXPECTED OUTPUT*

