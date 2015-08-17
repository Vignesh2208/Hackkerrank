# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
M = {}

def assign_val(i,Top_prev,Bottom_prev,Top_curr,Bottom_curr) :
    M[i][1] = 0
    M[i][2] = 0
    M[i][3] = 0
    M[i][4] = 0
    if Top_curr == '1' and Bottom_curr == '1' :
        if Top_prev == '1'  and Bottom_prev == '1' :
            M[i][3] = M[i-1][4]    
            M[i][4] = M[i-1][4]
        elif Top_prev == '1' and Bottom_prev == '0' :
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
        elif Top_prev == '0' and Bottom_prev == '1' : 
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
        else :
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
    elif Top_curr == '1' and Bottom_curr == '0' :
        if Top_prev == '1'  and Bottom_prev == '1' :
            M[i][3] = M[i-1][4]
            if M[i-1][4] == 1 :
                M[i][2] = 1
            else :
                M[i][2] = 0
                       
        elif Top_prev == '1' and Bottom_prev == '0'  :
                        
            if M[i-1][2] == 1 :
                M[i][4] = 1
            M[i][2] = M[i-1][4]
            M[i][3] = M[i-1][4]
            
        elif Top_prev == '0' and Bottom_prev == '1' :
            #if M[i-1][1] == 1 :
            #    M[i][4] = 1
            M[i][2] = M[i-1][4]
            M[i][3] = M[i-1][4]
        else :
            M[i][2] = M[i-1][4]
            M[i][3] = M[i-1][4]
            #if M[i-1][1] == 1 or M[i-1][2] == 1 :
            if M[i-1][2] == 1 :
                M[i][4] = 1
                
    elif Top_curr == '0' and Bottom_curr == '1' :
        if Top_prev == '1'  and Bottom_prev == '1' :
            M[i][3] = M[i-1][4]
            if M[i-1][4] == 1 :
                M[i][1] = 1
            else :
                M[i][1] = 0
                       
        elif Top_prev == '1' and Bottom_prev == '0'  :
                        
            if M[i-1][2] == 1 :
                M[i][4] = 1
            M[i][1] = M[i-1][4]
            M[i][3] = M[i-1][4]
            
        elif Top_prev == '0' and Bottom_prev == '1' :
            if M[i-1][1] == 1 :
                M[i][4] = 1
            M[i][1] = M[i-1][4]
            M[i][3] = M[i-1][4]
        else :
            M[i][1] = M[i-1][4]
            M[i][3] = M[i-1][4]
            if M[i-1][1] == 1 or M[i-1][2] == 1 :
                M[i][4] = 1
    elif Top_curr == '0' and Bottom_curr == '0' :
        if Top_prev == '1'  and Bottom_prev == '1' :
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
                       
        elif Top_prev == '1' and Bottom_prev == '0'  :
                        
            if M[i-1][2] == 1 :
                M[i][2] = 1
                M[i][1] = 1
                       
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
            
        elif Top_prev == '0' and Bottom_prev == '1' :
            if M[i-1][1] == 1 :
                M[i][2] = 1
                #M[i][1] = 1
            
            M[i][3] = M[i-1][4]
            M[i][4] = M[i-1][4]
            
        else :
            
            M[i][4] = M[i-1][4]
            M[i][3] = M[i-1][4]
            
            if M[i-1][2] == 1 :
                M[i][1] = 1
                M[i][2] = 1
            if M[i-1][1] == 1 :
                M[i][2] = 1
            
        

def is_feasible(N,Top_row,Bottom_row) :
    
    i = 0
    while i < N :
        M[i] = {}
        i = i + 1
   
    i = 0
    while i < N :
        if i > 0 :
            Top_prev = Top_row[i-1]
            Bottom_prev = Bottom_row[i-1]
            Top_curr = Top_row[i]
            Bottom_curr = Bottom_row[i]
            assign_val(i,Top_prev,Bottom_prev,Top_curr,Bottom_curr)
        else :
            M[0][1] = 0
            M[0][2] = 0
            M[0][3] = 1
            M[0][4] = 0
            if Top_row[0] == '1' and Bottom_row[0] == '1' :
                M[0][4] = 1
            elif Top_row[0] == '1' and Bottom_row[0] == '0' :
                M[0][2] = 1
            elif Top_row[0] == '0' and Bottom_row[0] == '1' :
                M[0][1] = 1
            else :
                M[0][4] = 1
        i = i + 1

    return M[N-1][4]

line_no = 0
for line in sys.stdin :
    if line_no == 0 :
        line_no = line_no + 1
        continue
    if (line_no -1) % 3 == 0 :
        N = int(line)
        line_no = line_no + 1
    elif (line_no -1) % 3 == 1 :
        Top_row = []
        i = 0
        length = len(line)
        if line[length -1] == '\n' :
            while i < length - 1 :
                Top_row.append(line[i])
                i = i + 1
        else :
            while i <= length - 1 :
                Top_row.append(line[i])
                i = i + 1
        
        line_no = line_no + 1
        
    elif (line_no -1) % 3 == 2 :
        
        Bottom_row = []
        i = 0
        length = len(line)
        if line[length -1] == '\n' :
            while i < length - 1 :
                Bottom_row.append(line[i])
                i = i + 1
        else :
            while i <= length - 1 :
                Bottom_row.append(line[i])
                i = i + 1
        feasibility = is_feasible(N,Top_row,Bottom_row)
        
        if feasibility == 1 :
            print "YES"
        else :
            print "NO"
        line_no = line_no + 1
        
