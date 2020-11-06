# A easy units converter.

class Unit:

    def __init__(self, dictionary):
        self.dict = {}
        for (key, value) in dictionary.items():
            if value: # value is not 0
                self.dict.update({key:value})

    def __str__(self): # This outputs more basic knowledge
        return str(self.dict)

    def __repr__(self):
        units = [(key, value) for (key, value) in self.dict.items()]
        terms = []
        for unit in units:
            if unit[1] == 1:
                term = unit[0]
            else:
                term = '{0}**{1}'.format(unit[0], unit[1])
            terms.append(term)
        string = ' * '.join(terms)
        return string

    def __eq__(self, other): # prevent 'same unit but are different objects'
        return self.dict == other.dict

    def __ne__(self, other): # prevent 'same unit but are different objects'
        return self.dict != other.dict

    def __mul__(self, other):
        result = self.dict.copy() # prevent override
        for (key, value) in other.dict.items(): # each unit and its power
            result[key] = result.get(key, 0) + value # add the power
            if result[key] == 0: # prevent empty values
                del result[key]
        return Unit(result)

    def __truediv__(self, other):
        result = self.dict.copy() # prevent override
        for (key, value) in other.dict.items(): # each unit and its power
            result[key] = result.get(key, 0) - value # add the power
            if result[key] == 0: # prevent empty values
                del result[key]
        return Unit(result)

    def __pow__(self, power): # do not suggest fraction power
        result = {}
        for (key, value) in self.dict.items():
            result.update({key:value*power})
        return Unit(result)


# variables start with '_' is physical quantities which don't have special unit

const = Unit({}) # could be used sometimes

kg = Unit({'kg':1})
m = Unit({'m':1})
s = Unit({'s':1})
A = Unit({'A':1})
mol = Unit({'mol':1})
K = Unit({'K':1})
Cd = Unit({'Cd':1})

Hz = s ** -1 # Hertz

_v = m / s # velocity
_a = m / s**2 # acceleration
_j = m / s**3 # jerk
_p = kg * _v # momentum

_omega = const / s # angular velocity
_alpha = const / s**2 # angular acceleration
_L = kg * m * _v # angular momentum
_I = kg * m**2 # moment of inertia

_l = m # length
_A = m**2 # area
_V = m**3 # volume
_rho = kg / m**3 # density

N = kg * _a # Newton
_M = N * m # torque

Pa = N / m**2 # Pascal
J = N * m # Joule
W = J / s # Watt

C = A * s # Coulomb
_E = N / C # electric field
V = _E * m # Voltage
F = C / V # Farad
T = N / (C * _v) # Tesla
Wb = T * m**2 # Weber
Ohm = V / A # Ohm
H = Ohm * s # Joseph Henry

# physical constants with units
_g = m / s**2 # gravitational acceleration
_N_A = const / mol # Avogadro constant
_R = J / K / mol # ideal gas constant
_k_B = J / K # Boltzmann constant
_sigma = W / m**2 / K**4 # Stefan-Boltzmann constant
_k = N * m**2 / C**2 # Coulomb constant
_epsilon_0 = C**2 / N / m**2 # Vacuum permittivity
_mu_0 = T * m / A # Permeability

_c = m / s # speed of light
_h = J * s # Planck constant
_e = C # electron charge


if __name__ == '__main__':
    # don't assign values to predefined units
    print(const / s == Hz)
    print(kg * _v**2 == J)
    print(N / C == V / m)
    print(F == s / Ohm)
    print(_mu_0 == H / m)
