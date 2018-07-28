from cmath import pi, tan
from fractions import Fraction


def norm_or_comp():
    """
    Returns a boolean value based on user input.
    True will be returned if 'complex' is given.
    False will be returned if 'normalized' is given.
    Use to determine a normalized or complex value.
    """
    while True:
        norm_or_comp = input("Would you like to calculate normalized "
                             "or complex input impedance? ").lower()
        if norm_or_comp == "complex":
            return True
        elif norm_or_comp == "normalized":
            return False
        else:
            print("Please type only 'normalized' or 'complex'\n")


def character_impedance():
    """ returns character impedance as complex value """
    while True:    
        try:
            char_impedance = complex(
                input("What is the character impedance, in ohms? "))
        except ValueError:
            print("Value cannot be empty or contain any letters!\n")
        else:
            return char_impedance


def norm_load_impedance():
    """ returns normalized load impedance as complex value """
    while True:    
        try:
            norm_load_imp = complex(
                input("What is the normalized load impedance? "))
        except ValueError:
            print("Value cannot be empty or contain any letters!\n")
        else:
            return norm_load_imp


def wavelength():
    """ returns wavelength as floating point value """
    while True:    
        try:
            wave_len = float(
                Fraction(
                    input("What is the length in wavelengths? ")))
        except ValueError:
            print("Value cannot be empty or contain any letters!\n")
        else:
            return wave_len


def impedance(comp):
    """
    Meant for use with norm_or_comp(), but, it will
    also work with a boolean passed in as an argument.
    Calculates complex input impedance for True,
    and normalized input impedance for False arguments, respectively.
    """
    if comp:
        while True:
            print("Calculating COMPLEX output...")
            cimpedance = character_impedance()
            norm_load_imp = norm_load_impedance()
            wave_len = wavelength()
            input_imp_comp = (1j * (tan(2 * pi * wave_len)) /
                (((norm_load_imp.real + 1j * norm_load_imp.imag) /
                 (cimpedance.real + cimpedance.imag)) *
                  tan(2 * pi * wave_len)))
            print("The complex input impedance in this case is "
                  f"{input_imp_comp}!\n")
            break
    elif not comp:
        while True:
            print("Calculating NORMALIZED output...")
            cimpedance = character_impedance()
            norm_load_imp = norm_load_impedance()
            wave_len = wavelength()
            input_imp_norm = ((cimpedance.real + cimpedance.imag) *
                (((norm_load_imp.real + norm_load_imp.imag) /
                 (cimpedance.real + cimpedance.imag)) +
                  (1j * (tan(2 * pi * wave_len)) /
                (((norm_load_imp.real + 1j * norm_load_imp.imag) /
                 (cimpedance.real + cimpedance.imag)) *
                  tan(2 * pi * wave_len)))))
            print("The normalized input impedance in this case is "
                  f"{input_imp_norm}!\n")
            break
    while True:
        run_again = input(
            "Would you like to run another calculation? ").lower()
        if run_again in ("y", "yes"):
            impedance(norm_or_comp())
        elif run_again in ("n", "no"):
            break
        else:
            print("Please type either (Y)es or (N)o...\n")


impedance(norm_or_comp())
