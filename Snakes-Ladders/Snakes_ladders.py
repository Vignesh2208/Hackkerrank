# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def shortest_path(graph):
    s = 1
    d = [100000]*101
    prev = [-1]*101
    
    d[s] = 0
    i = 1
    while i <= 100 :
        j = 1
        while j < 100 :
            out_edges = graph[j].keys()
            for k in out_edges :
                if d[j] + graph[j][k] < d[k] :
                    prev[k] = j
                    d[k] = d[j] + graph[j][k]
            j = j + 1
        i = i + 1

    k = 100
    length = 0
    
    if d[k] == 100000 :
        print "-1"
        return
    
    while prev[k] > 0 :
        length = length + graph[prev[k]][k]        
        if prev[k] == 1 :
            break
        k = prev[k]
        
    print length
line_no = 0
for line in sys.stdin :
    if line_no == 0 :
        line_no = line_no + 1
        
    elif line_no == 1 :
        N = int(line)
        graph = {}
        i = 1
        while i < 100 :
            graph[i] = {}
            j = i + 1
            while j <= 100 and j <= i + 6:
                graph[i][j] = 1
                j = j + 1
            i = i + 1
        line_no = line_no + 1
        
        
    elif line_no >= 2 and line_no < 2 + N :
        ls = line.split(' ')
        n1 = int(ls[0])
        n2 = int(ls[1])
        graph[n1][n2] = 0
        line_no = line_no + 1
        
    elif line_no == 2 + N :
        M = int(line)
        line_no = line_no + 1
        
    elif line_no >= 2 + N + 1 and line_no < 2 + N + 1 + M :
        ls = line.split(' ')
        n1 = int(ls[0])
        n2 = int(ls[1])  
        del graph[n1]
        graph[n1] = {}
        graph[n1][n2] = 0
        line_no = line_no + 1
        if line_no == 2 + N + 1 + M :
            shortest_path(graph)
            line_no = 1
