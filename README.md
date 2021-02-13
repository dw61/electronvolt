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

| Name                            | Symbol   | Value        | Unit                                               |
|---------------------------------|----------|--------------|----------------------------------------------------|
|                                 |          |              |                                                    |
| **Math Constants**              |          |              |                                                    |
|                                 | pi       | 3\.14159265  |                                                    |
| Euler's number                  | euler    | 2\.71828183  |                                                    |
|                                 |          |              |                                                    |
| **Metric Prefixes**             |          |              |                                                    |
|                                 | yotta    | 1\.00E\+24   |                                                    |
|                                 | zetta    | 1\.00E\+21   |                                                    |
|                                 | exa      | 1\.00E\+18   |                                                    |
|                                 | peta     | 1\.00E\+15   |                                                    |
|                                 | tera     | 1\.00E\+12   |                                                    |
|                                 | giga     | 1\.00E\+09   |                                                    |
|                                 | mega     | 1000000      |                                                    |
|                                 | kilo     | 1000         |                                                    |
|                                 | hecto    | 100          |                                                    |
|                                 | deca     | 10           |                                                    |
|                                 | deci     | 0\.1         |                                                    |
|                                 | centi    | 0\.01        |                                                    |
|                                 | milli    | 0\.001       |                                                    |
|                                 | micro    | 1\.00E\-06   |                                                    |
|                                 | nano     | 1\.00E\-09   |                                                    |
|                                 | pico     | 1\.00E\-12   |                                                    |
|                                 | femto    | 1\.00E\-15   |                                                    |
|                                 | atto     | 1\.00E\-18   |                                                    |
|                                 | zepto    | 1\.00E\-21   |                                                    |
|                                 | yocto    | 1\.00E\-24   |                                                    |
|                                 |          |              |                                                    |
| **Common Prefixes**             |          |              |                                                    |
|                                 | hundred  | 100          |                                                    |
|                                 | thousand | 1000         |                                                    |
|                                 | million  | 1000000      |                                                    |
|                                 | billion  | 1\.00E\+09   |                                                    |
|                                 | trillion | 1\.00E\+12   |                                                    |
|                                 |          |              |                                                    |
| **SI Base Units**               |          |              |                                                    |
| second                          | s        | 1            | s                                                  |
| meter                           | m        | 1            | m                                                  |
| kilogram                        | kg       | 1            | kg                                                 |
| ampere                          | A        | 1            | A                                                  |
| kelvin                          | K        | 1            | K                                                  |
| mole                            | mol      | 1            | mol                                                |
| candela                         | cd       | 1            | cd                                                 |
|                                 |          |              |                                                    |
| **Time**                        |          |              |                                                    |
|                                 | minute   | 60           | s                                                  |
|                                 | hour     | 3600         | s                                                  |
|                                 | day      | 86400        | s                                                  |
|                                 | week     | 604800       | s                                                  |
|                                 | year     | 31557600     | s                                                  |
| millisecond                     | ms       | 0\.001       | s                                                  |
| microsecond                     | us       | 1\.00E\-06   | s                                                  |
| nanosecond                      | ns       | 1\.00E\-09   | s                                                  |
|                                 |          |              |                                                    |
| **Length**                      |          |              |                                                    |
| kilometer                       | km       | 1000         | m                                                  |
| decimeter                       | dm       | 0\.1         | m                                                  |
| centimeter                      | cm       | 0\.01        | m                                                  |
| millimeter                      | mm       | 0\.001       | m                                                  |
| micrometer                      | um       | 1\.00E\-06   | m                                                  |
| nanometer                       | nm       | 1\.00E\-09   | m                                                  |
| femtometer                      | fm       | 1\.00E\-15   | m                                                  |
|                                 |          |              |                                                    |
| **Frequency**                   |          |              |                                                    |
| hertz                           | Hz       | 1            | s\*\*\-1                                           |
| kilohertz                       | kHz      | 1000         | s\*\*\-1                                           |
| megahertz                       | MHz      | 1000000      | s\*\*\-1                                           |
| gigahertz                       | GHz      | 1\.00E\+09   | s\*\*\-1                                           |
| terahertz                       | THz      | 1\.00E\+12   | s\*\*\-1                                           |
|                                 |          |              |                                                    |
| **Classical Mechanics**         |          |              |                                                    |
| gravitational acceleration      | g        | 9\.80665     | m \* s\*\*\-2                                      |
| newton                          | N        | 1            | kg \* m \* s\*\*\-2                                |
| pascal                          | Pa       | 1            | kg \* m\*\*\-1 \* s\*\*\-2                         |
| joule                           | J        | 1            | kg \* m\*\*2 \* s\*\*\-2                           |
| watt                            | W        | 1            | kg \* m\*\*2 \* s\*\*\-3                           |
|                                 |          |              |                                                    |
| **Thermodynamics**              |          |              |                                                    |
| Planck constant                 | h        | 6\.63E\-34   | kg \* m\*\*2 \* s\*\*\-1                           |
| reduced Planck constant         | hbar     | 1\.05E\-34   | kg \* m\*\*2 \* s\*\*\-1                           |
| Avogadro constant               | NA       | 6\.02E\+23   | mol\*\*\-1                                         |
| Boltzmann constant              | kB       | 1\.38E\-23   | kg \* m\*\*2 \* s\*\*\-2 \* K\*\*\-1               |
| ideal gas constant              | R        | 8\.31446262  | kg \* mol\*\*\-1 \* K\*\*\-1 \* m\*\*2 \* s\*\*\-2 |
|                                 |          |              |                                                    |
| **Electromagnetism**            |          |              |                                                    |
| coulomb                         | C        | 1            | s \* A                                             |
| volt                            | V        | 1            | kg \* A\*\*\-1 \* m\*\*2 \* s\*\*\-3               |
| farad                           | F        | 1            | kg\*\*\-1 \* A\*\*2 \* m\*\*\-2 \* s\*\*4          |
|                                 | Ohm      | 1            | kg \* A\*\*\-2 \* m\*\*2 \* s\*\*\-3               |
| tesla                           | T        | 1            | kg \* A\*\*\-1 \* s\*\*\-2                         |
| weber                           | Wb       | 1            | kg \* m\*\*2 \* s\*\*\-2 \* A\*\*\-1               |
| henry                           | H        | 1            | kg \* A\*\*\-2 \* m\*\*2 \* s\*\*\-2               |
| speed of light                  | c        | 299792458    | m \* s\*\*\-1                                      |
| vacuum magnetic permeability    | mu0      | 1\.26E\-06   | kg \* A\*\*\-2 \* m \* s\*\*\-2                    |
| vacuum electric permittivity    | epsilon0 | 8\.85E\-12   | kg\*\*\-1 \* m\*\*\-3 \* s\*\*4 \* A\*\*2          |
| Coulomb constant                | k        | 8\.99E\+09   | kg \* m\*\*3 \* s\*\*\-4 \* A\*\*\-2               |
| elementary charge               | e        | 1\.60E\-19   | s \* A                                             |
|                                 |          |              |                                                    |
| **Imperial Units**              |          |              |                                                    |
|                                 | inch     | 0\.0254      | m                                                  |
|                                 | foot     | 0\.3048      | m                                                  |
|                                 | yard     | 0\.9144      | m                                                  |
|                                 | mile     | 1609\.344    | m                                                  |
| pound-mass                      | lb       | 0\.45359237  | kg                                                 |
| pound-force                     | lbf      | 4\.44822162  | kg \* m \* s\*\*\-2                                |
|                                 | slug     | 14\.5939029  | kg                                                 |
|                                 | blob     | 175\.126835  | kg                                                 |
|                                 |          |              |                                                    |
| **Common Units**                |          |              |                                                    |
| kilometer per hour              | kph      | 0\.277777778 | m \* s\*\*\-1                                      |
| miles per hour                  | mph      | 0\.44704     | m \* s\*\*\-1                                      |
|                                 | gram     | 0\.001       | kg                                                 |
| liter                           | L        | 0\.001       | m\*\*3                                             |
| pound per square inch           | psi      | 6894\.757    | kg \* m\*\*\-1 \* s\*\*\-2                         |
| kilowatt-hour                   | kWh      | 3600000      | kg \* m\*\*2 \* s\*\*\-2                           |
|                                 |          |              |                                                    |
| **Atomic Physics**              |          |              |                                                    |
| electron rest mass              | me       | 9\.11E\-31   | kg                                                 |
| proton mass                     | mp       | 1\.67E\-27   | kg                                                 |
| neutron mass                    | mn       | 1\.67E\-27   | kg                                                 |
| atomic mass unit                | u        | 1\.66E\-27   | kg                                                 |
| atomic mass of hydrogen         | mH       | 1\.67E\-27   | kg                                                 |
| atomic mass of helium           | mHe      | 6\.65E\-27   | kg                                                 |
|                                 |          |              |                                                    |
| **Quantum Mechanics**           |          |              |                                                    |
| Stefan-Boltzmann constant       | sigma    | 5\.67E\-08   | kg \* K\*\*\-4 \* s\*\*\-3                         |
| Bohr radius                     | a0       | 5\.29E\-11   | m                                                  |
| hydrogen ground state energy    | hground  | \-2\.18E\-18 | kg \* m\*\*2 \* s\*\*\-2                           |
| fine-structure constant         | alpha    | 0\.007297353 |                                                    |
| Rydberg constant                | Rinfty   | 10973731\.6  | m\*\*\-1                                           |
|                                 |          |              |                                                    |
| **Radioactive Decays**          |          |              |                                                    |
| becquerel                       | Bq       | 1            | s\*\*\-1                                           |
| curie                           | Ci       | 3\.70E\+10   | s\*\*\-1                                           |
| millicurie                      | mCi      | 37000000     | s\*\*\-1                                           |
| microcurie                      | uCi      | 37000        | s\*\*\-1                                           |
|                                 |          |              |                                                    |
| **Nuclear Physics**             |          |              |                                                    |
| electronvolt                    | eV       | 1\.60E\-19   | kg \* m\*\*2 \* s\*\*\-2                           |
| kilo-electronvolt               | keV      | 1\.60E\-16   | kg \* m\*\*2 \* s\*\*\-2                           |
| mega-electronvolt               | MeV      | 1\.60E\-13   | kg \* m\*\*2 \* s\*\*\-2                           |
| giga-electronvolt               | GeV      | 1\.60E\-10   | kg \* m\*\*2 \* s\*\*\-2                           |
| tera-electronvolt               | TeV      | 1\.60E\-07   | kg \* m\*\*2 \* s\*\*\-2                           |
| electronvolt per speed of light | eVpc     | 5\.34E\-28   | kg \* m \* s\*\*\-1                                |
| mega-electronvolt per c         | MeVpc    | 5\.34E\-22   | kg \* m \* s\*\*\-1                                |
| electronvolt per c squared      | eVpc2    | 1\.78E\-36   | kg                                                 |
| mega-electronvolt per c squared | MeVpc2   | 1\.78E\-30   | kg                                                 |
|                                 |          |              |                                                    |
| **Cosmology**                   |          |              |                                                    |
| gravitational constant          | G        | 6\.67E\-11   | kg\*\*\-1 \* m\*\*3 \* s\*\*\-2                    |
| astronomical unit               | au       | 1\.50E\+11   | m                                                  |
| light-year                      | ly       | 9\.46E\+15   | m                                                  |
| parsec                          | pc       | 3\.09E\+16   | m                                                  |
| megaparsec                      | Mpc      | 3\.09E\+22   | m                                                  |
| Hubble parameter                | H0       | 2\.33E\-18   | s\*\*\-1                                           |
