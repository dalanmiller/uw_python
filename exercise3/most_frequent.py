"""
Daniel Miller's Solution


===

Assignment due week 4, Tues Nov 1, bring exercise to turn in (hardcopy)

 Required reading: Ch. 10, 12, 13, 14

 Exercise: 12.3 in Downey - write the function most_frequent that takes a string
 and prints the letters in decreasing order of frequency. ...

"""
from sys import argv 

def most_frequent(s):
    if (type(s) != str): print "Please verify that the variable is a string"
    
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1

    for x in sorted(d.items(), key=lambda (k,v) : (v,k), reverse=True):
        print "%s: %s" % (x[0], x[1]) 


if __name__ == "__main__":
    try: 
        if (argv[1]): most_frequent(str(argv[1]))
    except: most_frequent(raw_input("Please enter the string you would like to most_frequentize: "))
       

 
        




