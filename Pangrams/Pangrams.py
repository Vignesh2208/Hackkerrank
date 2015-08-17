# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    string = line
    i = 0
    Dict = {}
    while i < len(string) :
        if string[i].isalpha() == True :
            curr_char = string[i].lower()
            if curr_char in Dict.keys() :
                pass
            else :
                Dict[curr_char] = 1
        i += 1
    if len(Dict.keys()) == 26 :
        print "pangram"
    else :
        print "not pangram"
            
