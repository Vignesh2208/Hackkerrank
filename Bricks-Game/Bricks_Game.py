# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def find_max_pts(S,W) :
    M = {}
    M[0] = W[0]
    M[-1] = 0
    S[-1] = 0
    i = 1
    while i < N :
        max_val = W[i] + S[i-1] - M[i-1] # remove one brick
        if i-1 >= 0 :
            if max_val < W[i] + W[i-1] + S[i-2] - M[i-2] : #remove 2 bricks
                max_val = W[i] + W[i-1] + S[i-2] - M[i-2]
            
            if i-2 >= 0 :
                if max_val < W[i] + W[i-1] + W[i-2] + S[i-3] - M[i-3] : #remove 3 bricks
                    max_val = W[i] + W[i-1] + W[i-2] + S[i-3] - M[i-3]
        M[i] = max_val
        i = i + 1
    return M[N-1]     
        

line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        line_no = line_no + 1
    elif line_no % 2 == 0 :
        N = int(line)
        line_no = line_no + 1
    else :
        W_string = line.split(' ')
        W = []
        S = {}
        for w in W_string :
            W.insert(0,(int(w)))
        i = 0
        temp = 0
        #print "N = ",N, " len(W) = ",len(W)
        while i < N :
            temp = temp + W[i]
            S[i] = temp
            i = i + 1
        pts = find_max_pts(S,W)
        print pts
        line_no = line_no + 1
