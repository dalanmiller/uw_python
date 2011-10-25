"""
Daniel Miller's Excercise 2

Usage: 

One can import concordance.py or can also call it via the command line and use a string and paths to file names as arguments. 

"import concordance.py"

"$ python concordance.py "a_string" ~/input.txt ~/output.txt" 

===

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

"""

from re import search,compile
from sys import argv 

def concordance( s, r, w  ):  #string, read object, write object
    """
    This function takes a string, an open read object, and an open write object.
    It then reads through every line of the read object and if a match is found with the provided string will write the line number where the matched string was found in the read object and the contents of that line into the write object.
    """
    
    query = compile(s)
    i = 0
    total = 0
    if (not r or not w): #Checking that the objects are legitimate
        print "Read or write objects broken, please fix" 
    for line in r:
        if search(query,line): #If the compiled search string s is found in the line.            
            content = u"Line %s: %s" % (i,line)
            w.writelines(content)
            total += 1 
        i+=1
    print "Total lines/matches written to output file: %s" % (total) 

    #Close the file objects
    r.close()
    w.close() 

if __name__ == "__main__": 
    try:
        s == type(string)
        r = sys.argv[2]
        w = sys.argv[3] 
        concordance(sys.argv[1], open(s,"r") , open(w,"w")) #Problem instructions indicate that opened file objects should be provided, but providing paths also should work.
    except: 
        print "Something went wrong with your supplied variables, please try again" 





