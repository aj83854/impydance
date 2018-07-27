from cmath import pi, tan, cos, sin, phase, sqrt
from fractions import Fraction

def norm_or_comp():
    """
    Checks to see if user is calculating normalized or complex input impedence;
    returns boolean value.
    """
    while True:
        is_complex = input("Would you like to calculate "
                        "normalized or complex impedance? ").lower()
        if is_complex == "normalized":
            return False
        elif is_complex == "complex":
            return True
        else:
            print("Please type only 'normalized' or 'complex'\n")

def impedance(comp):
    """
    Meant for use with norm_or_comp(), but, it will
    also work with a boolean passed in as an arguement.

    Calculates complex input impedance for True,
    and normalized input impedance for False arguments, respectively.
    """
    if comp:
        while True:
            print("Calculating COMPLEX input impedance. . .")
            cimpedance = complex(
                input("What is the character impedance, in ohms? "))
            norm_load_imp = complex(
                input("What is the normalized load impedance? "))
            wave_len = float(
                Fraction(
                    input("And finally, what is the length in wavelengths? ")))
            input_imp_comp = (1j * ((tan(2 * pi * wave_len))) / (
                ((norm_load_imp.real + 1j * norm_load_imp.imag) /
                (cimpedance.real + cimpedance.imag)) * tan(2 * pi * wave_len)))
            print("The complex input impedence in this case is "
                  f"{input_imp_comp}!\n")
            break
    elif not comp:
        while True:
            print("Calculating NORMALIZED input impedance. . .")
            cimpedance = complex(
                input("What is the character impedance, in ohms? "))
            norm_load_imp = complex(
                input("What is the normalized load impedance? "))
            wave_len = float(
                Fraction(
                    input("And finally, what is the length in wavelengths? ")))
            input_imp_norm = ((cimpedance.real + cimpedance.imag) * (
                ((norm_load_imp.real + norm_load_imp.imag) /
                (cimpedance.real + cimpedance.imag)) +
                (1j * ((tan(2 * pi * wave_len))) /
                (((norm_load_imp.real + 1j * norm_load_imp.imag) /
                (cimpedance.real + cimpedance.imag)) * tan(2 * pi * wave_len)))
                ))
            print("The normalized input impedence in this case is "
                  f"{input_imp_norm}!\n")
            break
    run_again = input("Would you like to run another calculation? ").lower()
    if run_again in ("y", "yes"):
        impedance(norm_or_comp())

impedance(norm_or_comp())
