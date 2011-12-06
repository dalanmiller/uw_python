"""
Daniel Miller's Solution - 10/15/2011

input:

print_grid(5)

output:

+=====+=====+
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
+=====+=====+
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
+=====+=====+

"""
#! /usr/bin/python

def main_line(num):
    print "+"+num*"="+"+"+num*"="+"+"

def edge_line(num):
    for x in xrange(0, num):
        print "|"+num*" "+"|"+num*" "+"|"

def print_grid(num):
    main_line(num)
    edge_line(num)
    main_line(num)
    edge_line(num)
    main_line(num) 

if __name__ == "__main__":
    print_grid(int(raw_input("Please enter 'n': ")))
