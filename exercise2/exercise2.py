"""
Daniel Miller's Excercise 2

Assignment due week 3, Tues Oct 25, bring exercise to turn in (hardcopy)

 Required: Ch. 8, 9, 14
 Optional: http://docs.python.org/library/stdtypes.html#string-methods
            http://docs.python.org/howto/regex.html
            http://docs.python.org/howto/unicode.html
	    http://farmdev.com/talks/unicode/

 Exercise: Write a function named concordance that takes three
  arguments: a string, a file object for a file that is open for
  reading, and a file object for a file that is open for writing.  The
  function writes in the output file the line numbers and contents of all the lines
  in the input file where the string occurs.  Write the function in a module
  concordance.py that also opens the input and output files, calls the function,
  and closes the files.

Method/Attribute	Purpose
match()	    Determine if the RE matches at the beginning of the string.
search()	Scan through a string, looking for any location where this RE matches.
findall()	Find all substrings where the RE matches, and returns them as a list.
finditer()	Find all substrings where the RE matches, and returns them as an iterator.


"""
from re import search
from sys import argv 

def concordance( s, r, w  ):  #string, read object, write object
    """
    This function takes a string, an open read object, and an open write object.
    It then reads through every line of the read object and if a match is found with the provided string
    will write the line number where the matched string was found in the read object and the contents of that line into the write object
    """
    i = 0
    total = 0   
    if (not r or not w): #Checking that the objects are legitimate
        print "Read or write objects broken, please fix" 
    for line in r:
        if search(s,line): #If the compiled search string s is found in the line. 
            print "Line %s: %s" % [i,line]            
            #w.write("Line %s: %s" % [i,line])
            total += 1 
        i+=1
        
    print "Total lines written to output file: %s" % [total] s

    r.close(); w.close() #Close the file objects


if __name__ == "__main__": 
    try:
        s == type(string)
        r = sys.argv[2]
        w = sys.argv[3] 
        concordance(sys.argv[1], open(s,"r") , open(w,"w")) #Problem instructions indicate that opened file objects should be provided, but providing paths also should work.
    except: 
        print "Something went wrong with your supplied variables, please try again" 





