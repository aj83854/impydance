from cmath import pi, tan, cos, sin, phase, sqrt
from fractions import Fraction

while True:
    norm_or_comp = input(" * Welcome to the Input Impedance Calculator! * \n"
                         "Would you like to calculate "
                         "normalized or complex impedance? ").lower()
    if norm_or_comp == "normalized":
        print("\nWe'll gather a few more details in order "
              f"to calculate the {norm_or_comp.upper()} impedance!")
        input("Press 'Enter' to continue. . .\n")
        cimpedance = complex(
            input("What is the character impedance, in ohms? "))
        norm_load_imp = complex(
            input("What is the normalized load impedance? "))
        wave_len = float(
            Fraction(
                input("And finally, what is the length, in wavelengths? ")))
        input_imp_norm = ((cimpedance.real + cimpedance.imag) * (
            ((norm_load_imp.real + norm_load_imp.imag) /
             (cimpedance.real + cimpedance.imag)) +
            (1j * ((tan(2 * pi * wave_len))) /
             (((norm_load_imp.real + 1j * norm_load_imp.imag) /
               (cimpedance.real + cimpedance.imag)) * tan(2 * pi * wave_len))))
                          )
        print("The normalized input impedence "
              f"in this case is {input_imp_norm}!\n")
    elif norm_or_comp == "complex":
        print("\nWe'll gather a few more details in order "
              f"to calculate the {norm_or_comp.upper()} impedance!")
        input("Press 'Enter' to continue. . .\n")
        cimpedance = complex(
            input("What is the character impedance, in ohms? "))
        norm_load_imp = complex(
            input("What is the normalized load impedance? "))
        wave_len = float(
            Fraction(
                input("And finally, what is the length, in wavelengths? ")))
        input_imp_comp = (1j * ((tan(2 * pi * wave_len))) / (
            ((norm_load_imp.real + 1j * norm_load_imp.imag) /
             (cimpedance.real + cimpedance.imag)) * tan(2 * pi * wave_len)))
        print("The complex input impedence "
              f"in this case is {input_imp_comp}!\n")
    else:
        print("Please type either 'normalized' or 'complex' when prompted.\n")
