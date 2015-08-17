#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_L(int S, char * str1, char * str2){
    int n,i,j;
    char * s = str1;                        
    //int ** Len;
    //int ** M; 
    int max_val,p,q,new_len;
    n = 0;                            
    for(i = 0 ; *(s + i) != '\0'; i++)
        n++;
    int Mi[n];
    int Mi1[n];
    
    int Leni[n];
    int Leni1[n];
    int k;

                                  
    max_val = -1;
    for(i = n-1; i >= 0 ; i--){
        
        if(i+1 <= n-1){
           
           for(k = 0; k < n; k++){
               
               Mi1[k] = Mi[k];
               Leni1[k] = Leni[k];
           }  
           
        }
        
        for(j=n-1; j >= 0; j--){
            
            if(i == n-1 || j == n-1){
                if (*(str1 + i) == *(str2 + j)){
                    Mi[j]  = 1;
                    Leni[j] = 0;
                }    
                else{
                    if(S > 0 ){
                        Mi[j] = 1;
                        Leni[j] = 1;
                    }    
                    else{
                        Leni[j] = 1;
                        Mi[j] = 0;
                    }
                }
                
            }            
            else{
                
                if (*(str1 + i) == *(str2 + j)){
                    Mi[j] = Mi1[j+1] + 1;
                    Leni[j] = Leni1[j+1];
                }    
                else{
                    if(Leni1[j+1] == S ){
                        Leni[j] = S;
                        p = i + 1 + Mi1[j+1] -1;
                        q = j + 1 + Mi1[j+1] -1;
                        
                        new_len = Mi1[j+1];
                        
                        
                        while(*(str1 + p) == *(str2 + q)){
                            p = p - 1;
                            q = q - 1;
                            new_len = new_len - 1;
                        }
                        Mi[j] = new_len;
                    }
                    else{ 
                        if(Leni1[j+1] < S ){
                            Leni[j] = Leni1[j+1] + 1;
                            Mi[j] = Mi1[j+1] + 1;
                        }
                        else{
                            Leni[j] = Leni1[j+1];
                            Mi[j] = Mi1[j+1];
                        }
                    }
                }
            }
            if(max_val < Mi[j])
                max_val = Mi[j];
        }
        
        
    }    
    
    
    
    return max_val;                            
}                        

                    

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char *buffer = NULL;
    int read,L;
    unsigned int len;
    int T,i,j;
    char * pch;
    char * str1;
    char * str2;
    
    int curr_val = 0,S;
    read = getline(&buffer, &len, stdin);
    T = atoi(buffer);
    free(buffer);
    
    
    for(i = 0; i < T; i++){
        buffer = NULL;
        read = getline(&buffer, &len, stdin);
        
        curr_val = 0;
        pch = strtok (buffer," ");
        str1 = NULL;
        str2 = NULL;
        while (pch != NULL)
        {
            
            if(curr_val == 0){
                S = atoi(pch);
                            
            }
            if(curr_val == 1){
                str1 = pch;               
            }
            if(curr_val == 2){
                str2 = pch;  
                
                for(j = 0; *(str2+j) != '\0'; j++){
                    ;
                }
                
                if(*(str2 + j-1) == '\n')
                    *(str2 + j-1) = '\0';
            }
            pch = strtok (NULL, " ");
            curr_val++;
            
        }
        
        
        L = find_L(S,str1,str2);        
        printf("%d\n",L);
        
        
    }
    return 0;
    
}

