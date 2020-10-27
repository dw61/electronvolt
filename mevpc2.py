from math import *
 

# Unit converter.
class Unit:

    def __init__(self, d):
        self.d = {unit:power for unit, power in d.items() if power} # remove zero power

    def __repr__(self): # for commandline convenience. __str__ redirects here by default
        terms = []
        for unit, power in self.d.items():
            if power == 1:
                terms.append(unit)
            else:
                terms.append('{0}**{1}'.format(unit, power))
        return ' * '.join(terms)

    def __eq__(self, other): # prevent 'same unit but are different objects'
        return self.d == other.d #__ne__ is negation of __eq__ in python 3

    def __mul__(self, other):
        units = set(self.d) | set(other.d)
        d = {unit : self.d.get(unit, 0) + other.d.get(unit, 0) for unit in units}
        return Unit(d)

    def __truediv__(self, other):
        units = set(self.d) | set(other.d)
        d = {unit : self.d.get(unit, 0) - other.d.get(unit, 0) for unit in units}
        return Unit(d)

    def __pow__(self, p):
        result = {unit : power * p for unit, power in self.d.items()}
        return Unit(result)

    def __bool__(self):
        return bool(self.d)


# Physical quantity calculator.
class Quantity:

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return '{0} {1}'.format(self.value, repr(self.unit))

    def __eq__(self, other):
        return self.value == other.value and self.unit == other.unit

    def __add__(self, other):
        if isinstance(other, (int, float)): # handles 1*kg/kg + 1
            return self + Quantity(other, Unit({})) # implicit-ish recursion
        assert self.unit == other.unit # check for same unit. not considering 0*kg + 1*m = 1*m
        return Quantity(self.value + other.value, self.unit)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)): # handles 1*kg/kg - 1
            return self - Quantity(other, Unit({}))
        assert self.unit == other.unit # check for same unit
        return Quantity(self.value - other.value, self.unit)

    def __neg__(self):
        return Quantity(-self.value, self.unit)

    def __rsub__(self, other):
        return - (self - other) # self.__rsub__(other) becomes -self.__sub__(other)

    def __mul__(self, other): # both kg*10 and kg*m works
        if isinstance(other, (int, float)):
            return self * Quantity(other, Unit({}))
        return Quantity(self.value * other.value, self.unit * other.unit)

    def __rmul__(self, other): # handles 10*kg
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self / Quantity(other, Unit({}))
        return Quantity(self.value / other.value, self.unit / other.unit)

    def __rtruediv__(self, other):
        return (self / other) ** -1

    def __pow__(self, p):
        return Quantity(self.value ** p, self.unit ** p)

    def __contains__(self, other):
        return self.unit == other.unit # sloppy. not doing .convert()

    def __bool__(self):
        return bool(self.value)

    def __float__(self): # handles sin(1*m/m)
        assert not self.unit
        return float(self.value)


# trigonometry. currently has some domain and range issues unresolved
# https://en.wikipedia.org/wiki/Trigonometric_functions
# https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
# https://en.wikipedia.org/wiki/Hyperbolic_functions
# https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions

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


# SI metric prefixes
# https://en.wikipedia.org/wiki/Metric_prefix

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


# SI units

kg = Quantity(1, Unit({'kg' : 1}))
m = Quantity(1, Unit({'m' : 1}))
s = Quantity(1, Unit({'s' : 1}))
A = Quantity(1, Unit({'A' : 1}))
mol = Quantity(1, Unit({'mol' : 1}))
K = Quantity(1, Unit({'K' : 1}))
Cd = Quantity(1, Unit({'Cd' : 1}))


# derived units

Hz = s**-1 # Hertz

N = kg * m / s**2 # Newton
Pa = N / m**2 # Pascal
J = N * m # Joule
W = J / s # Watt

C = A * s # Coulomb
V = J / C # Voltage
F = C / V # Farad
T = V * s / m**2 # Tesla
Wb = T * m**2 # Weber
Ohm = V / A # Ohm
H = Ohm * s # Joseph Henry


# physical quantities. deprecated

_m = kg # mass
_v = m / s # velocity
_a = m / s**2 # acceleration
_j = m / s**3 # jerk
_p = kg * _v # momentum

_omega = 1 / s # angular velocity
_alpha = 1 / s**2 # angular acceleration
_L = kg * m * _v # angular momentum
_I = kg * m**2 # moment of inertia
_M = N * m # torque

_l = m # length
_A = m**2 # area
_V = m**3 # volume
_rho = kg / m**3 # density

_E = N / C # electric field


# physicsal constants
# https://en.wikipedia.org/wiki/List_of_physical_constants

c = 299792458 * m / s # speed of light
h = 6.62607015e-34 * J * s # Planck constant
hbar = h / (2 * pi) # reduced Planck constant
G = 6.67430e-11 * m**3 * kg**-1 * s**-2 # Newtonian constant of gravitation
mu0 = 1.25663706212e-6 * H / m # vacuum magnetic permeability
epsilon0 = 1 / (mu0 * c**2) # vacuum electric permittivity
e = 1.602176634e-19 * C # elementary charge
NA = 6.02214076e23 * mol**-1 # Avogadro constant
kB = 1.380649e-23 * J / K # Boltzmann constant
me = 9.1093837015e-31 * kg # electron mass
mp = 1.67262192369e-27 * kg # proton mass
mn = 1.67492749804e-27 * kg # neutron mass
Da = 1.66053906660e-27 * kg # dalton, atomic mass constant
R = NA * kB # ideal gas constant
sigma = 5.670374419e-8 * W / m**2 / K**4 # Stefan-Boltzmann constant


# more constants

ms = milli * s # millisecond
micros = micro * s # microsecond
ns = nano * s # nanosecond
minute = 60 * s # minute
hour = 60 * minute # hour
day = 24 * hour # day
year = 365.25 * day # year, average
ly = c * year # light year

cm = centi * m # centimeter
mm = milli * m # millimeter
microm = micro * m # micrometer
nm = nano * m # nanometer
fm = femto * m # femtometer, fermi
km = kilo * m # kilometer

kph = km / hour # kilometer per hour
mile = 1609.344 * m # miles
mph = mile / hour # miles per hour

gacceleration = 9.80665 * m / s**2 # gravitational acceleration
gram = kg / kilo # gram
k = 1 / (4 * pi * epsilon0) # Coulomb constant
eV = e * V # electronvolt
keV = kilo * eV # kilo electronvolt
MeV = mega * eV # mega electronvolt
GeV = giga * eV # giga electronvolt
TeV = tera * eV # tetra electronvolt
MeVpc2 = MeV / c**2 # mega electronvolt per c squared

a0 = 4 * pi * epsilon0 * hbar**2 / (me * e**2) # Bohr radius
hground = - me * e**4 / (32 * pi**2 * epsilon0**2 * hbar**2) # ground state hydrogen energy level
Rinfinity = me * e**4 / (64 * pi**3 * epsilon0**2 * hbar**3 * c) # Rydberg constant
alpha = 1 / (4 * pi * epsilon0) * e**2 / (hbar * c) # fine structure constant


# testings

assert 1 * m != 1 * kg
assert 2 * kg != 3 * kg
assert N / C in V / m
assert kg * c**2 in J
assert MeVpc2 == 1.7826619216278976e-30 * kg
