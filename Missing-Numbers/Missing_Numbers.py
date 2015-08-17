# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def find_missing_nos(A,B,n,m,Amin,Bmin) :
    Ca = [0]*101
    Cb = [0]*101
    
    i = 0
    while i < m :
        if i < n :
            Ca[A[i] - Amin] = Ca[A[i] - Amin] + 1
        Cb[B[i] - Bmin]  = Cb[B[i] - Bmin] + 1
        i = i + 1
    i = 0
    
    while i < 101 :
        diff = Cb[i]
        if i < n :
            diff = Cb[i] - Ca[i]
            
        if diff > 0 :
            
            out_val = i + Bmin
            sys.stdout.write(str(out_val) + str(" "))
            
        i = i + 1
                
        
            
    
line_no = 1
for line in sys.stdin :
    if line_no == 1 :
        n = int(line)
    elif line_no == 2 :
        ls = line.split(' ')
        A = []
        Amin = 1000000000
        for e in ls :
            A.append(int(e))
            if int(e) < Amin :
                Amin = int(e)
                
    elif line_no == 3 :
        m = int(line)
    elif line_no == 4 :
        ls = line.split(' ')
        B = []
        Bmin = 10000000000
        for e in ls :
            B.append(int(e))
            if int(e) < Bmin :
                Bmin = int(e)
        find_missing_nos(A,B,n,m,Amin,Bmin)            
    line_no = line_no + 1
