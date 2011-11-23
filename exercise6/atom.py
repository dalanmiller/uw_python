"""
Daniel Miller

Usage:
Call form main namespace to run test code

Notes:
As of this commit, the only thing not working is limiting the bonding to the MAX_BONDS variable


#def atomCheck(self, other):
#    Helper method to check that the given atom is an instance of Atom
#    and also that it is also not 'this' Atom.
#    
#    if isinstance(other,Atom) and self.id != other.id: return True
#    else: return False 
  

"""
import sys, inspect


class Atom(object):
    """This is a class outlining the attributes of an atom"""
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
            
            """Found out it was faster to just have a list of objects versus id -> find object based off id."""
            #bonded = []
            #for name, obj in inspect.getmembers(sys.modules[__name__]):
            #    if isinstance(obj, Atom) and obj.id in self.bonds:
            #        bonded.append({'name':name,'atomic':obj.atomic_number,'symbol':obj.chemical_symbol,'id':obj.id})

            return "Atomic Number: %s\nSymbol: %s\nand is bonded to the following atom(s):\n%s" % (self.atomic_number, self.chemical_symbol, [x for x in self.bonds])

    def __add__(self, other_atom):
        if isinstance(other_atom, Atom) and self.id != other_atom.id:
            self.bonds.append(other_atom)
            other_atom.bonds.append(self)
        else:
            print "Type Error! Uh oh! (Or perhaps another unforeseen error)"

    def __cmp__(self, other_atom):
        """Checks atoms based on atomic number"""
        if isinstance(other_atom, Atom):
            return self.atomic_number == other_atom.atomic_number
            

    def get_symbol(self):
        """returns string symbol"""
        return self.chemical_symbol

    def get_bonds(self):
        return self.bonds

    def get_number(self):
        return self.atomic_number

    def get_protons(self):
        return get_number(self)

    def num_bonds(self):
        return self.bonds.__len__()

class Oxygen(Atom):
    """Oxygen sublcass of Atom superclass"""
    MAX_BONDS = 2
    def __init__(self):
        Atom.__init__(self, "O", [], 8)
    
    def __add__(self,other_atom):
        if self.num_bonds() <= self.MAX_BONDS and other_atom.num_bonds() <= other_atom.MAX_BONDS:
            Atom.__add__(self,other_atom)            
        else:
            print "Captain! We can't bond anymore!"         

class Hydrogen(Atom):
    """Hydrogen subclass of Atom superclass"""
    MAX_BONDS = 1
    def __init__(self):
        Atom.__init__(self, "H", [], 1)
        
    def __add__(self,other_atom):
        if self.num_bonds() <= self.MAX_BONDS and other_atom.num_bonds() <= other_atom.MAX_BONDS:
            Atom.__add__(self,other_atom)            
        else:
            print "Captain! We can't bond anymore!"


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

    

