# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

M = {}
Prime = {}
Fact = {}
M[1] = 0
Fact[0] = 1


def is_prime(n):
    root = int(math.sqrt(n))
    if n == 1 :
        return 0
    
    i = 2
    while i <= root + 1 :
        if n % i == 0 and i != n:
            return 0
        i = i + 1
    return 1

def no_of_primes(n) :
    if n in M.keys() :
        return M[n]
    
    i = max(M.keys()) + 1
    no_of_primes = M[i-1]
    while i <= n :
        
        if is_prime(i) == 1 :
            no_of_primes = no_of_primes + 1
         
        M[i] = no_of_primes
        i = i + 1
        
    return M[n]

def find_factorial(n) :
    if n in Fact.keys() :
        return Fact[n]
    else :
        Fact[n]  = n*find_factorial(n-1)
        return Fact[n]
        
line_no = 0
for line in sys.stdin :
    if line_no == 0 :
        line_no = line_no + 1
        continue
    else :
        line_no = line_no + 1
        N = int(line)
        n_fact = find_factorial(N)
        min_vert = N%4
        total_no_of_ways = 0
        n_vert = min_vert
        n_hor = int(N/4)
        #n_total = n_hor_max + n_vert_min
        #n_total_fact = find_factorial(n_total)
        while n_vert <= N :
            n_hor = int((N - n_vert)/4)
            n_elements = n_vert + n_hor
            n_elements_fact = find_factorial(n_elements)
            n_rem_fact = find_factorial(n_elements - n_vert)
            n_vert_fact = find_factorial(n_vert)
            total_no_of_ways = total_no_of_ways + int(n_elements_fact/(n_rem_fact*n_vert_fact))
            n_vert = n_vert + 4
        #print "total no of ways = ",total_no_of_ways
        P = no_of_primes(total_no_of_ways)
        
        print P
