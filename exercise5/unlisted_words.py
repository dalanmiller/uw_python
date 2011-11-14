"""
Daniel Miller's Solution Exercise 5



===

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
import string

def unlisted_words(sample, reference): 
    s = (sample.translate(string.maketrans("",""),string.punctuation)).lower().split()
    r = (reference.translate(string.maketrans("",""),string.punctuation)).lower().split()
    return list(set([w for w in s if r.__contains__(w) == False]))  #list of all the words that appear in the sample string that do not appear in the reference string.
    
if __name__ == "__main__":
    test_sample = "For the past 33 years, I have looked in the mirror every morning and asked myself: 'If today were the last day of my life, would I want to do what I am about to do today?' And whenever the answer has been 'No' for too many days in a row, I know I need to change something. -Steve Jobs"
    test_ref = "mirror steve today no 33"

    print unlisted_words(test_sample, test_ref)






