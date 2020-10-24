#include<stdio.h>
typedef struct node{
    int h,min;
}node;
node flight[2005];
int fre[25];
int main(){
    FILE *in;
    int i=0;
    in=fopen("time.txt","r");
    while(fscanf(in,"%d:%d",&flight[i].h,&flight[i].min)!=EOF){
        i++;
    }
    int num=i;
    for(i=0;i<num;i++){
        fre[flight[i].h]++;
    }
    for(i=0;i<24;i++){
        printf("at %2d, %3d planes arrived\n",i,fre[i]);
    }
    return 0;
}