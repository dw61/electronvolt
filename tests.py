from electronvolt import *
from uncertainties import ufloat

print(table)

assert c == 299792458 * m / s
assert euler ** (1 * s / s) == exp(kg / kg)
assert cos(-pi) == -1
assert 12 != 12 * kg
assert 2 == 1 * kg / kg + 1
assert quantity(6, Unit({"kg":5, "mol":-2})) == 6 * kg**5 / mol**2
assert not isinstance(ufloat(3, 1) * km / ly, Quantity)
assert isinstance(alpha, float)

assert 1 * m != 1 * s
assert 2 * kg + kg * 2 <= 5 * kg
assert N / C == V / m
assert eV in J
assert pc > ly
