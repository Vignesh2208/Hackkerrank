# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def check_arrangement(N,G,A,sum_val) :
    Mi = {}
    Mi_1 = {}
    
    i = N-1
    while i >= 0 :
        j = 0
        while j <= G :
            if i == N-1 :
                if j < A[i] :
                    Mi_1[j] = 0
                else :
                    Mi_1[j] = A[i]
            else :
                if j < A[i] :
                    Mi[j] = Mi_1[j]
                else :
                    val1 = A[i] + Mi_1[j-A[i]]
                    val2 = Mi_1[j]
                    if val1 > val2 :
                        Mi[j]  = val1
                    else :
                        Mi[j] = val2

            j = j + 1
        if i != N-1 :
            Mi_1 = Mi.copy()
        i = i - 1
        
    max_sum = Mi[G]        
    rem_sum = sum_val - max_sum
    if rem_sum <= G :
        print "YES"
    else :
        print "NO"


line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        line_no = line_no + 1
    elif line_no % 2 == 0 :
        ls = line.split(' ')
        N = int(ls[0])
        G = int(ls[1])
        line_no = line_no + 1
    else :
        length = len(line)
        if line[length -1] == '\n' :
            new_line = line[0:length-1]
        else :
            new_line = line
        ls = new_line.split(' ')
        A = []
        sum_val = 0
        not_possible = 0
        for e in ls :
            A.append(int(e))
            if int(e) > G :
                not_possible = 1
            sum_val = sum_val + int(e)
        if sum_val > 2*G or not_possible == 1 :
            print "NO"
        elif sum_val <= G :
            print "YES"
        else :
            
            A.sort(reverse=True)
            check_arrangement(N,G,A,sum_val)
        line_no = line_no + 1
