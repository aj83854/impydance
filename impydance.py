from cmath import pi, tan
from fractions import Fraction


class Impedance:

    def __init__(self, character_imp, normalized_load_imp, wavelength, normalized=True):
        self.character_imp = character_imp
        self.normalized_load_imp = normalized_load_imp
        self.wavelength = wavelength
        self.normalized = normalized

    def __repr__(self):
        if self.normalized:
            input_imp_norm = ((self.character_imp.real + self.character_imp.imag) *
                              (((self.normalized_load_imp.real + self.normalized_load_imp.imag) /
                                (self.character_imp.real + self.character_imp.imag)) +
                               (1j * (tan(2 * pi * self.wavelength)) /
                                (((self.normalized_load_imp.real + 1j * self.normalized_load_imp.imag) /
                                  (self.character_imp.real + self.character_imp.imag)) *
                                  tan(2 * pi * self.wavelength)))))
            return str(input_imp_norm)
        input_imp_comp = ((((self.normalized_load_imp.real + self.normalized_load_imp.imag) /
                            (self.character_imp.real + self.character_imp.imag)) +
                           (1j * (tan(2 * pi * self.wavelength)) /
                            (((self.normalized_load_imp.real + 1j * self.normalized_load_imp.imag) /
                              (self.character_imp.real + self.character_imp.imag)) *
                             tan(2 * pi * self.wavelength)))))
        return str(input_imp_comp)


def norm_or_comp():
    """
    Returns a boolean value based on user input.
    True will be returned if 'complex' is given.
    False will be returned if 'normalized' is given.
    Use to determine a normalized or complex value.
    """
    while True:
        value = input(
            "Type [1] to calculate normalized input impedance, [2] for complex, or [3] to quit: ")
        if value == "1":
            return False
        elif value == "2":
            return True
        elif value == "3":
            quit()


def character_impedance():
    """ Returns character impedance as complex value. """
    while True:
        try:
            char_impedance = complex(
                input("What is the character impedance, in ohms? "))
        except ValueError:
            print("Value cannot be empty or contain any letters!\n")
        else:
            return char_impedance


def norm_load_impedance():
    """ Returns normalized load impedance as complex value. """
    while True:
        try:
            norm_load_imp = complex(
                input("What is the normalized load impedance? "))
        except ValueError:
            print("Value cannot be empty or contain any letters!\n")
        else:
            return norm_load_imp


def wavelength():
    """ Returns wavelength as floating point value. """
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
            print("Calculating COMPLEX input impedance-")
            cimpedance = character_impedance()
            norm_load_imp = norm_load_impedance()
            wave_len = wavelength()
            input_imp_comp = ((((norm_load_imp.real + norm_load_imp.imag) /
                                (cimpedance.real + cimpedance.imag)) +
                               (1j * (tan(2 * pi * wave_len)) /
                                (((norm_load_imp.real + 1j * norm_load_imp.imag) /
                                  (cimpedance.real + cimpedance.imag)) *
                                 tan(2 * pi * wave_len)))))
            print(f"The complex input impedance in this case is {input_imp_comp}!\n")
            break
    elif not comp:
        while True:
            print("Calculating NORMALIZED input impedance-")
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
            print(f"The normalized input impedance in this case is {input_imp_norm}!\n")
            break
    while True:
        run_again = input("Would you like to run another calculation? ").lower()
        if run_again in ("y", "yes"):
            impedance(norm_or_comp())
        elif run_again in ("n", "no"):
            break


if __name__ == '__main__':
    impedance(norm_or_comp())
