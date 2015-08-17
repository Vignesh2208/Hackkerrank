# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def max_sum_contiguous(A,N) :
    n = N
    m = [] #m[i] is the maximum contiguous sum with A[i] at the start
    i = 0
    while i <= n-1 :
        m.append(0)
        i += 1
    i = n-1
    while i >= 0 :
        if i == n-1 :
            m[n-1] = A[n-1]
        else :
            j = i + 1
            total = 0
            while  j < n and A[j] < 0:
                total += A[j]
                if j == n - 1 :
                    j = n
                    break
                j += 1
            if j  == n :
                m[i] = A[i]
            elif A[i] + total + m[j] > A[i] :
                m[i] = A[i] + total + m[j]
            else :
                m[i] = A[i]
        i = i - 1
    i = 0
    max_val = -100000
    while i <= n-1 :
        if max_val < m[i] :
            max_val = m[i]
        i += 1
    return max_val

def max_sum_non_contiguous(A,N) :
    n = N
    m = [] # m[i] is the maximum non contiguous sum in A[i..n-1]
    i = 0
    while i <= n-1 :
        m.append(0)
        i += 1
    i = n-1
    while i >= 0 :
        if i == n-1 :
            m[n-1] = A[n-1]
        else :
            max_val = 0
            a = m[i+1] + A[i]
            b = A[i]
            c = m[i+1]
            if a >= b :
                if a >= c :
                    m[i] = a
                else :
                    m[i] = c
            else :
                if b >= c :
                    m[i] = b
                else :
                    m[i] = c
        i = i - 1
    return m[0]
     
input_list = []
for line in sys.stdin:
    input_list.append(line)
T = int(input_list[0])
i = 0
while i < 2*T :
    N = int(input_list[1+i])
    A = []
    S = input_list[2+i]
    S = S.split()
    for e in S :
        A.append(int(e))
    
    max_cont = max_sum_contiguous(A,N)
    max_non_cont = max_sum_non_contiguous(A,N)
    i += 2
    print max_cont,max_non_cont

    
    
        
