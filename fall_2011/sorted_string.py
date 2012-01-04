"""
Daniel Miller's Solution for Exercise 4

As visible below, if this module is run in __main__ it will deploy tests that demonstrate that the function takes a string, sorts its contents, and then returns them sorted.


Exercise 5A - Write a function sorted_string that takes one string
  argument and returns a string with the same characters but sorted in
  lexical (alphabetic) order.  You may use the list sort method, but
  you may NOT use the built-in library function 'sorted' in your
  solution.  Write your function in a module also named sorted_string
  that defines at least two test strings.  In your module, call your
  function on each of these strings and print the results.

"""

def sorted_string (s):
    """Takes a variable which is converted to a string and then changed to lowercase if possible and finally converted into a list per character.
The list is then sorted using the .sort() method. 
And then the list is joined together and then returned.        
"""
    l = list(str(s.lower())) #Converts the string into a list. p
    l.sort() #Couldn't figure out how to tack on sort() onto another line, only works when the function is called uniquely
    return ''.join([str(x) for x in l]) # Type checks and converts (if possible) each element in the list into a string and then returns string sorted in lexical (alphabetical order)  


if __name__ == '__main__':
    
    test1 = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
    test2 = '135315PneumonoultramicroscopICSilico7135volca4no6cONIo361361sis3551'

    print "Pre-Function test1: %s" % (test1)
    print "sorted_string(test1): %s" % (sorted_string(test1))

    print "\n\n"

    print "Pre-Function test2: %s" % (test2)
    print "sorted_string(test2) %s" % (sorted_string(test2))


    
    

