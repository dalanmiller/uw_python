"""
Daniel Miller

Usage:
Call form main namespace to run test code

Notes:
As of this commit, everything works! Why I was previously using <= I have no idea...


#def atomCheck(self, other):
#    Helper method to check that the given atom is an instance of Atom
#    and also that it is also not 'this' Atom.
#    
#    if isinstance(other,Atom) and self.id != other.id: return True
#    else: return False 
  

"""
import sys, inspect


class Atom(object):
    MAX_BONDS = 0
    """This is a class outlining & intializing the attributes of an atom"""
    def __init__(self, symbol, bonds, number):
        
        if symbol: 
            self.chemical_symbol = symbol
        else:
            self.chemical_symbol = ""

        if bonds:
            self.bonds = bonds
        else:
            self.bonds = []

        if number:
            self.atomic_number = number
        else:
            self.atomic_number = 0

        self.id = id(self)

 
    def __str__(self):
        """Prints out the attributes of the Atom and the attributes of the other Atoms that it is bonded to"""
        if self.bonds.__len__() == 0:
            return "Atomic Number: %s\nSymbol: %s" % (self.atomic_number, self.chemical_symbol)
        else:
            s = ""
            for x in self.bonds:
                s += "Atomic Number: %s - Name: %s -  Id: %s\n" % (x.atomic_number,x.__class__.__name__, id(x))
            return u"Atomic Number: %s\nSymbol: %s\nand is bonded to the following atom(s):\n%s" % (self.atomic_number, self.chemical_symbol, s)

    def __add__(self, other_atom):
        """Overwriting builtin for adding Atoms together, adds the other object of Atom to each bond list"""
        if (isinstance(other_atom, Atom) and self.id != other_atom.id and self.num_bonds() < self.MAX_BONDS and other_atom.num_bonds() < other_atom.MAX_BONDS): #Checks that the given object is an instance of Atom, that the given object isn't the same Atom is "self" Atom, and that both Atoms have an available space for a bond.
            self.bonds.append(other_atom)
            other_atom.bonds.append(self)
            return other_atom

    def __cmp__(self, other_atom):
        """Checks atoms based on atomic number"""
        if isinstance(other_atom, Atom):
            return self.atomic_number == other_atom.atomic_number
           
    def get_symbol(self):
        """returns string symbol"""
        return self.chemical_symbol

    def get_bonds(self):
        """Returns bond list"""
        return self.bonds

    def get_number(self):
        """Returns atomic number"""
        return self.atomic_number

    def get_protons(self):
        """Returns number of protons / atomic number"""
        return get_number(self)

    def num_bonds(self):
        """Returns number of bonds currently in place"""
        return self.bonds.__len__()

class Oxygen(Atom):
    """Oxygen sublcass of Atom superclass"""
    MAX_BONDS = 2
    def __init__(self):
        Atom.__init__(self, "O", [], 8)      

class Hydrogen(Atom):
    """Hydrogen subclass of Atom superclass"""
    MAX_BONDS = 1
    def __init__(self):
        Atom.__init__(self, "H", [], 1)

if __name__ == "__main__":
    """Test code begins here"""
    h1 = Hydrogen() 
    o1 = Oxygen()
    o2 = Oxygen()

    h1 + o1 
    h1 + o2

    print h1
    print o1
    print o2

    

