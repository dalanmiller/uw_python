"""

+--

Exercise for week 9, Tues Dec 6, bring exercise to turn in (hardcopy)

Reading: see course web page

Exercise: Write a decorator that turns a function into a generator.
Write a module that defines a decorator function named generator,
which is used like this:

 @generator
 define f(x):
   ... 
   return ...

where f(x) here is a function with one argument.  Due to the
decorator, the argument of the decorated function f is an iterable
(for example, a list).  Then f(s) (where s is an iterable) is a
generator, where each call returns the result of applying the original
function to the next element of s.

Code this test case for your decorator:

 @generator
 define odd(i):
     return i % 2

 for y in odd([1,2,3]): print y

This test case should produce this output:
 
 1
 0
 1

"""


def generator(fn):
    def yielder(i):
        try:
            for x in i:
                yield fn(x)
        except:           
            yield i
    return yielder

@generator
def odd(i):
    return i % 2

if __name__ == "__main__":
    
    for y in odd([1,2,3]):  print y
