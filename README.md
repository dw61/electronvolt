## Demo

#### Rest mass of an electron

```
>>> me
9.1093837015e-31 kg
```

#### Speed of light

```
>>> c
299792458.0 m * s**-1
```

#### Rest energy of an electron

```
>>> me * c**2
8.187105776823886e-14 m**2 * s**-2 * kg
```

#### In mega electronvolts

```
>>> me * c**2 / MeV
0.5109989499961642
```

This matches the rest energy of electron on [Wikipedia](https://en.wikipedia.org/wiki/Electron_rest_mass).

## Usage

* Install this module via `pip install electronvolt`.
* Recommended to use in an interactive python environment, e.g. jupyter notebook.
* Recommended to import via `from electronvolt import *`.

#### You can also run this module online [**HERE**](https://mybinder.org/v2/gh/dw61/electronvolt/HEAD?filepath=online.ipynb).

* This page typically loads in 3 minutes.
* Use shift+enter to run a block of code.
* Run the first block to initialize the calculator.
* Run the second block to feel how it works.

## Units and Constants

| Variable Name             | Value        | Unit                                               |
|---------------------------|--------------|----------------------------------------------------|
| **Math Constants**        |              |                                                    |
| pi                        | 3\.14159265  |                                                    |
| euler                     | 2\.71828183  |                                                    |
|                           |              |                                                    |
| **Metric Prefixes**       |              |                                                    |
| yotta                     | 1\.00E\+24   |                                                    |
| zetta                     | 1\.00E\+21   |                                                    |
| exa                       | 1\.00E\+18   |                                                    |
| peta                      | 1\.00E\+15   |                                                    |
| tera                      | 1\.00E\+12   |                                                    |
| giga                      | 1\.00E\+09   |                                                    |
| mega                      | 1000000      |                                                    |
| kilo                      | 1000         |                                                    |
| hecto                     | 100          |                                                    |
| deca                      | 10           |                                                    |
| deci                      | 0\.1         |                                                    |
| centi                     | 0\.01        |                                                    |
| milli                     | 0\.001       |                                                    |
| micro                     | 1\.00E\-06   |                                                    |
| nano                      | 1\.00E\-09   |                                                    |
| pico                      | 1\.00E\-12   |                                                    |
| femto                     | 1\.00E\-15   |                                                    |
| atto                      | 1\.00E\-18   |                                                    |
| zepto                     | 1\.00E\-21   |                                                    |
| yocto                     | 1\.00E\-24   |                                                    |
|                           |              |                                                    |
| **Other Prefixes**        |              |                                                    |
| hundred                   | 100          |                                                    |
| thousand                  | 1000         |                                                    |
| million                   | 1000000      |                                                    |
| billion                   | 1\.00E\+09   |                                                    |
| trillion                  | 1\.00E\+12   |                                                    |
|                           |              |                                                    |
| **SI Units**              |              |                                                    |
| s                         | 1            | s                                                  |
| m                         | 1            | m                                                  |
| kg                        | 1            | kg                                                 |
| A                         | 1            | A                                                  |
| K                         | 1            | K                                                  |
| mol                       | 1            | mol                                                |
| cd                        | 1            | cd                                                 |
|                           |              |                                                    |
| **Time**                  |              |                                                    |
| minute                    | 60           | s                                                  |
| hour                      | 3600         | s                                                  |
| day                       | 86400        | s                                                  |
| week                      | 604800       | s                                                  |
| year                      | 31557600     | s                                                  |
| ms                        | 0\.001       | s                                                  |
| us                        | 1\.00E\-06   | s                                                  |
| ns                        | 1\.00E\-09   | s                                                  |
|                           |              |                                                    |
| **Length**                |              |                                                    |
| km                        | 1000         | m                                                  |
| dm                        | 0\.1         | m                                                  |
| cm                        | 0\.01        | m                                                  |
| mm                        | 0\.001       | m                                                  |
| um                        | 1\.00E\-06   | m                                                  |
| nm                        | 1\.00E\-09   | m                                                  |
| fm                        | 1\.00E\-15   | m                                                  |
|                           |              |                                                    |
| **Frequency**             |              |                                                    |
| Hz                        | 1            | s\*\*\-1                                           |
| kHz                       | 1000         | s\*\*\-1                                           |
| MHz                       | 1000000      | s\*\*\-1                                           |
| GHz                       | 1\.00E\+09   | s\*\*\-1                                           |
| THz                       | 1\.00E\+12   | s\*\*\-1                                           |
|                           |              |                                                    |
| **Classical Mechanics**   |              |                                                    |
| g                         | 9\.80665     | m \* s\*\*\-2                                      |
| N                         | 1            | kg \* m \* s\*\*\-2                                |
| Pa                        | 1            | kg \* m\*\*\-1 \* s\*\*\-2                         |
| J                         | 1            | kg \* m\*\*2 \* s\*\*\-2                           |
| W                         | 1            | kg \* m\*\*2 \* s\*\*\-3                           |
|                           |              |                                                    |
| **Thermodynamics**        |              |                                                    |
| h                         | 6\.63E\-34   | kg \* m\*\*2 \* s\*\*\-1                           |
| hbar                      | 1\.05E\-34   | kg \* m\*\*2 \* s\*\*\-1                           |
| NA                        | 6\.02E\+23   | mol\*\*\-1                                         |
| kB                        | 1\.38E\-23   | kg \* m\*\*2 \* s\*\*\-2 \* K\*\*\-1               |
| R                         | 8\.31446262  | kg \* mol\*\*\-1 \* K\*\*\-1 \* m\*\*2 \* s\*\*\-2 |
|                           |              |                                                    |
| **Electromagnetism**      |              |                                                    |
| C                         | 1            | s \* A                                             |
| V                         | 1            | kg \* A\*\*\-1 \* m\*\*2 \* s\*\*\-3               |
| F                         | 1            | kg\*\*\-1 \* A\*\*2 \* m\*\*\-2 \* s\*\*4          |
| Ohm                       | 1            | kg \* A\*\*\-2 \* m\*\*2 \* s\*\*\-3               |
| T                         | 1            | kg \* A\*\*\-1 \* s\*\*\-2                         |
| Wb                        | 1            | kg \* m\*\*2 \* s\*\*\-2 \* A\*\*\-1               |
| H                         | 1            | kg \* A\*\*\-2 \* m\*\*2 \* s\*\*\-2               |
| c                         | 299792458    | m \* s\*\*\-1                                      |
| mu0                       | 1\.26E\-06   | kg \* A\*\*\-2 \* m \* s\*\*\-2                    |
| epsilon0                  | 8\.85E\-12   | kg\*\*\-1 \* m\*\*\-3 \* s\*\*4 \* A\*\*2          |
| k                         | 8\.99E\+09   | kg \* m\*\*3 \* s\*\*\-4 \* A\*\*\-2               |
| e                         | 1\.60E\-19   | s \* A                                             |
|                           |              |                                                    |
| **Everyday Life**         |              |                                                    |
| mile                      | 1609\.344    | m                                                  |
| kph                       | 0\.277777778 | m \* s\*\*\-1                                      |
| mph                       | 0\.44704     | m \* s\*\*\-1                                      |
| gram                      | 0\.001       | kg                                                 |
| L                         | 0\.001       | m\*\*3                                             |
| kWh                       | 3600000      | kg \* m\*\*2 \* s\*\*\-2                           |
|                           |              |                                                    |
| **Atomic Physics**        |              |                                                    |
| me                        | 9\.11E\-31   | kg                                                 |
| mp                        | 1\.67E\-27   | kg                                                 |
| mn                        | 1\.67E\-27   | kg                                                 |
| u                         | 1\.66E\-27   | kg                                                 |
| mH                        | 1\.67E\-27   | kg                                                 |
| mHe                       | 6\.65E\-27   | kg                                                 |
|                           |              |                                                    |
| **Quantum Mechanics**     |              |                                                    |
| sigma                     | 5\.67E\-08   | kg \* K\*\*\-4 \* s\*\*\-3                         |
| a0                        | 5\.29E\-11   | m                                                  |
| hground                   | \-2\.18E\-18 | kg \* m\*\*2 \* s\*\*\-2                           |
| alpha                     | 0\.007297353 |                                                    |
| Rinfty                    | 10973731\.6  | m\*\*\-1                                           |
|                           |              |                                                    |
| **Radioactive Decay**     |              |                                                    |
| Bq                        | 1            | s\*\*\-1                                           |
| Ci                        | 3\.70E\+10   | s\*\*\-1                                           |
| mCi                       | 37000000     | s\*\*\-1                                           |
| uCi                       | 37000        | s\*\*\-1                                           |
|                           |              |                                                    |
| **Nuclear Physics**       |              |                                                    |
| eV                        | 1\.60E\-19   | kg \* m\*\*2 \* s\*\*\-2                           |
| keV                       | 1\.60E\-16   | kg \* m\*\*2 \* s\*\*\-2                           |
| MeV                       | 1\.60E\-13   | kg \* m\*\*2 \* s\*\*\-2                           |
| GeV                       | 1\.60E\-10   | kg \* m\*\*2 \* s\*\*\-2                           |
| TeV                       | 1\.60E\-07   | kg \* m\*\*2 \* s\*\*\-2                           |
| eVpc                      | 5\.34E\-28   | kg \* m \* s\*\*\-1                                |
| MeVpc                     | 5\.34E\-22   | kg \* m \* s\*\*\-1                                |
| eVpc2                     | 1\.78E\-36   | kg                                                 |
| MeVpc2                    | 1\.78E\-30   | kg                                                 |
|                           |              |                                                    |
| **Cosmology**             |              |                                                    |
| G                         | 6\.67E\-11   | kg\*\*\-1 \* m\*\*3 \* s\*\*\-2                    |
| au                        | 1\.50E\+11   | m                                                  |
| ly                        | 9\.46E\+15   | m                                                  |
| pc                        | 3\.09E\+16   | m                                                  |
| Mpc                       | 3\.09E\+22   | m                                                  |
| H0                        | 2\.33E\-18   | s\*\*\-1                                           |
