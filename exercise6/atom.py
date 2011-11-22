"""
 Assignment for week 7, Tues Nov 22, bring exercise to turn in (hardcopy)

 Python Tutorial: Section 9, Classes, except 9.9 - 9.11
 http://docs.python.org/tutorial/classes.html

Write a module atom.py that defines a class named Atom whose base
class is object.  An atom has a chemical symbol (a string).  An atom
can have chemical bonds to other atoms.  When an atom is created, it
has no bonds to other atoms.  Each atom can have no more than a
certain maximum number of bonds to other atoms.  When one atom has a
bond to another atom, the second atom must have a bond back to the
first.  An atom may have more than one bond to the same atom.  Every
atom has a method that returns a description string that contains its
chemical symbol, a unique identity, and the chemical symbols and
unique identities of all the atoms to which it has bonds.  The
identity in this string must be different in every atom, and must
always be the same in a given atom.

The atom module defines two more classes that represent hydrogen and
oxygen atoms, each with the base class Atom.  Every hydrogen atom has
the chemical symbol 'H' and has at most one bond.  Every oxygen atom
has the chemical symbol 'O' and has at most two bonds.

Also in atom.py, write code that tests the atom classes.  This test
code should execute only when the module is executed at top level, not
when it is imported.  This test code creates three hydrogen atoms and
two oxygen atoms.  Then this code creates bonds between one of the
oxygens and two of the hydrogens (forming a water molecule).  Then it
prints the description string of every atom.

Hints and reminders:
 This shouldn't take more than a page or two of code
 Use class attributes for data common to all instances of a class
 Instance attributes can be lists, you can have lists of objects
 Turn in what you have on Nov 22, even if it is not finished
"""

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

    #def atomCheck(self, other):
    #    """Helper method to check that the given atom is an instance of Atom
    #    and also that it is also not 'this' Atom.
    #    """
    #    if isinstance(other,Atom) and self.id != other.id: return True
    #    else: return False 
  
    def __str__(self):
        return "%s - %s is bonded to %s" % (self.atomic_number, self.chemical_symbol,[x.get_symbol for x in self.bonds])

    def __add__(self, other_atom):
        if isinstance(other_atom, Atom) and self.id != other_atom.id:
            self.bonds.append(id(other_atom))
            other_atom.bonds.append(id(self))
        else:
            print "Type Error! Uh oh"

    def __cmp__(self, other_atom):
        """Checks atoms based on atomic number"""
        if isinstance(other_atom, Atom):
            return self.atomic_number == other_atom.atomic_number
            

    def get_symbol(self):
        return self.chemical_symbol

    def get_bonds(self):
        return self.bonds

    def get_number(self):
        return self.atomic_number

    def get_protons(self):
        return get_number(self)

    def num_bonds(self):
        return self.bonds__len__()

   

class Oxygen(Atom):
    MAX_BONDS = 2
    def __init__(self):
        Atom.__init__(self, "O", [], 8)
    
    def __add__(self,other_atom):
        if self.get_bonds >= MAX_BONDS:
            print "Captain! We can't bond anymore!"
        else:
            Atom.__add__(self,other_atom)
                 


class Hydrogen(Atom):
    MAX_BONDS = 1
    def __init__(self):
        Atom.__init__(self, "H", [], 1)
        
    def __add__(self,other_atom):
        if self.get_bonds >= MAX_BONDS:
            print "Captain! We can't bond anymore!"
        else:
            Atom.__add__(self,other_atom)
