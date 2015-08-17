# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    parameters = line.split(' ')
    A = int(parameters[0])
    B = int(parameters[1])
    N = int(parameters[2])
    Fib_dict = {}
    Fib_dict[1] = A
    Fib_dict[2] = B
    i = 3
    while i <= N :
        Fib_dict[i] = Fib_dict[i-1]*Fib_dict[i-1] + Fib_dict[i-2]
        i += 1
    print Fib_dict[N]
                                                                  
