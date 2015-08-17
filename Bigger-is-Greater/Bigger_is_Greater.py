# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
line_no = 0
for line in sys.stdin :
    if line_no == 0 :
        line_no = 1
        continue
    curr_string = line
    
    str_len = len(curr_string)
    if curr_string[len(curr_string)-1] == '\n' :
        str_len -= 1
    #else :
    #    curr_string = curr_string + '\n'
    i = str_len - 1
    curr_largest = -1
    curr_largest_char = ''
    min_greater_index = -1
   
    while i >= 0 :
        if curr_largest <= ord(curr_string[i]) :
            curr_largest = ord(curr_string[i])
            curr_largest_char = curr_string[i]
        else :
            j = i + 1
            min_greater = curr_largest_char
            min_greater_index = i + 1
            while j <= str_len - 1 :
                if ord(curr_string[j]) > ord(curr_string[i]) :
                    if ord(curr_string[j]) < ord(min_greater) :
                        min_greater = curr_string[j]
                        min_greater_index = j
                j = j + 1
            break
    
        
        
        i = i - 1
        
    if min_greater_index == -1 :
        print "no answer"
    else :
        if i == 0 :
            new_string_unchanged_part = ""
        else :
            new_string_unchanged_part = curr_string[0:i]

        if min_greater_index == str_len - 1 :
            new_string_changed_part = curr_string[min_greater_index] + ''.join(sorted(curr_string[i:min_greater_index]))
        else :
            new_string_changed_part = curr_string[min_greater_index] + ''.join(sorted(curr_string[i:min_greater_index]+curr_string[min_greater_index+1:str_len]))
        new_string = new_string_unchanged_part + new_string_changed_part
        print new_string
            
    
