# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Node :
    
    def __init__(self) :
        self.marked = 0
        self.parent_i = -1
        self.parent_j = -1        
        self.n_children = 0
        
    def mark(self) :
        self.marked = 1
    
    def get_mark(self) :
        return self.marked
           
    def add_child(self) :
        self.n_children = self.n_children + 1
        
    def get_n_children(self) :
        return self.n_children
        
    def get_parent(self) :        
        return (self.parent_i,self.parent_j)
    
    def set_parent(self,x,y) :
        self.parent_i = x
        self.parent_j = y

      


def dfs(Nodes,M,i,j,m,n) :
    
    Nodes[i][j].mark()  
       
    
    if i-1 >= 0 :
        
        if Nodes[i-1][j].get_mark() == 0 and (M[i-1][j] == '.' or M[i-1][j] == '*' ):
            Nodes[i-1][j].set_parent(i,j)
            Nodes[i][j].add_child()
            dfs(Nodes,M,i-1,j,m,n)                
       
    if j - 1 >= 0 :
        if Nodes[i][j-1].get_mark() == 0 and (M[i][j-1] == '.' or M[i][j-1] == '*' ):
            Nodes[i][j-1].set_parent(i,j)
            Nodes[i][j].add_child()
            dfs(Nodes,M,i,j-1,m,n)
            
    if j + 1 < n :
        if Nodes[i][j+1].get_mark() == 0 and ( M[i][j+1] == '.' or M[i][j+1] == '*' ):
            Nodes[i][j + 1].set_parent(i,j)
            Nodes[i][j].add_child()
            dfs(Nodes,M,i,j+1,m,n)
                
                
    if i + 1 < m:
        
        if Nodes[i + 1][j].get_mark() == 0 and ( M[i + 1][j] == '.' or M[i+1][j] == '*' ):
            Nodes[i + 1][j].set_parent(i,j)
            Nodes[i][j].add_child()
            dfs(Nodes,M,i + 1,j,m,n)                
    
        
            
            
            
def find_number_of_waves(Nodes,M,i,j) :
    
    #print i,j ,": ", Nodes[i][j].get_n_children()
    if M[i][j] == '*' :       
        
        parent_i,parent_j = Nodes[i][j].get_parent()
        return find_number_of_waves(Nodes,M,parent_i,parent_j)
        
    elif M[i][j] == 'M' :
        if Nodes[i][j].get_n_children() > 1 :
            return 1
        else :
            return 0
    else :
        parent_i,parent_j = Nodes[i][j].get_parent()
        if Nodes[i][j].get_n_children() > 1 :
            
            return 1 + find_number_of_waves(Nodes,M,parent_i,parent_j)
        
        else :
            return find_number_of_waves(Nodes,M,parent_i,parent_j)
            
            
            
            
            
            
            
line_no = 1        

for line in sys.stdin :
    if line_no == 1 :
        t = int(line)
        line_no = 2
    elif line_no == 2 :
        ls = line.split(' ')
        m = int(ls[0])
        n = int(ls[1]) 
        i = 0
        M = {}
        Nodes = {}
        line_no = line_no + 1
    elif line_no -2 <= m :
        M[i] = {}
        Nodes[i] = {}
        length = len(line)
        if line[length - 1] == '\n' :
            new_line = line[0:length-1]
        else :
            new_line = line
            
        
        j = 0
        while j < n :
            if new_line[j] == '*' :
                dest_i = i
                dest_j = j
            if new_line[j] == 'M' :
                start_i = i
                start_j = j
                
            M[i][j] = new_line[j]
            Nodes[i][j] = Node()
            j  = j + 1
            
        i = i + 1     
        line_no = line_no + 1
        
    else :
        K = int(line)
        dfs(Nodes,M,start_i,start_j,m,n)
        l = find_number_of_waves(Nodes,M,dest_i,dest_j)
        #print l,K
        if l == K :
            print "Impressed"
        else :
            print "Oops!"
        line_no = 2

    

    


