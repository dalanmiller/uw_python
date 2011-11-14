"""
Daniel Miller's Solution Exercise 5



===
Assignment for week 6, Tues Nov 15, bring exercise to turn in (hardcopy)

 Required reading: textbook chapters 15, 16, 17, 18
 http://www.greenteapress.com/thinkpython/html/book016.html
 http://www.greenteapress.com/thinkpython/html/book017.html
 http://www.greenteapress.com/thinkpython/html/book018.html
 http://www.greenteapress.com/thinkpython/html/book019.html

Write a function unlisted_words that takes two string arguments, a
sample string and a reference string, and returns a list of all the
words that appear in the sample string that do not appear in the
reference string.  A word is a string of alphabetic characters (with no spaces,
numbers, or punctuation), where case is not significant (so python,
Python and PYTHON are the same word).  The output list must not
contain duplicates, each word must appear only once.

Write the function in a module also called unlisted_words that
contains a short sample string and a short reference string for
testing (so it is obvious from the returned list whether the function
is working correctly).  The module calls the function on these
strings and prints the returned list.

The module also reads a large sample string and a large reference
string (from a file or a web page, for example), calls the function on
them, and prints the output.  You may choose the sources for the
reference and sample strings yourself, or you may use these:
 sample: http://staff.washington.edu/jon/uw_python/fall_2011/big.txt
 reference: http://staff.washington.edu/jon/uw_python/fall_2011/words

"""
import string, re


def unlisted_words(sample, reference): 
    s = (sample.translate(string.maketrans("",""),string.punctuation)).lower().split()
    r = (reference.translate(string.maketrans("",""),string.punctuation)).lower().split()

    for w in s:
        if s.__contains__(w)

    return #list of all the words that appear in the sample string that do not appear in the reference string.
    







