# Impydance

Impydance is a Python module that calculates the input impedance at any point on a transmission line, given the normalized load impedance (zL) and the length (l) in wavelengths.

The module can be used as a standalone interactive script or imported and used in other Python programs.

## Purpose and Use

The purpose Impydance is to help engineers, students and researchers to quickly and easily calculate the input impedance of transmission lines. This information is crucial for designing and analyzing various radio frequency (RF) and microwave systems, such as antennas, filters, and matching networks.

## How It Works

Impydance calculates the input impedance using the transmission line theory, based on the given normalized load impedance and the length of the transmission line in wavelengths. The application handles complex numbers and can provide the results in both complex and normalized impedance formats.

The relevant equation is:

```math
Zin = ZL * (cosh(γL) + (1 / ZL) * sinh(γL)) / (cosh(γL) + ZL * sinh(γL))
```

Where:

- `Zin` is the complex input impedance
- `ZL` is the normalized load impedance (complex)
- `γ` is the complex propagation constant
- `L` is the length of the transmission line in wavelengths

## Usage

### Interactively

To run Impydance interactively, simply execute the transmission_line.py script:

```bash
python impydance.py
```

The script will prompt you to enter the real and imaginary parts of the normalized load impedance (zL) and the length in wavelengths (l).

After entering the required values, the script will calculate and display the input impedance (Zin).

### As a Module

Impydance can also be imported and used in other Python programs as well:

```python
import impydance

zL = 50 - 25j
l = 0.25

Zin = impydance.calculate_input_impedance(zL, l)
print(Zin)
```

This example calculates the input impedance for a normalized load impedance of 50 - 25j and a length of 0.25 wavelengths.
