# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

def find_max_sum(N,A) :
    S = {}
    i = 0
    while i < N :
        S[i] = {}
        i = i + 1
    i = 0
    while i < N :
        if i == 0 :
            S[0][0] = 0
            S[0][1] = 0
        else :
            if S[i-1][0] + abs(A[i] - A[i-1]) > S[i-1][1] + abs(A[i] - 1) :
                S[i][0] = S[i-1][0] + abs(A[i] - A[i-1])
            else :
                S[i][0] = S[i-1][1] + abs(A[i] - 1)
             
            if S[i-1][0] + abs(1 - A[i-1]) > S[i-1][1]  :
                S[i][1] = S[i-1][0] + abs(1-A[i-1])
            else :
                S[i][1] = S[i-1][1]
        i = i + 1
    
    if S[N-1][0] > S[N-1][1] :
        return S[N-1][0]
    else :
        return S[N-1][1]
    

line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        line_no = line_no + 1
        continue
    elif line_no % 2 == 0 :
        N = int(line)
        line_no = line_no + 1
    else :
        length = len(line)
        if line[length - 1] == '\n' :
            new_line = line[0:length-1]
        else :
            new_line = line
        ls = new_line.split(' ')
        B = []
        for c in ls :
            if c != '' :
                B.append(int(c))
        val = find_max_sum(N,B)
        print val
        line_no = line_no + 1
