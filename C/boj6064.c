#include<stdio.h>

int main(void){
    int M, N;
    int x, y;
    int cycle;
    int sw;
    scanf("%d", &cycle);
    
    for(int i = 0; i < cycle; i++){
        sw = -1;
        scanf("%d %d %d %d", &M, &N, &x, &y);
        long long limit = M * N;
        x--;
        y--;
        for(int j = x; j < limit; j += M){
            if( j % N == y ){
                sw = j + 1;
                break;
            }
        }
        printf("%d\n", sw);
    }
    return 0;
}