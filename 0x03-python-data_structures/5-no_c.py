#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy_str = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(copy_str))
