"""
 Daniel Miller's Solution to Exercise 4

 As seen below, if running the module from __main__, the tests will deploy demonstrating that the sorted_list function does indeed make a copy and returns an entirely new string.

I tried to decrease the amount of lines use and simply use 'return list(l).sort()' however this does not work for a reason that I was unable to discover. 

===

 Exercise 5B - Write a function sorted_list that takes one list
  argument and returns a list with the same elements but sorted.  This
  function must NOT change the list in the caller.  You may use the
  list sort method, but you may NOT use the built-in library function
  'sorted' in your solution.  Write your function in a module also
  named sorted_list that defines at least two test strings.  In your
  module, call your function on each of these lists and print the
  results.  Also, print both lists after calling the function to show
  that they have not changed.

"""


def sorted_list(l):
    """Takes a list and creates a copy of it. Then sorts the list and then returns a copy of the helper list"""
    new_l = list(l)
    new_l.sort()
    return list(new_l)



if __name__ == "__main__":
    test1 = [ "mary", "had", "a", "little", "lamb"]
    test2 = [10,9,3,53,6336,136134,135134,1231]  
    test3 = ["fibonacci", 10, "pythagorean", 1030101303103050139503190590135, "isoceles", [10,5,1], {'name':'daniel'}] 

    print ("Pre-Function Test 1: %s" % (test1))
    print ( "sorted_list(test1) = %s" % (sorted_list(test1)) )
    print ("Post-Function Test 1: %s" % (test1)) 

    print "\n\n"

    print "Pre-Function Test 2: %s" % (test2) 
    print "sorted_list(test2): %s" % (sorted_list(test2))
    print "Post-Function Test 2: %s" % (test2)
    
    print "\n\n"
    
    print "Pre-Function Test 3: %s" % (test3) 
    print "sorted_list(test3): %s" % (sorted_list(test3))
    print "Post-Function Test 3: %s" % (test3) 
