class Unit:

    def __init__(self, d):
        self.d = {unit : power for unit, power in d.items() if power} # remove zero power

    def __repr__(self): # for commandline convenience. __str__ redirects here
        terms = []
        for unit, power in self.d.items():
            if power == 1:
                terms.append(unit)
            else:
                terms.append(f'{unit}**{power}')
        return ' * '.join(terms)

    def __eq__(self, other):
        return self.d == other.d

    def __mul__(self, other):
        units = set(self.d) | set(other.d)
        d = {unit : self.d.get(unit, 0) + other.d.get(unit, 0) for unit in units}
        return Unit(d)

    def __truediv__(self, other):
        units = set(self.d) | set(other.d)
        d = {unit : self.d.get(unit, 0) - other.d.get(unit, 0) for unit in units}
        return Unit(d)

    def __pow__(self, p):
        d = {unit : power * p for unit, power in self.d.items()}
        return Unit(d)

    def __bool__(self):
        return bool(self.d)
