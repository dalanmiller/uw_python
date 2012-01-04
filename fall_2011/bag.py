"""
Daniel Miller

Exercise: Write a module bag.py that defines a class named bag.  A bag (also
called a multiset) is a collection without order (like a set) but with
repetition (unlike a set) --- an element can appear one or more times
in a bag.  Implement bag as a subclass of dictionary where each bag
element is a key and its value is an integer that represents its
multiplicity (the number of repetitions).  For example in b1 =
bag({'a':2, 'b':3}), b1 is a bag where 'a' occurs twice (has
multiplicity 2) and 'b' occurs three times.  Provide a bag union
operator + (plus sign) that operates on two bags and returns a third
bag, their union.  The bag union contains all of the elements of both
bags, with their multiplicities added.  For example, after b2 =
bag({'b':1, 'c':2}), then b1 + b2 == bag({'a':2, 'b':4', 'c':2})
"""

class Bag(dict):
    #If a dictionary is given, need to initialize with that dictionary versus creating a blank one.
    def __init__(self, *args):     
        if args: dict.__init__(self,*args)
        else: dict.__init__(self)       
            
    def __add__(self, other):
        assert isinstance(other, Bag)
        new_bag = Bag(other)

        for x in self.keys():
            new_bag[x] = new_bag.get(x, 0) + self.get(x,0)

        return new_bag 
    
    def combine(self, other):
        return __add__(self,other)
    
    
