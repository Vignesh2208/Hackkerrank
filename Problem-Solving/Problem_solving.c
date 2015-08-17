#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int root(int * a, int i, int N){
    if(a[i] == i)
        return i;
    else{
        a[i] = root(a,a[i],N);
        return a[i];
    }
}

void union_add(int * a, int * s, int i, int j, int N, int * n_trees){
    
    int root_i;
    int root_j;
    int t_i_size;
    int t_j_size;
    
    if( i != j){
        
        //printf("Union %d %d\n",i,j);
        
        root_i = root(a,i,N);
        root_j = root(a,j,N);
        t_i_size = s[root_i];
        t_j_size = s[root_j];
        
        if(root_i != root_j){
            
            if(t_i_size < t_j_size){
                a[i] = root_j;
                s[root_j] = t_i_size + t_j_size;
                s[root_i] = 0;
            }
            else{
                a[j] = root_i;
                s[root_i] = t_i_size + t_j_size;
                s[root_j] = 0;
            }
            
            *n_trees = *n_trees - 1;
        }
        
    }
}


// returns 1 if path exists between s and d. Path is filled in the next array.
// returns 0 otherwise
int find_next_path(int **res, int *next, int * visited, int s, int d, int N){
    
    // N is actually 2*N + 2 i.e the number of nodes    
    
    
    int i = 0;
    int path_exists = 0;
    int start;
    int end;
   
    
    visited[s] = 1;   
    
    if(s == d){
        next[s] = d;
        res[s][d] = 0;
        return 1;
    }
    
    if(res[s][d] == 1){
       
        res[s][d] = 0;
        res[d][s] = 1;
        next[s] = d;
        visited[d] = 1;
        return 1;
    }
        
    
    for(i = 0; i < N-2; i++){        
        if(i != s && res[s][i] == 1){
           
            if(visited[i] == 0){
           
                res[s][i] = 0;
                res[i][s] = 1;
                
                if(find_next_path(res,next,visited,i,d,N)){
                    next[s] = i;    
                    path_exists = 1;
                    break;
                }
                else{                    
                    res[s][i] = 1;
                    res[i][s] = 0;
                }
            }
        }        
    }
    
    
    if(path_exists)
        return 1;
    else
        return 0;
    
    
    
    
}

// returns the minimum number of required days.
int bipartite_matching_algo(int **graph, int N, int K){
    
    
    
    int i,j,k;
    int s = 2*N;
    int d = 2*N + 1;
    int edge_found;
    int **res;
    
    res = (int *) malloc(sizeof(int *) * (2*N + 2));    
    for(i = 0 ; i < 2*N + 2; i++){
        res[i] = (int *) malloc(sizeof(int) * (2*N + 2));
        for(j = 0; j < 2*N + 2; j++)
            res[i][j] = 0;
    }
    
    for(i = 0; i < N; i++){
        
        for(j = 0; j < N; j++){
            if(graph[i][j] == 1){
                res[s][2*i] = 1;
                res[2*j + 1][d] = 1;
                res[2*i][2*j+1] = 1;
            }
        }
        
                
    }
    
    for(i = 0; i < N; i++){
        if(res[s][2*i] == 0 && res[2*i + 1][d] == 0){
            res[s][2*i] = 1;
            res[2*i + 1][d] = 1;
            res[2*i][2*i + 1] = 1;
        }
    }
    
        
    int next[2*N + 2];
    int flow_next[N];
    int size[N];
    int n_distinct_path_covers = N;
    int visited[2*N + 2];
    
    for(i = 0; i < N ; i++){
        flow_next[i] = i;
        size[i] = 1;
    }
    
    
    // find max flow in res graph.
    
    while(1){
        
        
        //memset(visited,0,2*N + 2);
        //memset(next,0,2*N + 2);
        for(k = 0; k < 2*N + 2; k++){
            visited[k] = 0;
            next[k] = 0;
        }
        if(find_next_path(res,next,visited,s,d,2*N + 2) == 0){ 
         
          break;        
        }
        
        
        int n1 = next[s];
        int n2 = next[n1];   
        if(n1%2 != 0 || n2%2 != 1 ){
            printf("ERROR: n1  = %d, n2 = %d", n1, n2);
            return n_distinct_path_covers;
        }
        else{
           
            union_add(flow_next,size,n1/2,(n2-1)/2,N,&n_distinct_path_covers);
        }
        
    }
    
    free(res);
    return n_distinct_path_covers;
    
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    int N, K;
    int i,j,k;
    
    scanf("%d",&T);
    for(i = 0; i < T; i++){
        scanf("%d %d",&N,&K);
        int * vi_list = (int *) malloc(sizeof(int)*N);
               
        int ** graph;
        int n_nodes = 0;
        int curr_node;
        for(j = 0; j < N; j++){
        
            scanf("%d",&curr_node);
            vi_list[n_nodes++] = curr_node;
        
            
        }
        //printf("n_nodes = %d\n",n_nodes);
        graph = (int *) malloc(sizeof(int*) * n_nodes);    
        for(j = 0 ; j < n_nodes; j++)
            graph[j] = (int *) malloc(sizeof(int) * n_nodes);
        
        for(j = 0; j < n_nodes; j++){
            for(k = 0; k < n_nodes; k++){
                if(abs(vi_list[j] - vi_list[k]) >= K && k > j){
                   
                    graph[j][k] = 1;
                   
                }
                else{
                   
                    graph[j][k] = 0;
                }
            }
        }
        
        int n_days = bipartite_matching_algo(graph,n_nodes,K);
        free(vi_list);
        free(graph);
        printf("%d\n", n_days);
            
    }
    
    return 0;
}

