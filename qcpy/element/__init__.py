class Element:
    _atomic_number = 1
    _symbol = "H"
    _rgb = (255, 250, 205)
    _cov = 0.23
    _vdw = 1.09
    _m = 1.00794

    def __init__(self, atomic_number, name, symbol, r, g, b, cov, vdw, m):
        self._atomic_number = atomic_number
        self._name = name
        self._symbol = symbol
        self._rgb = (r, g, b)
        self._cov = cov
        self._vdw = vdw
        self._m = m
    
    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol
      
    @property
    def atomic_number(self):
        return self._atomic_number

    @property
    def color(self, rgb=True):
        return self._rgb
      
    @property
    def covalent_radius(self, angstroms=True):
        return self._cov
    
    @property
    def van_der_waals_radius(self, angstroms=True):
        return self._vdw
    
    @property
    def mass(self):
        return self._m
    
    def __repr__(self):
        return self.symbol
    
    def __eq__(self, other):
        return self.atomic_number == other.atomic_number


class PeriodicTable:
    """
    Singleton object containing the periodic table of elements.
    Used as a factory class for Element.
    
    >>> table = PeriodicTable()
    >>> h = table['hydrogen']
    >>> h
    H
    >>> h.covalent_radius
    0.23
    >>> h.mass
    1.00794
    >>> h == table['H']
    True
    >>> h == table.hydrogen
    True
    >>> h is table.H
    True
    >>> table['nitrogen'] == h
    False
    >>> table['unobtainium']
    Traceback (most recent call last):
     ...
    KeyError: "No such element 'unobtainium'"
    """
    _element_data = [
        ("hydrogen", "H", 255, 250, 205, 0.23, 1.09, 1.00794),
        ("helium", "He", 185, 211, 238, 1.50, 1.40, 4.002602),
        ("lithium", "Li", 190, 190, 190, 1.28, 1.82, 6.941),
        ("beryllium", "Be", 190, 190, 190, 0.96, 2.00, 9.012182),
        ("boron", "B", 160, 60, 60, 0.83, 2.00, 10.811),
        ("carbon", "C", 84, 84, 84, 0.68, 1.70, 12.0107),
        ("nitrogen", "N", 30, 144, 255, 0.68, 1.55, 14.0067),
        ("oxygen", "O", 255, 0, 0, 0.68, 1.52, 15.9994),
        ("fluorine", "F", 255, 255, 0, 0.64, 1.47, 18.998403),
        ("neon", "Ne", 185, 211, 238, 1.50, 1.54, 20.1797),
        ("sodium", "Na", 190, 190, 190, 1.66, 2.27, 22.98977),
        ("magnesium", "Mg", 190, 190, 190, 1.41, 1.73, 24.305),
        ("aluminium", "Al", 190, 190, 190, 1.21, 2.00, 26.981538),
        ("silicon", "Si", 211, 211, 211, 1.20, 2.10, 28.0855),
        ("phosphorus", "P", 255, 140, 0, 1.05, 1.80, 30.973761),
        ("sulfur", "S", 255, 246, 143, 1.02, 1.80, 32.065),
        ("chlorine", "Cl", 0, 255, 0, 0.99, 1.75, 35.453),
        ("argon", "Ar", 185, 211, 238, 1.51, 1.88, 39.948),
        ("potassium", "K", 190, 190, 190, 2.03, 2.75, 39.0983),
        ("calcium", "Ca", 190, 190, 190, 1.76, 2.00, 40.078),
        ("scandium", "Sc", 190, 190, 190, 1.70, 2.00, 44.95591),
        ("titanium", "Ti", 190, 190, 190, 1.60, 2.00, 47.867),
        ("vanadium", "V", 190, 190, 190, 1.53, 2.00, 50.9415),
        ("chromium", "Cr", 190, 190, 190, 1.39, 2.00, 51.9961),
        ("manganese", "Mn", 190, 190, 190, 1.61, 2.00, 54.938049),
        ("iron", "Fe", 190, 190, 190, 1.52, 2.00, 55.845),
        ("cobalt", "Co", 190, 190, 190, 1.26, 2.00, 58.9332),
        ("nickel", "Ni", 190, 190, 190, 1.24, 1.63, 58.6934),
        ("copper", "Cu", 255, 130, 71, 1.32, 1.40, 63.546),
        ("zinc", "Zn", 190, 190, 190, 1.22, 1.39, 65.409),
        ("gallium", "Ga", 190, 190, 190, 1.22, 1.87, 69.723),
        ("germanium", "Ge", 190, 190, 190, 1.17, 2.00, 72.64),
        ("arsenic", "As", 190, 190, 190, 1.21, 1.85, 74.9216),
        ("selenium", "Se", 190, 190, 190, 1.22, 1.90, 78.96, ),
        ("bromine", "Br", 190, 130, 60, 1.21, 1.85, 79.904),
        ("krypton", "Kr", 185, 211, 238, 1.50, 2.02, 83.798),
        ("rubidium", "Rb", 190, 190, 190, 2.20, 2.00, 85.4678),
        ("strontium", "Sr", 190, 190, 190, 1.95, 2.00, 87.62),
        ("yttrium", "Y", 190, 190, 190, 1.90, 2.00, 88.90585),
        ("zirconium", "Zr", 190, 190, 190, 1.75, 2.00, 91.224),
        ("niobium", "Nb", 190, 190, 190, 1.64, 2.00, 92.90638),
        ("molybdenum", "Mo", 190, 190, 190, 1.54, 2.00, 95.94),
        ("technetium", "Tc", 190, 190, 190, 1.47, 2.00, 98.0),
        ("ruthenium", "Ru", 190, 190, 190, 1.46, 2.00, 101.07),
        ("rhodium", "Rh", 190, 190, 190, 1.45, 2.00, 102.9055),
        ("palladium", "Pd", 190, 190, 190, 1.39, 1.63, 106.42),
        ("silver", "Ag", 255, 255, 255, 1.45, 1.72, 107.8682),
        ("cadmium", "Cd", 190, 190, 190, 1.44, 1.58, 112.411),
        ("indium", "In", 190, 190, 190, 1.42, 1.93, 114.818),
        ("tin", "Sn", 190, 190, 190, 1.39, 2.17, 118.71),
        ("antimony", "Sb", 190, 190, 190, 1.39, 2.00, 121.76),
        ("tellurium", "Te", 190, 190, 190, 1.47, 2.06, 127.6),
        ("iodine", "I", 160, 32, 240, 1.40, 1.98, 126.90447),
        ("xenon", "Xe", 185, 211, 238, 1.50, 2.16, 131.293),
        ("caesium", "Cs", 190, 190, 190, 2.44, 2.00, 132.90545),
        ("barium", "Ba", 190, 190, 190, 2.15, 2.00, 137.327),
        ("lanthanum", "La", 190, 190, 190, 2.07, 2.00, 138.9055),
        ("cerium", "Ce", 190, 190, 190, 2.04, 2.00, 140.116),
        ("praseodymium", "Pr", 190, 190, 190, 2.03, 2.00, 140.90765),
        ("neodymium", "Nd", 190, 190, 190, 2.01, 2.00, 144.24),
        ("promethium", "Pm", 190, 190, 190, 1.99, 2.00, 145.0),
        ("samarium", "Sm", 190, 190, 190, 1.98, 2.00, 150.36),
        ("europium", "Eu", 190, 190, 190, 1.98, 2.00, 151.964),
        ("gadolinium", "Gd", 190, 190, 190, 1.96, 2.00, 157.25),
        ("terbium", "Tb", 190, 190, 190, 1.94, 2.00, 158.92534),
        ("dysprosium", "Dy", 190, 190, 190, 1.92, 2.00, 162.5),
        ("holmium", "Ho", 190, 190, 190, 1.92, 2.00, 164.93032),
        ("erbium", "Er", 190, 190, 190, 1.89, 2.00, 167.259),
        ("thulium", "Tm", 190, 190, 190, 1.90, 2.00, 168.93421),
        ("Ytterbium", "Yb", 190, 190, 190, 1.87, 2.00, 173.04),
        ("lutetium", "Lu", 190, 190, 190, 1.87, 2.00, 174.967),
        ("hafnium", "Hf", 190, 190, 190, 1.75, 2.00, 178.49),
        ("tantalum", "Ta", 190, 190, 190, 1.70, 2.00, 180.9479),
        ("tungsten", "W", 190, 190, 190, 1.62, 2.00, 183.84),
        ("rhenium", "Re", 190, 190, 190, 1.51, 2.00, 186.207),
        ("osmium", "Os", 190, 190, 190, 1.44, 2.00, 190.23),
        ("iridium", "Ir", 190, 190, 190, 1.41, 2.00, 192.217),
        ("platinum", "Pt", 190, 190, 190, 1.36, 1.72, 195.078),
        ("gold", "Au", 255, 215, 0, 1.50, 1.66, 196.96655),
        ("mercury", "Hg", 190, 190, 190, 1.32, 1.55, 200.59),
        ("thallium", "Tl", 190, 190, 190, 1.45, 1.96, 204.3833),
        ("lead", "Pb", 190, 190, 190, 1.46, 2.02, 207.2),
        ("bismuth", "Bi", 190, 190, 190, 1.48, 2.00, 208.98038),
        ("polonium", "Po", 190, 190, 190, 1.40, 2.00, 290.0),
        ("astatine", "At", 190, 190, 190, 1.21, 2.00, 210.0),
        ("radon", "Rn", 185, 211, 238, 1.50, 2.00, 222.0),
        ("francium", "Fr", 190, 190, 190, 2.60, 2.00, 223.0),
        ("radium", "Ra", 190, 190, 190, 2.21, 2.00, 226.0),
        ("actinium", "Ac", 190, 190, 190, 2.15, 2.00, 227.0),
        ("thorium", "Th", 190, 190, 190, 2.06, 2.00, 232.0381),
        ("protactinium", "Pa", 190, 190, 190, 2.00, 2.00, 231.03588),
        ("uranium", "U", 190, 190, 190, 1.96, 1.86, 238.02891),
        ("neptunium", "Np", 190, 190, 190, 1.90, 2.00, 237.0),
        ("plutonium", "Pu", 190, 190, 190, 1.87, 2.00, 244.0),
        ("americium", "Am", 190, 190, 190, 1.80, 2.00, 243.0),
        ("curium", "Cm", 190, 190, 190, 1.69, 2.00, 247.0),
        ("berkelium", "Bk", 190, 190, 190, 1.54, 2.00, 247.0),
        ("californium", "Cf", 190, 190, 190, 1.83, 2.00, 251.0),
        ("einsteinium", "Es", 190, 190, 190, 1.50, 2.00, 252.0),
        ("fermium", "Fm", 190, 190, 190, 1.50, 2.00, 257.0),
        ("mendelevium", "Md", 190, 190, 190, 1.50, 2.00, 258.0),
        ("nobelium", "No", 190, 190, 190, 1.50, 2.00, 259.0),
        ("lawrencium", "Lr", 190, 190, 190, 1.50, 2.00, 262.0),
    ]
    elements = [Element(n, *args) for n, args in enumerate(_element_data, 1)]    
    
    def __init__(self):
        for e in self.elements:
            setattr(self, e.name, e)
            setattr(self, e.symbol, e)
    
    def __iter__(self):
        return iter(self.elements)
    
    def __getitem__(self, key):
        if isinstance(key, int):
          return self.elements[key - 1]
        else:
            matches = [e for e in self.elements if (e.name == key or e.symbol == key)]
            if len(matches) < 1:
                raise KeyError("No such element '{}'".format(key))
            return matches[0]

periodictable = PeriodicTable()

# Set so one can import O, H etc from this module
for element in periodictable:
    globals()[element.name] = element
    globals()[element.symbol] = element
