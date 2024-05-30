from formula import parse_formula
# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def make_periodic_table():
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.941, 3],
        "Be": ["Beryllium", 9.012182, 4],
        "B": ["Boron", 10.811, 5],
        "C": ["Carbon", 12.0107, 6],
        "N": ["Nitrogen", 14.0067, 7],
        "O": ["Oxygen", 15.9994, 8],
        "F": ["Fluorine", 18.9984032, 9],
        "Ne": ["Neon", 20.1797, 10],
        "Na": ["Sodium", 22.98976928, 11],
        "Mg": ["Magnesium", 24.3050, 12],
        "Al": ["Aluminum", 26.9815386, 13],
        "Si": ["Silicon", 28.0855, 14],
        "P": ["Phosphorus", 30.973762, 15],
        "S": ["Sulfur", 32.065, 16],
        "Cl": ["Chlorine", 35.453, 17],
        "K": ["Potassium", 39.0983, 19],
        "Ar": ["Argon", 39.948, 18],
        "Ca": ["Calcium", 40.078, 20],
        "Sc": ["Scandium", 44.955912, 21],
        "Ti": ["Titanium", 47.867, 22],
        "V": ["Vanadium", 50.9415, 23],
        "Cr": ["Chromium", 51.9961, 24],
        "Mn": ["Manganese", 54.938045, 25],
        "Fe": ["Iron", 55.845, 26],
        "Ni": ["Nickel", 58.6934, 28],
        "Co": ["Cobalt", 58.933195, 27],
        "Cu": ["Copper", 63.546, 29],
        "Zn": ["Zinc", 65.38, 30],
        "Ga": ["Gallium", 69.723, 31],
        "Ge": ["Germanium", 72.63, 32],
        "As": ["Arsenic", 74.92160, 33],
        "Se": ["Selenium", 78.96, 34],
        "Br": ["Bromine", 79.904, 35],
        "Kr": ["Krypton", 83.798, 36],
        "Rb": ["Rubidium", 85.4678, 37],
        "Sr": ["Strontium", 87.62, 38],
        "Y": ["Yttrium", 88.90585, 39],
        "Zr": ["Zirconium", 91.224, 40],
        "Nb": ["Niobium", 92.90638, 41],
        "Mo": ["Molybdenum", 95.96, 42],
        "Tc": ["Technetium", 98, 43],
        "Ru": ["Ruthenium", 101.07, 44],
        "Rh": ["Rhodium", 102.90550, 45],
        "Pd": ["Palladium", 106.42, 46],
        "Ag": ["Silver", 107.8682, 47],
        "Cd": ["Cadmium", 112.411, 48],
        "In": ["Indium", 114.818, 49],
        "Sn": ["Tin", 118.710, 50],
        "Sb": ["Antimony", 121.760, 51],
        "I": ["Iodine", 126.90447, 53],
        "Te": ["Tellurium", 127.60, 52],
        "Xe": ["Xenon", 131.293, 54],
        "Cs": ["Cesium", 132.9054519, 55],
        "Ba": ["Barium", 137.327, 56],
        "La": ["Lanthanum", 138.90547, 57],
        "Ce": ["Cerium", 140.116, 58],
        "Pr": ["Praseodymium", 140.90765, 59],
        "Nd": ["Neodymium", 144.242, 60],
        "Pm": ["Promethium", 145, 61],
        "Sm": ["Samarium", 150.36, 62],
        "Eu": ["Europium", 151.964, 63],
        "Gd": ["Gadolinium", 157.25, 64],
        "Tb": ["Terbium", 158.92535, 65],
        "Dy": ["Dysprosium", 162.500, 66],
        "Ho": ["Holmium", 164.93032, 67],
        "Er": ["Erbium", 167.259, 68],
        "Tm": ["Thulium", 168.93421, 69],
        "Yb": ["Ytterbium", 173.04, 70],
        "Lu": ["Lutetium", 174.967, 71],
        "Hf": ["Hafnium", 178.49, 72],
        "Ta": ["Tantalum", 180.94788, 73],
        "W": ["Tungsten", 183.84, 74],
        "Re": ["Rhenium", 186.207, 75],
        "Os": ["Osmium", 190.23, 76],
        "Ir": ["Iridium", 192.217, 77],
        "Pt": ["Platinum", 195.084, 78],
        "Au": ["Gold", 196.966569, 79],
        "Hg": ["Mercury", 200.59, 80],
        "Tl": ["Thallium", 204.3833, 81],
        "Pb": ["Lead", 207.2, 82],
        "Bi": ["Bismuth", 208.98040, 83],
        "Th": ["Thorium", 232.03806, 90],
        "Pa": ["Protactinium", 231.03588, 91],
        "U": ["Uranium", 238.02891, 92],
        "Np": ["Neptunium", 237, 93],
        "Pu": ["Plutonium", 244, 94],
        "Am": ["Americium", 243, 95],
        "Cm": ["Curium", 247, 96],
        "Bk": ["Berkelium", 247, 97],
        "Cf": ["Californium", 251, 98],
        "Es": ["Einsteinium", 252, 99],
        "Fm": ["Fermium", 257, 100],
        "Md": ["Mendelevium", 258, 101],
        "No": ["Nobelium", 259, 102],
        "Lr": ["Lawrencium", 262, 103],
        "Rf": ["Rutherfordium", 267, 104],
        "Db": ["Dubnium", 270, 105],
        "Sg": ["Seaborgium", 271, 106],
        "Bh": ["Bohrium", 270, 107],
        "Hs": ["Hassium", 277, 108],
        "Mt": ["Meitnerium", 276, 109],
        "Ds": ["Darmstadtium", 281, 110],
        "Rg": ["Roentgenium", 282, 111],
        "Cn": ["Copernicium", 285, 112],
        "Nh": ["Nihonium", 286, 113],
        "Fl": ["Flerovium", 289, 114],
        "Mc": ["Moscovium", 290, 115],
        "Lv": ["Livermorium", 293, 116],
        "Ts": ["Tennessine", 294, 117],
        "Og": ["Oganesson", 294, 118]
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_protons = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity
    return total_protons

def main():
    # Get a chemical formula for a molecule from the user.
    formula = input("Enter the molecular formula of the sample: ")

    # Get the mass of a chemical sample in grams from the user.
    mass_in_grams = float(input("Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the chemical formula given by the user
    # to a compound list that stores element symbols and the quantity of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Call the compute_molar_mass function to compute the molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample.
    number_of_moles = mass_in_grams / molar_mass

    # Print the molar mass.
    print(f"{molar_mass:.5f} grams/mole")

    # Print the number of moles.
    print(f"{number_of_moles:.5f} moles")

    # Known molecules dictionary
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    # Get the formula name and print it
    compound_name = get_formula_name(formula, known_molecules_dict)
    print(f"Compound name: {compound_name}")

    # Calculate and print the number of protons
    total_protons = sum_protons(symbol_quantity_list, periodic_table)
    print(f"Total number of protons: {total_protons}")

if __name__ == "__main__":
    main()