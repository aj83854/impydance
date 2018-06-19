project-imPydance
======================

A simple script that takes character impedance (Zo), normalized load impedance (Zl), and wavelength (L) values as input and calculates either normalized or complex values for Input Impedance (Zin) at any point on a transmission line.

Background
----------

This was inspired by an EE university assignment given to a colleague of mine which I am using as a learning tool for Python, as well as some basic electrical engineering mathematics.

I started this project a few months back while I was in the middle of a python course, and when I came back to this I saw that it was, as expected, not only poorly written (still learning!) but also unexpectedly provided incorrect output. After re-consulting with my very bright colleague, they helped me understand the math and I spent only about an hour translating the garbage I originally typed out and refactored it into what it is now- just a single, infinitely looping conditional.

It has been verified for accuracy by the student and myself; however, you should probably go ahead and double-check the math just in case.


What this script actually does
------------------------------

First, a conditional runs asking if you want the output as either 'Complex' or 'Normalized'.

Based on your selection and additional inputs for (Zo), (Zl), and (L), a calculation will run and provide either the complex load impedance value, OR the normalized value.

Example test cases to try:

1. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/8

2. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/4

3. cimpedance (Zo) = 100, norm_load_imp (zL) = 1, wave_len (L) = 1/4

4. cimpedance (Zo) = 50, norm_load_imp (zL) = 1, wave_len (L) = 1/2

***
*Please Note*

In its current state, there is really no error handling other than the first conditional which will only process the rest of the script if 'normalized' or 'complex' is specified.
Wavelength WILL accept fractions OR decimal values; however, the script will break if blank or string input is given to any of the value input prompts.
***

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

Zin = [input_imp_norm, input_imp_comp] = INPUT IMPEDANCE = *EXPECTED OUTPUT*


Future Plans
------------

Not only do I intend to re-refactor it and add additional features/functionality, but, I'll most likely eventually add this into a more complex program with multiple engineering calculations.

---
Feel free to leave constructive feedback, comments, or let me know if something is off with the math/calculations!
