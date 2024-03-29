# Demo

#### Import module
```python
>>> from electronvolt import *
```

#### Rest mass of an electron
```python
>>> me
9.1093837015e-31 * kg
```

#### Rest energy of the electron, in [SI](https://en.wikipedia.org/wiki/International_System_of_Units) units
```python
>>> me * c**2
8.187105776823886e-14 * m**2 * s**-2 * kg
```

#### In mega electronvolts
```python
>>> me * c**2 / MeV
0.5109989499961642
```

This matches the electron rest energy on [Wikipedia](https://en.wikipedia.org/wiki/Electron_rest_mass).

# Usage

Install via `pip install electronvolt`.

#### Alternatively, run this module [online](https://mybinder.org/v2/gh/dw61/electronvolt/HEAD?filepath=online.ipynb)
* Typically loads within 3 minutes.
* Shift+enter to run a block of code. Run first block to initialize the calculator.

# Units and Constants

|Name                           |Symbol    |Value               |Unit                         |
|-------------------------------|----------|--------------------|-----------------------------|
|                               |          |                    |                             |
|**Math Constants**             |          |                    |                             |
|                               |`pi`      |3.141592653589793   |                             |
|Euler's number                 |`euler`   |2.718281828459045   |                             |
|                               |          |                    |                             |
|**Metric Prefixes**            |          |                    |                             |
|                               |`yotta`   |1 `e+24`            |                             |
|                               |`zetta`   |1 `e+21`            |                             |
|                               |`exa`     |1 `e+18`            |                             |
|                               |`peta`    |1 `e+15`            |                             |
|                               |`tera`    |1 `e+12`            |                             |
|                               |`giga`    |1 `e+09`            |                             |
|                               |`mega`    |1000000             |                             |
|                               |`kilo`    |1000                |                             |
|                               |`hecto`   |100                 |                             |
|                               |`deca`    |10                  |                             |
|                               |`deci`    |0.1                 |                             |
|                               |`centi`   |0.01                |                             |
|                               |`milli`   |0.001               |                             |
|                               |`micro`   |1 `e-06`            |                             |
|                               |`nano`    |1 `e-09`            |                             |
|                               |`pico`    |1 `e-12`            |                             |
|                               |`femto`   |1 `e-15`            |                             |
|                               |`atto`    |1 `e-18`            |                             |
|                               |`zepto`   |1 `e-21`            |                             |
|                               |`yocto`   |1 `e-24`            |                             |
|                               |          |                    |                             |
|**Common Prefixes**            |          |                    |                             |
|                               |`hundred` |100                 |                             |
|                               |`thousand`|1000                |                             |
|                               |`million` |1000000             |                             |
|                               |`billion` |1 `e+09`            |                             |
|                               |`trillion`|1 `e+12`            |                             |
|                               |          |                    |                             |
|**SI Base Units**              |          |                    |                             |
|second                         |`s`       |1                   |`s`                          |
|meter                          |`m`       |1                   |`m`                          |
|kilogram                       |`kg`      |1                   |`kg`                         |
|ampere                         |`A`       |1                   |`A`                          |
|kelvin                         |`K`       |1                   |`K`                          |
|mole                           |`mol`     |1                   |`mol`                        |
|candela                        |`cd`      |1                   |`cd`                         |
|                               |          |                    |                             |
|**Time**                       |          |                    |                             |
|                               |`minute`  |60                  |`s`                          |
|                               |`hour`    |3600                |`s`                          |
|                               |`day`     |86400               |`s`                          |
|                               |`week`    |604800              |`s`                          |
|                               |`year`    |31557600            |`s`                          |
|millisecond                    |`ms`      |0.001               |`s`                          |
|microsecond                    |`us`      |1 `e-06`            |`s`                          |
|nanosecond                     |`ns`      |1 `e-09`            |`s`                          |
|                               |          |                    |                             |
|**Length**                     |          |                    |                             |
|kilometer                      |`km`      |1000                |`m`                          |
|decimeter                      |`dm`      |0.1                 |`m`                          |
|centimeter                     |`cm`      |0.01                |`m`                          |
|millimeter                     |`mm`      |0.001               |`m`                          |
|micrometer                     |`um`      |1 `e-06`            |`m`                          |
|nanometer                      |`nm`      |1 `e-09`            |`m`                          |
|picometer                      |`pm`      |1 `e-12`            |`m`                          |
|femtometer                     |`fm`      |1 `e-15`            |`m`                          |
|                               |          |                    |                             |
|**Frequency**                  |          |                    |                             |
|hertz                          |`Hz`      |1                   |`s-1`                        |
|kilohertz                      |`kHz`     |1000                |`s-1`                        |
|megahertz                      |`MHz`     |1000000             |`s-1`                        |
|gigahertz                      |`GHz`     |1 `e+09`            |`s-1`                        |
|terahertz                      |`THz`     |1 `e+12`            |`s-1`                        |
|                               |          |                    |                             |
|**Classical Mechanics**        |          |                    |                             |
|gravitational acceleration     |`g`       |9.80665             |`m` `s-2`                    |
|newton                         |`N`       |1                   |`kg` `m` `s-2`               |
|pascal                         |`Pa`      |1                   |`kg` `m-1` `s-2`             |
|joule                          |`J`       |1                   |`kg` `m2` `s-2`              |
|watt                           |`W`       |1                   |`kg` `m2` `s-3`              |
|                               |          |                    |                             |
|**Thermodynamics**             |          |                    |                             |
|Planck constant                |`h`       |6.62607015 `e-34`   |`kg` `m2` `s-1`              |
|reduced Planck constant        |`hbar`    |1.05457181765 `e-34`|`kg` `m2` `s-1`              |
|Avogadro constant              |`NA`      |6.02214076 `e+23`   |`mol-1`                      |
|Boltzmann constant             |`kB`      |1.380649 `e-23`     |`kg` `m2` `s-2` `K-1`        |
|ideal gas constant             |`R`       |8.31446261815324    |`kg` `mol-1` `K-1` `m2` `s-2`|
|                               |          |                    |                             |
|**Electromagnetism**           |          |                    |                             |
|coulomb                        |`C`       |1                   |`s` `A`                      |
|volt                           |`V`       |1                   |`kg` `A-1` `m2` `s-3`        |
|farad                          |`F`       |1                   |`kg-1` `A2` `m-2` `s4`       |
|                               |`Ohm`     |1                   |`kg` `A-2` `m2` `s-3`        |
|tesla                          |`T`       |1                   |`kg` `A-1` `s-2`             |
|weber                          |`Wb`      |1                   |`kg` `m2` `s-2` `A-1`        |
|henry                          |`H`       |1                   |`kg` `A-2` `m2` `s-2`        |
|speed of light                 |`c`       |299792458           |`m` `s-1`                    |
|vacuum magnetic permeability   |`mu0`     |1.25663706212 `e-06`|`kg` `A-2` `m` `s-2`         |
|vacuum electric permittivity   |`epsilon0`|8.8541878128 `e-12` |`kg-1` `m-3` `s4` `A2`       |
|Coulomb constant               |`k`       |8987551792.26078    |`kg` `m3` `s-4` `A-2`        |
|elementary charge              |`e`       |1.602176634 `e-19`  |`s` `A`                      |
|                               |          |                    |                             |
|**Imperial Units**             |          |                    |                             |
|inch ('in' is a python keyword)|`in_`     |0.0254              |`m`                          |
|foot                           |`ft`      |0.3048              |`m`                          |
|yard                           |`yd`      |0.9144              |`m`                          |
|mile                           |`mi`      |1609.344            |`m`                          |
|                               |`acre`    |4046.8564224        |`m2`                         |
|nautical mile                  |`NM`      |1852                |`m`                          |
|knot                           |`kn`      |0.514444444444445   |`m` `s-1`                    |
|US gallon                      |`gal`     |0.003785411784      |`m3`                         |
|pound-mass                     |`lb`      |0.45359237          |`kg`                         |
|pound-force                    |`lbf`     |4.4482216152605     |`kg` `m` `s-2`               |
|                               |`slug`    |14.59390293720637   |`kg`                         |
|                               |`blob`    |175.1268352464764   |`kg`                         |
|                               |          |                    |                             |
|**Common Units**               |          |                    |                             |
|kilometer per hour             |`kph`     |0.277777777777778   |`m` `s-1`                    |
|miles per hour                 |`mph`     |0.44704             |`m` `s-1`                    |
|                               |`gram`    |0.001               |`kg`                         |
|liter                          |`L`       |0.001               |`m3`                         |
|pound per square inch          |`psi`     |6894.757            |`kg` `m-1` `s-2`             |
|kilowatt-hour                  |`kWh`     |3600000             |`kg` `m2` `s-2`              |
|hectare                        |`ha`      |10000               |`m2`                         |
|                               |          |                    |                             |
|**Atomic Physics**             |          |                    |                             |
|electron rest mass             |`me`      |9.1093837015 `e-31` |`kg`                         |
|proton mass                    |`mp`      |1.67262192369 `e-27`|`kg`                         |
|neutron mass                   |`mn`      |1.67492749804 `e-27`|`kg`                         |
|atomic mass unit               |`u`       |1.6605390666 `e-27` |`kg`                         |
|atomic mass of hydrogen        |`mH`      |1.6735327848 `e-27` |`kg`                         |
|atomic mass of helium          |`mHe`     |6.64647698905 `e-27`|`kg`                         |
|                               |          |                    |                             |
|**Quantum Mechanics**          |          |                    |                             |
|Stefan-Boltzmann constant      |`sigma`   |5.67037441918 `e-08`|`kg` `K-4` `s-3`             |
|Bohr radius                    |`a0`      |5.29177210906 `e-11`|`m`                          |
|hydrogen ground state energy   |`hground` |-2.1798723611 `e-18`|`kg` `m2` `s-2`              |
|fine-structure constant        |`alpha`   |0.007297352569278   |                             |
|Rydberg constant               |`Rydberg` |10973731.56807162   |`m-1`                        |
|                               |          |                    |                             |
|**Radioactive Decays**         |          |                    |                             |
|becquerel                      |`Bq`      |1                   |`s-1`                        |
|curie                          |`Ci`      |3.7 `e+10`          |`s-1`                        |
|millicurie                     |`mCi`     |37000000            |`s-1`                        |
|microcurie                     |`uCi`     |37000               |`s-1`                        |
|                               |          |                    |                             |
|**Nuclear Physics**            |          |                    |                             |
|electronvolt                   |`eV`      |1.602176634 `e-19`  |`kg` `m2` `s-2`              |
|kilo-electronvolt              |`keV`     |1.602176634 `e-16`  |`kg` `m2` `s-2`              |
|mega-electronvolt              |`MeV`     |1.602176634 `e-13`  |`kg` `m2` `s-2`              |
|giga-electronvolt              |`GeV`     |1.602176634 `e-10`  |`kg` `m2` `s-2`              |
|tera-electronvolt              |`TeV`     |1.602176634 `e-07`  |`kg` `m2` `s-2`              |
|electronvolt per speed of light|`eVpc`    |5.34428599268 `e-28`|`kg` `m` `s-1`               |
|mega-electronvolt per c        |`MeVpc`   |5.34428599268 `e-22`|`kg` `m` `s-1`               |
|electronvolt per c squared     |`eVpc2`   |1.78266192163 `e-36`|`kg`                         |
|mega-electronvolt per c squared|`MeVpc2`  |1.78266192163 `e-30`|`kg`                         |
|                               |          |                    |                             |
|**Cosmology**                  |          |                    |                             |
|gravitational constant         |`G`       |6.6743 `e-11`       |`kg-1` `m3` `s-2`            |
|astronomical unit              |`au`      |149597870700        |`m`                          |
|light-year                     |`ly`      |9460730472580800    |`m`                          |
|parsec                         |`pc`      |3.08567758149 `e+16`|`m`                          |
|megaparsec                     |`Mpc`     |3.08567758149 `e+22`|`m`                          |
|Hubble parameter               |`H0`      |2.3333610884 `e-18` |`s-1`                        |

# More Demo

#### Import `ufloat` from [uncertainties](https://github.com/lebigot/uncertainties)
```python
>>> from uncertainties import ufloat
```

#### Rest mass of an electron
```python
>>> me = ufloat(9.1093837015, 0.0000000028) * 1e-31 * kg
```

#### Rest energy of the electron
```python
>>> me * c**2
(8.1871057768+/-0.0000000025)e-14 * kg * s**-2 * m**2
```

This matches the electron rest energy on the [same](https://en.wikipedia.org/wiki/Electron_rest_mass) Wikipedia page.
