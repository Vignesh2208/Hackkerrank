#include<stdio.h>
#include<stdlib.h>
int * a;
int * s;

int root(int i){
    
    if(a[i] == i)
        return i;
    else
        a[i] = root(a[i]);
        return a[i];
}

void union_add(int i, int j){
    
    int root_i = root(i);
    int root_j = root(j);
    
    int root_i_size = s[root_i];
    int root_j_size = s[root_j];
    
    if(root_i != root_j){
    
        if(root_i_size > root_j_size){
            a[root_j]  = root_i;
            s[root_j] = 0;
            s[root_i] = root_i_size + root_j_size;
        
        }
        else{
            a[root_i]  = root_j;
            s[root_i] = 0;
            s[root_j] = root_i_size + root_j_size;
        
        }
        
    }
    
}

void initialize(int n){
    
    int i;
    for(i = 0; i < n; i++){        
        a[i] = i;
        s[i] = 1;
        
    }  
    
    
}

long long int find_no_of_ways(int n){
    
    int sum[n];
    long long int n_ways = 0;
    
    int i;
    
    for(i = n-1; i>=0; i--){
        if(i == n-1)
            sum[i] = s[i];
        else
            sum[i] = s[i] + sum[i+1];
                
    }
    
    for(i = 0; i < n; i++){
        
        if(i + 1 < n){
            
            n_ways += s[i]*sum[i+1];
        }
                
    }
    
    return n_ways;
}

 
int main()
{
    int n,l;
    
    scanf("%d%d",&n,&l);
    if(n==1)
    {
        printf("0\n");
        return(0);
    }
    int **pairs=(int**)malloc(sizeof(int*)*l);
    a = (int *)malloc(sizeof(int)*n);
    s = (int *)malloc(sizeof(int)*n);
    
    initialize(n);
    
    for(int i=0;i<l;i++){
        pairs[i]=(int*)calloc(2,sizeof(int));
        scanf("%d%d",&pairs[i][0], & pairs[i][1]);   
        union_add(pairs[i][0], pairs[i][1]);
    }
    
    long long int ans=0;
   
    /** Write code to compute answer using n,l,pairs**/
    
    ans = find_no_of_ways(n);   
    
  
    printf("%lld\n",ans);
    free(a);
    free(s);
    
    for(int i=0;i<l;i++){
        free(pairs[i]);
    }
    free(pairs);
    return(0);
}

