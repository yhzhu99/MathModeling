#include <cstdio>
#include <iostream>
using namespace std;
#define maxn 101
int NumOfMerchant, NumOfServent, CapacityOfBoat, NumOfTrans, NumOfStep;
int graph[maxn * maxn][maxn * maxn], state[maxn][maxn];
int Change_Merchant[maxn * maxn], Change_Servent[maxn * maxn];
int b_step[maxn * maxn], f_step[maxn * maxn];
bool flag = false;      // 表示是否有可行解
void print() {
    for (int i = 0; i <= NumOfStep; i++) {
        printf("(%d,%d)", b_step[i], f_step[i]);
        if (i != NumOfStep)
            printf(" -> ");
    }
    printf("\n");
    flag = true;
}
void DFS(int bus, int fol, int step, int dir) {
    b_step[step] = bus, f_step[step] = fol;
    if (bus == 0 && fol == 0) { // 如果达到的目标状态，则输出转移的过程
        NumOfStep = step;
        print();
        return;
    }
    int fa = bus * (NumOfMerchant + 1) + fol;
    for (int i = 0; i < NumOfTrans; i++) {
        int b_next = bus + dir * Change_Merchant[i], f_next = fol + dir * Change_Servent[i];
        if (b_next >= 0 && b_next <= NumOfMerchant
                && f_next >= 0 && f_next < NumOfServent + 1 && state[b_next][f_next]) {
            int son = b_next * ( NumOfMerchant + 1 ) + f_next;
            if (!graph[fa][son] && !graph[son][fa]) {
                graph[fa][son] = 1;
                graph[son][fa] = 1;
                DFS(b_next, f_next, step + 1, -dir);
                graph[fa][son] = 0;
                graph[son][fa] = 0;
            }
        }
    }
}
int main() {
    printf("Input: Number of the Merchant, Servant and Capacity of boat: ");
    scanf("%d %d %d", &NumOfMerchant, &NumOfServent, &CapacityOfBoat);//输入初始数据
    if (NumOfMerchant < NumOfServent) { // 题目设定为商人数大于等于随从数
        printf("They can't cross the river.\n");
        return 0;
    }
    NumOfTrans = (CapacityOfBoat + 1) * (CapacityOfBoat + 2) / 2 - 1; // 转移律向量的个数
    for (int i = 0; i < NumOfTrans; i++) {
        for (int j = CapacityOfBoat; j >= 1; j--) {
            for (int k = j; k >= 0; k--, i++) {
                Change_Merchant[i] = k;
                Change_Servent[i] = j - k;
            }
        }
    }
    int abs = NumOfMerchant - NumOfServent;  // 表示商人比随从多出来的数量
    for (int i = 0; i <= NumOfMerchant; i++) { // 构造状态空间
        state[i][0] = 1;
        state[i][NumOfMerchant] = 1;    // state数组记录可行的状态空间
        for (int j = i; j <= i + abs; j++)
            state[j][i] = 1;
    }
    DFS(NumOfMerchant, NumOfServent, 0, -1);
    // 参数1表示商人的数量，参数2表示随从的数量，参数3表示进行的步数，参数4表示船行进的方向
    if (!flag) // 如果没有找到可行解
        printf("They can't cross the river.\n");
}