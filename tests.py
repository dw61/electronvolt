from electronvolt import *
from uncertainties import ufloat

print(table)

assert Unit({"y":3})**-1 == Unit({"y":-3})
assert Quantity(5, Unit({"x":1})) != 5
assert quantity(6, Unit({"kg":5, "mol":-2})) == 6 * kg**5 / mol**2
assert quantity(3) == 3
assert unit("kg") * 8 == 8 * kg

assert cos(-pi) == -1
assert -1e-9 < sind(30) - 1/2 < 1e-9

assert c == 299792458 * m / s
assert euler ** (1 * s / s) == exp(kg / kg)
assert 2 == 1 * kg / kg + 1
assert 34 * nm < 1.77 * cm <= 0.1 * ly
assert 0.003 * year > 1 * day >= 80000.3 * s >= 1e-4 * us
assert -kilo*eV < 0.511*MeV - me*c**2 < kilo * eV <= J

assert not isinstance(ufloat(3, 1) * km / ly, Quantity)
assert isinstance(alpha, float)

assert 12 != 12 * kg
assert 1 * m != 1 * s
assert 2 * kg + kg * 2 <= 5 * kg
assert N / C == V / m
assert eV in J
assert pc > ly
