# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

NW = {}

def no_of_ways(N,C) :
    M = len(C)
    i = 0
    while i <= N :
        j = M-1
        last_seen = 0
        while j >= 0 :
            if i < C[j] :
                NW[i][j] = 0
            else :
                if i == C[j] :
                    NW[i][j] = 1
                    last_seen = j
                else : # i > C[j]
                    #k = 0
                    #while k <= last_seen :
                    #    NW[i][j] = NW[i][j] + NW[i-C[k]][k]
                    #    k = k + 1
                    #print "i = ",i, "j = ",j
                    if j == M - 1 : 
                        NW[i][j] = NW[i-C[j]][j]
                    else :
                        NW[i][j] = NW[i-C[j]][j] + NW[i][j+1]
            j = j - 1
        i = i + 1                    
    #print NW
    return NW[N][0]
                    

line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        ls = line.split(' ')
        N = int(ls[0])
        M = int(ls[1])
        line_no = line_no + 1
    else :
        
        length = len(line)
        if line[length - 1] == '\n' :
            new_line = line[0:length - 1]
        else :
            new_line = line
        Cl = new_line.split(' ')
        C = []
        
        for c in Cl :
            if c != '' :
                C.append(int(c))
        C.sort()
        
        i = 0
        while i <= N :
            NW[i] = {}
            i = i + 1
        n_ways = no_of_ways(N,C)
        print n_ways
        break
