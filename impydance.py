"""
Transmission Line Input Impedance Calculator

This module provides functions to calculate the input impedance at any point
on a transmission line, given the normalized load impedance (zL) and the length
(l) in wavelengths. The module can be imported and used in other programs or
run interactively to prompt the user for input values and display the results.

Functions
---------
calculate_input_impedance(zL, l)
    Calculate the input impedance at any point on a transmission line.
get_complex_number(prompt)
    Prompt the user to input a complex number.
run_interactively()
    Run the program interactively, prompting the user for input and displaying the output.

Example
-------
To calculate the input impedance for a given zL and l:

    >>> import transmission_line
    >>> zL = 50 - 25j
    >>> l = 0.25
    >>> Zin = transmission_line.calculate_input_impedance(zL, l)
    >>> print(Zin)
    (0.016+0.00799999999999994j)
"""


from cmath import pi, cosh, sinh


def calculate_input_impedance(zL: complex, l: float) -> complex:
    """
    Calculate the input impedance at any point on a transmission line.

    Parameters
    ----------
    zL : complex
        Normalized load impedance.
    l : float
        Length in wavelengths.

    Returns
    -------
    complex
        Normalized input impedance (Zin).
    """
    gamma = 2j * pi * l
    Zin = zL * (cosh(gamma) + (1 / zL) * sinh(gamma)) / (cosh(gamma) + zL * sinh(gamma))
    return Zin


def get_complex_number(prompt: str) -> complex:
    """
    Prompt the user to input a complex number.

    Parameters
    ----------
    prompt : str
        The text to display to the user when asking for input.

    Returns
    -------
    complex
        The complex number entered by the user.
    """
    real = float(input(f"Enter the real part of {prompt}: "))
    imag = float(input(f"Enter the imaginary part of {prompt}: "))
    return real + imag * 1j


def run_interactively():
    """
    Run interactively.
    Prompts the user for input and displays the output to stdout.
    """
    print("This program calculates the input impedance at any point on a transmission line.")
    
    zL = get_complex_number("the normalized load impedance (zL)")
    l = float(input("Enter the length in wavelengths (l): "))

    Zin = calculate_input_impedance(zL, l)
    print(f"\nThe normalized input impedance (Zin) is: {Zin}")

if __name__ == "__main__":
    run_interactively()
