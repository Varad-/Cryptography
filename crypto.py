"""
@author: varad
Quick tool to convert between numeric strings and alphabetic strings with
(a,b,c,...,z)=(0,1,2,...,25)(mod 26)
"""

import string

def main():
    print 'Cryptoconverter\n'
    print 'Enter either numbers separated by spaces or a string of letters.'
    print 'Quit by entering \'!q\'\n'
    inp = raw_input('')
    while(inp!='!q'):
        if inp[-1] not in string.digits:
            #input string is alphabetic
            strls = list(inp.upper())
            numls = [num(i) for i in strls]
            print strls
            print numls
        else:
            #input string is numeric
            numls = [int(i)%26 for i in inp.split()]
            strls = [letter(n) for n in numls]
            print numls
            print strls
        
        inp = raw_input('')
    
def num(letter):
    """takes a letter of either lowercase or uppercase and returns its 
    associated numerical value between 0 and 25.
    returns -1 if not one of the 52 possible letters
    returns 0 if letter is empty"""
    return string.uppercase.find(letter.upper())

def letter(num):
    """takes any integer and returns the corresponding letter using mod 26."""
    return chr(int(num)%26 + 97)

main()
