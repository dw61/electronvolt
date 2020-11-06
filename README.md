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

Use this module in an interactive python environment, such as jupyter notebook, via `from hbar import *`, for best experience.

You can also run this module online [here](https://mybinder.org/v2/gh/DiegoWang51/hbar/HEAD?filepath=others%2Fcalculator.ipynb). Use shift+enter to execute a block of code. Execute the first block of code upon entry to initialize the calculator. This page typically loads in 3 minutes.

## Units and Constants

Here are a list of units and constants that this module currently supports. A constant table will also be (barbarically) provided when importing this module. If you believe this module would better not print anything at import, please let me know.

| Variable Name      | Value                        | Unit                                |
|--------------------|------------------------------|-------------------------------------|
|                    |                              |                                     |
| Math Constants     |                              |                                     |
| pi                 | 3.141592653589790            |                                     |
| euler              | 2.718281828459050            |                                     |
|                    |                              |                                     |
| SI Metric Prefixes |                              |                                     |
| yotta              | 1E+24                        |                                     |
| zetta              | 1E+21                        |                                     |
| exa                | 1E+18                        |                                     |
| peta               | 1000000000000000.0           |                                     |
| tera               | 1000000000000.0              |                                     |
| giga               | 1000000000.0                 |                                     |
| mega               | 1000000.0                    |                                     |
| kilo               | 1000.0                       |                                     |
| hecto              | 100.0                        |                                     |
| deca               | 10.0                         |                                     |
| deci               | 0.1                          |                                     |
| centi              | 0.01                         |                                     |
| milli              | 0.001                        |                                     |
| micro              | 1E-06                        |                                     |
| nano               | 1E-09                        |                                     |
| pico               | 1E-12                        |                                     |
| femto              | 1E-15                        |                                     |
| atto               | 1E-18                        |                                     |
| zepto              | 1E-21                        |                                     |
| yocto              | 1E-24                        |                                     |
|                    |                              |                                     |
| Units              |                              |                                     |
| kg                 | 1                            | kg                                  |
| m                  | 1                            | m                                   |
| s                  | 1                            | s                                   |
| A                  | 1                            | A                                   |
| mol                | 1                            | mol                                 |
| K                  | 1                            | K                                   |
| Cd                 | 1                            | Cd                                  |
| Hz                 | 1.0                          | s\*\*-1                               |
| N                  | 1.0                          | kg \* m \* s\*\*-2                      |
| Pa                 | 1.0                          | kg \* m\*\*-1 \* s\*\*-2                  |
| J                  | 1.0                          | kg \* m\*\*2 \* s\*\*-2                   |
| W                  | 1.0                          | kg \* m\*\*2 \* s\*\*-3                   |
| C                  | 1                            | A \* s                               |
| V                  | 1.0                          | m\*\*2 \* A\*\*-1 \* kg \* s\*\*-3           |
| F                  | 1.0                          | kg\*\*-1 \* m\*\*-2 \* A\*\*2 \* s\*\*4        |
| T                  | 1.0                          | A\*\*-1 \* kg \* s\*\*-2                  |
| Wb                 | 1.0                          | A\*\*-1 \* kg \* m\*\*2 \* s\*\*-2           |
| Ohm                | 1.0                          | m\*\*2 \* A\*\*-2 \* kg \* s\*\*-3           |
| H                  | 1.0                          | m\*\*2 \* A\*\*-2 \* kg \* s\*\*-2           |
| ms                 | 0.001                        | s                                   |
| us                 | 1E-06                        | s                                   |
| ns                 | 1E-09                        | s                                   |
| minute             | 60                           | s                                   |
| hour               | 3600                         | s                                   |
| day                | 86400                        | s                                   |
| year               | 31557600.0                   | s                                   |
| dm                 | 0.1                          | m                                   |
| cm                 | 0.01                         | m                                   |
| mm                 | 0.001                        | m                                   |
| um                 | 1E-06                        | m                                   |
| nm                 | 1E-09                        | m                                   |
| fm                 | 1E-15                        | m                                   |
| km                 | 1000.0                       | m                                   |
| L                  | 0.0010000000000000000        | m\*\*3                                |
| kph                | 0.2777777777777780           | m \* s\*\*-1                           |
| mile               | 1609.344                     | m                                   |
| mph                | 0.44704                      | m \* s\*\*-1                           |
|                    |                              |                                     |
| Constants          |                              |                                     |
| c                  | 299792458.0                  | m \* s\*\*-1                           |
| h                  | 6.62607015E-34               | kg \* m\*\*2 \* s\*\*-1                   |
| hbar               | 1.05457181764616E-34         | kg \* m\*\*2 \* s\*\*-1                   |
| G                  | 6.6743E-11                   | kg\*\*-1 \* m\*\*3 \* s\*\*-2               |
| mu0                | 1.25663706212E-06            | m \* A\*\*-2 \* kg \* s\*\*-2              |
| epsilon0           | 8.85418781280039E-12         | kg\*\*-1 \* A\*\*2 \* m\*\*-3 \* s\*\*4        |
| e                  | 1.602176634E-19              | A \* s                               |
| NA                 | 6.02214076E+23               | mol\*\*-1                             |
| kB                 | 1.380649E-23                 | kg \* m\*\*2 \* s\*\*-2 \* K\*\*-1           |
| me                 | 9.1093837015E-31             | kg                                  |
| mp                 | 1.67262192369E-27            | kg                                  |
| mn                 | 1.67492749804E-27            | kg                                  |
| Da                 | 1.6605390666E-27             | kg                                  |
| u                  | 1.6605390666E-27             | kg                                  |
| R                  | 8.31446261815324             | m\*\*2 \* K\*\*-1 \* mol\*\*-1 \* kg \* s\*\*-2 |
| sigma              | 5.670374419E-08              | kg \* s\*\*-3 \* K\*\*-4                  |
| ly                 | 9460730472580800.0           | m                                   |
| g                  | 9.80665                      | m \* s\*\*-2                           |
| gram               | 0.001                        | kg                                  |
| k                  | 8987551792.26078             | A\*\*-2 \* kg \* m\*\*3 \* s\*\*-4           |
| eV                 | 1.602176634E-19              | kg \* m\*\*2 \* s\*\*-2                   |
| keV                | 1.602176634E-16              | kg \* m\*\*2 \* s\*\*-2                   |
| MeV                | 1.602176634E-13              | kg \* m\*\*2 \* s\*\*-2                   |
| GeV                | 1.602176634E-10              | kg \* m\*\*2 \* s\*\*-2                   |
| TeV                | 1.602176634E-07              | kg \* m\*\*2 \* s\*\*-2                   |
| MeVpc2             | 1.7826619216279E-30          | kg                                  |
| a0                 | 5.29177210906108E-11         | m                                   |
| hground            | -2.17987236108603E-18        | m\*\*2 \* kg \* s\*\*-2                   |
| Rinfty             | 10973731.568071600           | m\*\*-1                               |
| alpha              | 0.007297352569277710         |                                     |
