# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


Board = {}

def find_min_changes(N,M,K,p,q) :
    Mk = {}
    Mk_1 = {}
    if p == 0 and q == 0 :
        return 0
    i = 0
    while i < N :
        Mk[i] = {}
        Mk_1[i] = {}
        i = i + 1

    k = 0
    while k <= K :
        if k == 0 :
            i = 0
            while i < N :
                j = 0
                while j < M :
                    Mk_1[i][j] = -1
                    Mk[i][j] = -1
                    j = j + 1
                i = i + 1
            Mk_1[p][q] = 0
            Mk[p][q] = 0
        else :
            i = 0
            while i < N :
                j = 0
                while j < M :
                    U = 1
                    L = 1
                    R = 1
                    D = 1
                    min_val = 100000
                    changed_value = 'N'
                    if True :
                        if i == 0 :
                            U = 0
                        if j == 0 :
                            L = 0
                        if i == N-1 :
                            D = 0
                        if j == M-1 :
                            R = 0
                        if U == 1 :
                            if Mk_1[i-1][j] != -1 :
                                if Board[i][j] == 'U' :
                                    if min_val > Mk_1[i-1][j] :
                                        min_val = Mk_1[i-1][j]
                                        changed_value = 'U'
                                else :
                                    if min_val > Mk_1[i-1][j] + 1:
                                        min_val = Mk_1[i-1][j] + 1
                                        changed_value = 'U'
                        if D == 1 :
                            if Mk_1[i+1][j] != -1 :
                                if Board[i][j] == 'D' :
                                    if min_val > Mk_1[i+1][j] :
                                        min_val = Mk_1[i+1][j]
                                        changed_value = 'D'
                                else :
                                    if min_val > Mk_1[i+1][j] + 1:
                                        min_val = Mk_1[i+1][j] + 1
                                        changed_value = 'D'
                        if L == 1 :
                            if Mk_1[i][j-1] != -1 :
                                if Board[i][j] == 'L' :
                                    if min_val > Mk_1[i][j-1] :
                                        min_val = Mk_1[i][j-1]
                                        changed_value = 'L'
                                else :
                                    if min_val > Mk_1[i][j-1] + 1:
                                        min_val = Mk_1[i][j-1] + 1
                                        changed_value = 'L'
                        if R == 1 :
                            if Mk_1[i][j+1] != -1 :
                                if Board[i][j] == 'R' :
                                    if min_val > Mk_1[i][j+1] :
                                        min_val = Mk_1[i][j+1]
                                        changed_value = 'R'
                                else :
                                    if min_val > Mk_1[i][j+1] + 1:
                                        min_val = Mk_1[i][j+1] + 1
                                        changed_value = 'R'
                        if changed_value != 'N' :
                            if Mk[i][j] == - 1:
                                Mk[i][j] = min_val                              
                                #Board[i][j] = changed_value
                            else :
                                if min_val < Mk[i][j] :
                                    Mk[i][j] = min_val
                                    #Board[i][j] = changed_value
                        #else :
                        #    Mk[i][j] = -1
                    j = j + 1
                i = i + 1
            a = 0
            while a < N :
                b = 0
                while b < M :
                    Mk_1[a][b] = Mk[a][b]
                    b = b + 1
                a = a + 1
            
        k = k + 1
    return Mk[0][0]
line_no = 1 
for line in sys.stdin :
    if line_no == 1 :
        ls = line.split(' ')
        N = int(ls[0])
        M = int(ls[1])
        K = int(ls[2])
        line_no = line_no + 1
        i = 0
    else :
        Board[i] = {}
        j = 0
        length = len(line)
        if line[length -1] == '\n' :
            new_line = line[0:length-1]
        else :
            new_line = line
        while j < len(new_line) :
            Board[i][j] = new_line[j]
            if new_line[j] == '*' :
                p = i
                q = j
            j = j + 1
        i = i + 1
        
        line_no = line_no + 1
nchanges = find_min_changes(N,M,K,p,q)
print nchanges
