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
        printf("%2d %3d\n",i,fre[i]);
    }
    int sum1=0,sum2=fre[0];
    for(i=9;i<=19;i++){
        sum1+=fre[i];
    }
    for(i=20;i<=23;i++){
        sum2+=fre[i];
    }
    printf("%d %d\n",sum1/11,sum2/5);
}