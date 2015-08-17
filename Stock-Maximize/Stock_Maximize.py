# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# With Dynamic Programming (Bad choice O(N^2))
def find_max_profit_DP(N,C) :
    M = {}
    Sub = {}
    
    i = 0
    M[N] = {}
    Sub[N] = {}
    while i <= N-1 :
        M[N][i] = C[N-1]*i
        if i == 0 : 
            Sub[N][i] = M[N][i]
        else:
            if M[N][i] > Sub[N][i-1] + C[N-2] :
                Sub[N][i] = M[N][i]
            else :
                Sub[N][i] = Sub[N][i-1] + C[N-2]
            
        i = i + 1
    i = N-1
    while i >= 1 :
        j = 0
        M[i] = {}
        Sub[i] = {}
        while j <= i-1 : # Currently have j shares at the start of day i            
            max_val = Sub[i+1][j]            
            if max_val < M[i+1][j+1] - C[i-1] : # Buy one share on day i
                max_val = M[i+1][j+1] - C[i-1]
            M[i][j] = max_val
            
            if i != 1 :
                if j == 0 : 
                    Sub[i][j] = M[i][j]
                else:
                    if M[i][j] > Sub[i][j-1] + C[i-2] :
                        Sub[i][j] = M[i][j]
                    else :
                        Sub[i][j] = Sub[i][j-1] + C[i-2]
            j = j + 1
            
            
        Sub.pop(i+1,None)
        M.pop(i+1,None)
        i = i - 1
    return M[1][0]

#Without DP O(N)
def find_profit_upto_max_peak(N,C) :
    cost = 0
    n = 0
    peak_pos = 0
    i = 0
    while i < N :
        if C[i] > C[peak_pos] :
            peak_pos = i
        i = i + 1
    i = 0
    
    while i <= peak_pos -1 :
        cost = cost + C[i]
        n = n + 1
        i = i + 1
    return (n*C[peak_pos] - cost,peak_pos)


def find_max_profit_non_DP(N,C) :
    i = 0
    Cost = C
    total_profit = 0
    curr_peak = 0
    while i < N :
        (profit,peak) = find_profit_upto_max_peak(N-i,Cost)
        curr_peak = curr_peak + peak + 1
        #print "profit = ", profit, "peak = ", curr_peak
        total_profit = total_profit + profit
        i = curr_peak
        if curr_peak < N-1 :
            j = 0
            Cost = []
            while j < N- i :
                Cost.append(C[i + j])
                j = j + 1
        
    return total_profit



line_no = 0
for line in sys.stdin:
    if line_no == 0:
        line_no = line_no + 1
        continue
    elif line_no % 2 == 1 :
        N = int(line)
        line_no = line_no + 1
        #print N
    else :
        Cost_string_list = line.split(' ')
        C = []
        for cost in Cost_string_list :
            C.append(int(cost))
        #print C   
        max_profit = find_max_profit_non_DP(N,C)    
        line_no = line_no + 1
        print max_profit
            
    
