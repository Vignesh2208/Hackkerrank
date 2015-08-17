string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
Dict = {}
i = 0
while i < len(string) :
    curr_char = string[i]
    if curr_char.isalpha() == True :
        if curr_char in Dict.keys() :
            if Dict[curr_char] == 0 :
                Dict[curr_char] = 1
            else :
                Dict[curr_char] = 0 
        else :
                Dict[curr_char] = 1
    i += 1
sum_val = sum(Dict.values())

if sum_val > 1 :
    found = False
else :
    found = True

if not found:
    print("NO")
else:
    print("YES")

