# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def find_LCS(A,B,n,m) :
    L = {}
    LCS = {}
    i = 0
    while i < n :
        L[i] = {}
        LCS[i] = {}
        i = i + 1
    
    i = 0
    while i < n :
        j = 0 
        while j < m :
            if i == 0 or j== 0 :
                if A[i] == B[j] :
                    L[i][j] = 1
                    LCS[i][j] = A[i]
                else :
                    if i == 0 and j == 0 :
                        L[i][j] = 0
                        LCS[i][j] = ""
                    elif i == 0 :
                        L[i][j] = L[i][j-1]
                        LCS[i][j] = LCS[i][j-1]
                    else :
                        L[i][j] = L[i-1][j]
                        LCS[i][j] = LCS[i-1][j]
            else :
                if A[i] == B[j] :
                    L[i][j] = L[i-1][j-1] + 1
                    LCS[i][j] = LCS[i-1][j-1] + " " + A[i]
                else :
                    if L[i][j-1] > L[i-1][j] :
                        LCS[i][j] = LCS[i][j-1]
                        L[i][j] = L[i][j-1]
                    else :
                        LCS[i][j] = LCS[i-1][j]
                        L[i][j] = L[i-1][j]
            j = j + 1
        
        i = i + 1
    
    print LCS[n-1][m-1]
        
line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        
        
        ls = line.split(' ')
        n = int(ls[0])
        m = int(ls[1])
        line_no = line_no + 1
    elif line_no %2 == 0 :
        line_len = len(line)
        if line[line_len - 1] == '\n' :
            new_line = line[0:line_len-1]
            A = new_line.split(' ')
        else :
            A = line.split(' ')
        line_no = line_no + 1
    else :
        line_len = len(line)
        if line[line_len - 1] == '\n' :
            new_line = line[0:line_len-1]
            B = new_line.split(' ')
        else :
            B = line.split(' ')
        
        line_no = line_no + 1
        find_LCS(A,B,n,m)    
        
