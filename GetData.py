# GetTextData.py
# CS 1110 Professors (cs-1110profs-L@cornell.edu)
# March 2016

""" This module provides functions that can be
used to extract data from text files.
"""


def fileToStringList(FName):
    """ Returns a list of strings L with the property that
    L[k] is line k in the file with name FName.

    PreC: FName is a string that names the file that is to be read.
    It should include the filename's suffix, e.g., for file
    MyFile.txt, FName must be 'MyFile.txt', not 'MyFile'.
    The file must be in the current working directory.
    """
    L = []
    with open(FName,"r") as F:
        for s in F:
            # Remove trailing newline character...
            s1=s.rstrip("\n")
            # Remove trailing carriage return...
            s2 = s1.rstrip("\r")
            # Append this "cleaned up" file line...
            L.append(s2)
    return L


def stringToWordList(s):
    """Returns t.split() where t is obtained from s.lower() by replacing
    every non-letter in this string with a blank. Basically, it returns
    a list of the 'words' (sequences of letters) in s.

    PreC: s is a string.
    """
    t = ''
    for c in s.lower():
        if c in 'abcdefghijklmnopqrstuvwxyz':
            t = t + c
        else:
            t = t + ' '
    return t.split()


