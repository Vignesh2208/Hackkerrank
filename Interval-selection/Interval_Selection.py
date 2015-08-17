#!/bin/python
from operator import itemgetter


def intersects(a1,b1,a2,b2) :
    if a1 <= a2 :
        if b1 >= a2 :
            return True
        else :
            return False
    elif b2 >= a1 :
        return True
    else :
        return False

def len_largest_subset(Sorted_intervals,N,t) :
    L = {}
    Max = {}
    Next = {}
    i = 0
    max_i = 0
    max_j = 0
    A = []
    B = []
    while i < N :
        A.append(Sorted_intervals[i][0])
        
        B.append(Sorted_intervals[i][1])
        
        Max[i] = {}
        i = i + 1      
    i = N-1
    while i >= 0 :
        if i == N-1 :
            Next[i] = -1
        else :
            if B[i] < A[i+1] :
                Next[i] = i+1
            else :
                j = i+2
                #if Next[i+1] != -1 :
                #    end_pt = Next[i+1]
                #else :
                end_pt = N-1
                while j <= end_pt and A[j] <= B[i] :
                    j = j + 1
                if j > end_pt :
                    Next[i] = -1
                else :
                    Next[i] = j
                    
        i = i - 1
    max_val = -1    
    i = N-1
    while i >= 0 :
        j = i-1 
        while j >= 0 :
            if i == N-1 :
                Max[i][j] = 2
                Lij = 2
                if max_val < Lij :
                    max_val = Lij
                    
            else :
                if intersects(A[j],B[j],A[i],B[i]) == True :
                    next_j = Next[j]
                    next_i = Next[i]
                    
                    if B[j] > B[i] :
                        larger = j
                        smaller = i
                    else :
                        larger = i
                        smaller = j
                        
                    if next_i == -1 and next_j == -1 :
                        Lij = 2
                        
                    elif Next[larger] == -1 :
                        
                        Lij = 1 + Max[Next[smaller]][larger]
                    else :
                        if Next[smaller] == -1 :
                            # can only happen if B[j] = B[i]
                            Lij = 1 + Max[Next[larger]][smaller] # Can also be Lij = 1 + Max[Nex[larger]][larger]
                            
                        else :
                            Lij = 1 + Max[Next[smaller]][larger]
                    
                    
                    if Lij > Max[i+1][j] :
                        Max[i][j] = Lij
                    else :
                        Max[i][j] = Max[i+1][j]
                        
                    if max_val < Lij :
                        max_val = Lij
                else :
                    next_i = i + 1
                    Lij = 1 + Max[next_i][i]
                    if Lij > Max[i+1][j] :
                        Max[i][j]  = Lij
                    else :
                        Max[i][j] = Max[i+1][j]
                    if max_val < Lij :
                        max_val = Lij
                        
            j = j - 1
        i = i - 1
    #if t== 8 :
    #    print "Next = ",Next
    #    print "Max = ", Max
        
    return max_val
# code snippet for illustrating input/output

test = int(raw_input())

for t in range(0, test):

    N = int(raw_input())
    
    Sorted_intervals = []
    
    Intervals = {}
    n = 0
    for i in range(0, N):

        numbers = raw_input()
        a, b = [int(x) for x in numbers.split(' ')]
        #Intervals.append((a,b))           
        if a in Intervals.keys() :
            #if b not in Intervals[a] :
            Intervals[a].append(b)
            Intervals[a].sort()
            n = n + 1
        else :
            Intervals[a] = []
            Intervals[a].append(b)
            n = n + 1
            
    sorted_keys = Intervals.keys()
    sorted_keys.sort()
        
    for a in sorted_keys :
        for b in Intervals[a] :
            Sorted_intervals.append((a,b))
            
    
    
    val = len_largest_subset(Sorted_intervals,n,t)
    if True :
        print val
        #print Sorted_intervals
        
    result = 0
   

