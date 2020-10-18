# A physical quantity calculator with units.

### Demonstration 1

Calculate relativistic rest mass energy of an electron.

```python
In[1]: me * c**2

Out[1]: 8.187105776823886e-14 m**2 * s**-2 * kg
```

Check that the energy is in Joules.

```python
In[2]: me * c**2 in J # sloppy use of __contains__

Out[2]: True
```

Convert joules to mega electronvolts if you like.

```python
In[3]: me * c**2 / MeV

Out[3]: 0.5109989499961642
```

### Demonstration 2

Calculating the relativistic total energy of electron moving at 0.8c.

#### Method 1. Use ![equation](http://latex.codecogs.com/gif.latex?E=\gamma%20mc^2)

Calculate gamma factor at 0.8c.

```python
In[4]: gamma = 1 / (1 - 0.8**2) ** 0.5
       gamma

Out[4]: 1.666666666666667
```

Plug in to the relativistic total energy formula.

```python
In[5]: gamma * me * c**2

Out[5]: 1.3645176294706481e-13 m**2 * s**-2 * kg
```

Convert to mega electronvolts if you like.

```python
In[6]: gamma * me * c**2 / MeV

Out[6]: 0.851664916660274
```

#### Method 2. Use ![equation](http://latex.codecogs.com/gif.latex?E^2=p^2c^2+m^2c^4)

Calculate the relativistic momentum of the electron.

```python
In[7]: p = gamma * me * 0.8*c
       p

Out[7]: 3.6412327076504325e-22 m * s**-1 * kg
```

Use the formula of relativistic total energy.

```python
In[8]: (p**2 * c**2 + me**2 * c**4) ** 0.5

Out[8]: 1.364517629470648e-13 m**2.0 * s**-2.0 * kg
```

Convert to mega electronvolts if you like.

```python
In[9]: gamma * me * c**2 / MeV

Out[9]: 0.851664916660274
```

This yields same value as of method 1.
