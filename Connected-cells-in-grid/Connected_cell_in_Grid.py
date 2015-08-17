# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Node :
    
    def __init__(self,id) :
        self.neighbours = []
        self.marked = 0
        self.id = id
        
        
    def get_neighbours(self) :
        return self.neighbours
    
    def mark(self) :
        self.marked = 1
    def get_mark(self) :
        return self.marked
    
    def add_neighbour(self,neighbour) :
    
        for entry in self.neighbours :
            if neighbour.id == entry.id :
                return
            
        self.neighbours.append(neighbour)
        
    def get_id(self) :
        return self.id

region_count = 0       


def dfs(Nodes,M,i,j,m,n) :
    global region_count 
    
    Nodes[i][j].mark()
    region_count = region_count + 1
    
    if i-1 >= 0 :
        if j - 1 >= 0 :
            if Nodes[i-1][j-1].get_mark() == 0 and M[i-1][j-1] == 1 :
                dfs(Nodes,M,i-1,j-1,m,n)
        if Nodes[i-1][j].get_mark() == 0 and M[i-1][j] == 1 :
            dfs(Nodes,M,i-1,j,m,n)                
    
        if j + 1 < n :
            if Nodes[i-1][j+1].get_mark() == 0 and M[i-1][j+1] == 1 :
                dfs(Nodes,M,i-1,j+1,m,n)
                
            
    
    if j - 1 >= 0 :
        if Nodes[i][j-1].get_mark() == 0 and M[i][j-1] == 1 :
            dfs(Nodes,M,i,j-1,m,n)
            
    if j + 1 < n :
        if Nodes[i][j+1].get_mark() == 0 and M[i][j+1] == 1 :
            dfs(Nodes,M,i,j+1,m,n)
                
                
    if i + 1 < m:
        if j - 1 >= 0 :
            if Nodes[i + 1][j-1].get_mark() == 0 and M[i + 1][j-1] == 1 :
                dfs(Nodes,M,i + 1,j-1,m,n)
                
        if Nodes[i + 1][j].get_mark() == 0 and M[i + 1][j] == 1 :
            dfs(Nodes,M,i + 1,j,m,n)                
    
        if j + 1 < n :
            if Nodes[i+ 1][j+1].get_mark() == 0 and M[i + 1][j+1] == 1 :
                dfs(Nodes,M,i + 1,j+1,m,n)
            
            
            
            
            
            
            
            
            
            
            
            
line_no = 1        
i = 0
M = {}
Nodes = {}
for line in sys.stdin :
    if line_no == 1 :
        m = int(line)
    
    elif line_no == 2 :
        n = int(line)
        
    else :
        M[i] = {}
        Nodes[i] = {}
        length = len(line)
        if line[length - 1] == '\n' :
            new_line = line[0:length-1]
        else :
            new_line = line
            
        ls = new_line.split(' ')
        j = 0
        while j < n :
            M[i][j] = int(ls[j])
            Nodes[i][j] = Node(i*n + j)
            j  = j + 1
            
        i = i + 1
    line_no = line_no + 1
max_region_count = -1    
    
i = 0
while i < m :
    j = 0
    while j < n :
        region_count = 0
        if M[i][j] == 1 and Nodes[i][j].get_mark() == 0 :
            dfs(Nodes,M,i,j,m,n)
            if region_count > max_region_count :
                max_region_count = region_count
                
        j = j + 1
    i = i + 1      
    
print max_region_count

