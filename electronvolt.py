from math import pi
from math import e as euler # prevent duplicating elementary charge
from math import log as ln # log defaults to ln
from math import exp, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, degrees, radians

# unit converter

class Unit:

    def __init__(self, d):
        self.d = {}
        for unit, power in d.items():
            if power: # remove zero power
                self.d[unit] = power

    def __repr__(self): # for commandline convenience. __str__ redirects here
        terms = []
        for unit, power in self.d.items():
            if power == 1:
                terms.append(unit)
            else:
                terms.append(f"{unit}**{power}")
        return " * ".join(terms)

    def __eq__(self, other):
        return self.d == other.d

    def __mul__(self, other):
        d = {}
        for unit in set(self.d) | set(other.d):
            d[unit] = self.d.get(unit, 0) + other.d.get(unit, 0)
        return Unit(d)

    def __truediv__(self, other):
        d = {}
        for unit in set(self.d) | set(other.d):
            d[unit] = self.d.get(unit, 0) - other.d.get(unit, 0)
        return Unit(d)

    def __pow__(self, p):
        d = {}
        for unit, power in self.d.items():
            d[unit] = power * p
        return Unit(d)

    def __bool__(self):
        return bool(self.d)

# physical quantity calculator

class Quantity:

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __repr__(self):
        if not self.unit:
            return repr(self.value)
        return f"{self.value} * {self.unit}"

    def __eq__(self, other):
        if not isinstance(other, Quantity): # not considering 0*kg == 0
            return False # Quantity != dimensionless
        return self.value == other.value and self.unit == other.unit

    def __lt__(self, other):
        assert self.unit == other.unit, f"'<' undefined between '{self.unit}' and '{other.unit}'"
        return self.value < other.value

    def __gt__(self, other):
        assert self.unit == other.unit, f"'>' undefined between '{self.unit}' and '{other.unit}'"
        return self.value > other.value

    def __le__(self, other):
        assert self.unit == other.unit, f"'<=' undefined between '{self.unit}' and '{other.unit}'"
        return self.value <= other.value

    def __ge__(self, other):
        assert self.unit == other.unit, f"'>=' undefined between '{self.unit}' and '{other.unit}'"
        return self.value >= other.value

    def __add__(self, other):
        assert isinstance(other, Quantity), f"Addition undefined between '{self.unit}' and ''"
        assert self.unit == other.unit, f"Addition undefined between '{self.unit}' and '{other.unit}'"
        return quantity(self.value + other.value, self.unit)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        assert isinstance(other, Quantity), f"Subtraction undefined between '{self.unit}' and ''"
        assert self.unit == other.unit, f"Subtraction undefined between '{self.unit}' and '{other.unit}'"
        return quantity(self.value - other.value, self.unit)

    def __rsub__(self, other): # calls __neg__
        return -(self - other) # self.__rsub__(other) becomes -self.__sub__(other)

    def __neg__(self):
        return quantity(-self.value, self.unit)

    def __mul__(self, other): # both kg*10 and kg*m works
        if not isinstance(other, Quantity):
            return quantity(self.value * other, self.unit)
        return quantity(self.value * other.value, self.unit * other.unit)

    def __rmul__(self, other): # handles 10*kg
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Quantity):
            return quantity(self.value / other, self.unit)
        return quantity(self.value / other.value, self.unit / other.unit)

    def __rtruediv__(self, other):
        return (self / other) ** -1

    def __pow__(self, exponent):
        return quantity(self.value ** exponent, self.unit ** exponent)

    def __rpow__(self, base): # handles euler ** (1*s/s)
        assert not self.unit, f"Exponent cannot have unit '{self.unit}'"
        return base ** self.value

    def __contains__(self, other):
        return self.unit == other.unit # sloppy. not doing .convert()

    def __bool__(self):
        return bool(self.value)

# wrapper

def quantity(value=1, unit=None): # returns Quantity
    if not unit: # Quantity cannot be dimensionless
        return value # value can be any type
    return Quantity(value, unit)

def unit(unit): # returns Quantity, despite its name
    return quantity(1, Unit({unit : 1}))

# trigonometric functions

# sin, provided by math, input in radians
# cos
# tan
csc = lambda x : 1 / sin(x)
sec = lambda x : 1 / cos(x)
cot = lambda x : 1 / tan(x)
# asin, return in radians
# acos
# atan
acsc = lambda x : asin(1 / x)
asec = lambda x : acos(1 / x)
acot = lambda x : atan(1 / x)

sind = lambda x : sin(radians(x)) # input in degrees
cosd = lambda x : cos(radians(x))
tand = lambda x : tan(radians(x))
cscd = lambda x : csc(radians(x))
secd = lambda x : sec(radians(x))
cotd = lambda x : cot(radians(x))
asind = lambda x : degrees(asin(x)) # return in degrees
acosd = lambda x : degrees(acos(x))
atand = lambda x : degrees(atan(x))
acscd = lambda x : degrees(acsc(x))
asecd = lambda x : degrees(asec(x))
acotd = lambda x : degrees(acot(x))

# sinh, hyperbolic functions
# cosh
# tanh
csch = lambda x : 1 / sinh(x)
sech = lambda x : 1 / cosh(x)
coth = lambda x : 1 / tanh(x)
# asinh
# acosh
# atanh
acsch = lambda x : asinh(1 / x)
asech = lambda x : acosh(1 / x)
acoth = lambda x : atanh(1 / x)

# prefixes

yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deca = 1e1

deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24

hundred = hecto
thousand = kilo
million = mega
billion = giga
trillion = tera

# units and constants

s = unit("s")
m = unit("m")
kg = unit("kg")
A = unit("A")
K = unit("K")
mol = unit("mol")
cd = unit("cd")

minute = 60 * s
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365.25 * day # average year
ms = milli * s
us = micro * s # microsecond
ns = nano * s

km = kilo * m
dm = deci * m
cm = centi * m
mm = milli * m
um = micro * m # micrometer
nm = nano * m
pm = pico * m
fm = femto * m # fermi

Hz = s**-1 # Hertz
kHz = kilo * Hz
MHz = mega * Hz
GHz = giga * Hz
THz = tera * Hz

g = 9.80665 * m / s**2 # gravitational acceleration
N = kg * m / s**2 # Newton
Pa = N / m**2 # Pascal
J = N * m # Joule
W = J / s # Watt

h = 6.62607015e-34 * J * s # Planck constant
hbar = h / (2 * pi) # reduced Planck constant
NA = 6.02214076e23 * mol**-1 # Avogadro constant
kB = 1.380649e-23 * J / K # Boltzmann constant
R = NA * kB # ideal gas constant

C = A * s # Coulomb
V = J / C # Volt
F = C / V # Farad
Ohm = V / A # Ohm
T = V * s / m**2 # Tesla
Wb = T * m**2 # Weber
H = Ohm * s # Joseph Henry
c = 299792458 * m / s # speed of light
mu0 = 1.25663706212e-6 * H / m # vacuum magnetic permeability
epsilon0 = 1 / (mu0 * c**2) # vacuum electric permittivity
k = 1 / (4 * pi * epsilon0) # Coulomb constant
e = 1.602176634e-19 * C # elementary charge

in_ = 25.4 * mm # "in" is a python keyword
ft = 12 * in_
yd = 3 * ft
mi = 1760 * yd
acre = (66 * ft) * (660 * ft)
NM = 1852 * m # nautical mile
kn = NM / hour # knot
gal = 231 * in_**3 # US gallon

lb = 0.45359237 * kg # pound mass
lbf = lb * g # pound force
slug = lbf * s**2 / ft # imperial unit of mass
blob = lbf * s**2 / in_ # imperial unit of mass

kph = km / hour # kilometer per hour
mph = mi / hour # miles per hour
gram = kg / kilo # gram
L = dm**3 # liter
psi = 6.894757 * kilo * Pa # pound per square inch
kWh = kilo * W * hour # kilowatt-hour
ha = (hecto * m) ** 2 # hectare

me = 9.1093837015e-31 * kg # electron mass
mp = 1.67262192369e-27 * kg # proton mass
mn = 1.67492749804e-27 * kg # neutron mass
u = 1.66053906660e-27 * kg # atomic mass unit, 1/12 atomic mass of carbon 12
mH = 1.007825 * u # atomic mass of hydrogen
mHe = 4.002602 * u # atomic mass of helium

sigma = pi**2 * kB**4 / (60 * hbar**3 * c**2) # Stefan-Boltzmann constant
a0 = 4 * pi * epsilon0 * hbar**2 / (me * e**2) # Bohr radius
hground = -me * e**4 / (8 * h**2 * epsilon0**2) # hydrogen ground state energy
alpha = e**2 / (4 * pi * epsilon0 * hbar * c) # fine structure constant
Rydberg = alpha**2 * me * c / (2 * h) # Rydberg constant

Bq = s**-1 # Becquerel
Ci = 3.7e10 * Bq # Curie, radioactive decay
mCi = milli * Ci # millicurie
uCi = micro * Ci # microcurie

eV = e * V # electronvolt
keV = kilo * eV # kilo-electronvolt
MeV = mega * eV # mega-electronvolt
GeV = giga * eV # giga-electronvolt
TeV = tera * eV # tera-electronvolt
eVpc = eV / c # electronvolt per speed of light
MeVpc = mega * eVpc # mega-electronvolt per c
eVpc2 = eV / c**2 # electronvolt per c squared
MeVpc2 = mega * eVpc2 # mega-electronvolt per c squared

G = 6.67430e-11 * m**3 * kg**-1 * s**-2 # gravitational constant
au = 149597870700 * m # astronomical unit
ly = c * year # light year
pc = au / radians(1/3600) # parsec
Mpc = mega * pc # megaparsec
H0 = 72 * km/s / Mpc # Hubble parameter

# table of constants

table = ""
for symbol, object_ in globals().copy().items():

    if isinstance(object_, (int, float, complex)):
        if symbol == "pi":
            table += "\nMath Constants\n"
        elif symbol == "yotta":
            table += "\nMetric Prefixes\n"
        elif symbol == "hundred":
            table += "\nCommon Prefixes\n"
        table += f"{symbol:<12}{object_:.15g}\n"

    if isinstance(object_, Quantity):
        if symbol == "s":
            table += "\nSI Base Units\n"
        elif symbol == "minute":
            table += "\nTime\n"
        elif symbol == "km":
            table += "\nLength\n"
        elif symbol == "Hz":
            table += "\nFrequency\n"
        elif symbol == "g":
            table += "\nClassical Mechanics\n"
        elif symbol == "h":
            table += "\nThermodynamics\n"
        elif symbol == "C":
            table += "\nElectromagnetism\n"
        elif symbol == "in_":
            table += "\nImperial Units\n"
        elif symbol == "kph":
            table += "\nCommon Units\n"
        elif symbol == "me":
            table += "\nAtomic Physics\n"
        elif symbol == "sigma":
            table += "\nQuantum Mechanics\n"
        elif symbol == "Bq":
            table += "\nRadioactive Decays\n"
        elif symbol == "eV":
            table += "\nNuclear Physics\n"
        elif symbol == "G":
            table += "\nCosmology\n"
        table += f"{symbol:<12}{object_.value:<25.15g}{object_.unit}\n"
