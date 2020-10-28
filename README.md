## Demo

#### Calculate the rest mass energy of an electron.

```
>>> me * c**2
8.187105776823886e-14 m**2 * s**-2 * kg
```

#### Check that the energy is in Joules.

```
>>> me * c**2 in J # sloppy use of __contains__
True
```

#### Convert joules to mega electronvolts if you like.

```
>>> me * c**2 / MeV
0.5109989499961642
```

This matches the rest mass energy of electron from [Wikipedia](https://en.wikipedia.org/wiki/Electron_rest_mass).

## Usage

Install this module using pip via `pip install hbar`.

Use this module in an interactive python environment, such as jupyter notebook, via `from hbar import *`, for best using experience.
