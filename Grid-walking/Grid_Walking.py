# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
fact = {}

def fact_init() :
    fact[0] = 1
    for i in range(1,301) :
        fact[i] = i * fact[i-1]

def choose_mod(N,k) :
    val = fact[N]/(fact[k]*fact[N-k])
    return val
        
def total_no_of_ways(M,W) :
   
    T = {}    
    N = len(W.keys())
    ls = W.keys()
    if N == 0 :
        print 0
        return
    ls.sort()
    start_idx = N-1
    while start_idx >= 0 :
        T[start_idx] = {}
        for rem_steps in range(0,M+1) :
            if start_idx == N-1 :
                if rem_steps == 0 :
                    T[start_idx][0] = 1
                
                else:
                    T[start_idx][rem_steps] = W[ls[start_idx]][rem_steps]
           
            else :
                if rem_steps == 0 :
                    T[start_idx][0] = 1
                
                else :
                    T[start_idx][rem_steps] = 0
                    for k in range(0,rem_steps + 1) :
                        if k == 0 :                            
                            T[start_idx][rem_steps]  = T[start_idx + 1][rem_steps]
                        else :
                            T[start_idx][rem_steps]  = T[start_idx][rem_steps] + choose_mod(rem_steps,k)*W[ls[start_idx]][k]*T[start_idx + 1][rem_steps - k]

        start_idx = start_idx - 1
                            
    ans = T[0][M]%(1000000007)
    print ans
    


def find_no_of_ways(N,M,D,X) :
    
    W = {}
    Remove_list = []
    i = 0    
    while i < N :
        Pts = {}
        W[i] = {}
        for xi in range(1,D[i] + 1) :
            Pts[xi] = {}
        if D[i] == 1 :
            if i not in Remove_list :
                Remove_list.append(i)
            
        for t in range(1,M + 1) :
            for xi in range(1,D[i] + 1) :
                if t == 1 :
                    if xi == 1 or xi == D[i] :
                        Pts[xi][t] = 1                   
                    
                    elif xi != 1 and xi != D[i] :
                        Pts[xi][t] = 2
                
                else :
                    if xi == 1 and D[i] == 1 :
                        Pts[xi][t] = 1  # not used
                        
                    elif xi == 1 :
                        Pts[xi][t] = Pts[xi+1][t-1]                    
                    
                    elif xi == D[i] :
                        Pts[xi][t] = Pts[xi - 1][t-1]
                    
                    elif xi != 1 and xi != D[i] :
                        Pts[xi][t] = Pts[xi + 1][t-1] + Pts[xi - 1][t-1]                       
                
                
            
            W[i][t] = Pts[X[i]][t]   
        i = i + 1 
    
    for idx in Remove_list :
        W.pop(idx,None)
    
    
    total_no_of_ways(M,W)


line_no = 0
fact_init()
for line in sys.stdin :
    if line_no == 0 :
        line_no = line_no + 1
    else :
        if line_no % 3 == 1 :
            ls = line.split(' ')
            N = int(ls[0])
            M = int(ls[1])
            line_no = line_no + 1
        elif line_no % 3  == 2 :
            X = []
            length = len(line)
            if line[length - 1] == '\n' :
                new_line = line[0:length-1]
            else :
                new_line = line
            
            ls = new_line.split(' ')
            for c in ls :
                if c != ' ' :
                    X.append(int(c))
            line_no = line_no + 1
        else :
            D = []
            length = len(line)
            if line[length - 1] == '\n' :
                new_line = line[0:length-1]
            else :
                new_line = line
            
            ls = new_line.split(' ')
            for c in ls :
                if c != ' ' :
                    D.append(int(c))
            find_no_of_ways(N,M,D,X)
            line_no = line_no + 1
                   
