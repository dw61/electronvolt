# hbar

A physical quantity calculator with units.

## Demo

#### Calculate the rest mass energy of an electron.

```
In[1]: me * c**2

Out[1]: 8.187105776823886e-14 m**2 * s**-2 * kg
```

#### Check that the energy is in Joules.

```
In[2]: me * c**2 in J # sloppy use of __contains__

Out[2]: True
```

#### Convert joules to mega electronvolts if you like.

```
In[3]: me * c**2 / MeV

Out[3]: 0.5109989499961642
```

This matches the rest mass energy of electron from [Wikipedia](https://en.wikipedia.org/wiki/Electron_rest_mass).

## Usage

Install this module using pip via `pip install hbar`.

Use this module in an interactive python environment via `from hbar import *` for best user experience.
