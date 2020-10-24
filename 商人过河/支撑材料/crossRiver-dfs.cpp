#include <cstdio>
#define maxn 101
int m, s, c;
int num;
int nn;
int graph[maxn*maxn][maxn*maxn];
int state[maxn][maxn];

//when cross river
int c_bus[maxn*maxn];
int c_fol[maxn*maxn];
int b_step[maxn*maxn];
int f_step[maxn*maxn];

bool flag = false;
void DFS(int bus, int fol, int step, int dir)
{
    b_step[step] = bus, f_step[step] = fol;
    if(bus == 0 && fol == 0)
    {
        for(int i = 0; i <= step; i++)
        {
            printf("(%d,%d)", b_step[i], f_step[i]);
            if(i != step )
                printf(" -> ");
        }
        printf("\n");
        flag = true;
        return;
    }
    int fa = bus * ( num + 1 ) + fol;
    for(int i = 0; i < nn ; i++)
    {
        if(dir)
        {
            int b_next = bus - c_bus[i], f_next = fol - c_fol[i];
            if(b_next >= 0 && b_next < m+1 && f_next >= 0 && f_next < s + 1 && state[b_next][f_next])
            {
                int son = b_next * ( num + 1 ) + f_next;
                if(!graph[fa][son] && !graph[son][fa])
                {
                    graph[fa][son] = 1;
                    graph[son][fa] = 1;
                    DFS(b_next, f_next, step + 1, !dir);
                    graph[fa][son] = 0;
                    graph[fa][son] = 0;
                }
            }
        }
        else
        {
            int b_next = bus + c_bus[i], f_next = fol + c_fol[i];
            if(b_next >= 0 && b_next < m + 1 && f_next >= 0 && f_next < s + 1 && state[b_next][f_next])
            {
                int son = b_next * ( num + 1) + f_next;
                if(!graph[fa][son] && !graph[son][fa])
                {
                    graph[fa][son] = 1;
                    graph[son][fa] = 1;
                    DFS(b_next, f_next, step + 1, !dir);
                    graph[fa][son] = 0;
                    graph[fa][son] = 0;
                }
            }
        }
    }
}
int main()
{
	printf("Number of the Merchant, Servant and capacity of boat: ");
	scanf("%d %d %d", &m, &s, &c);
	if(m < s)
	{
		printf("they can't cross the river.\n");
		return 0;
	}
	num = m;
	nn = (c+1)*(c+2)/2-1;

	for(int i = 0; i < nn; )
	{
		for(int j = c; j >= 1; j--)
		{
			for(int k = j; k >= 0; k--, i++)
			{
				c_bus[i] = k;
				c_fol[i] = j-k;
			}
		}
	}
	int abs = m-s;
    for(int i = 0; i < num + 1; i++)
    {
        state[i][0] = 1;
        state[i][num] = 1;
        for(int j = i; j <= i+abs; j++)
        state[j][i] = 1;
    }
    DFS(m, s, 0, 1);
    if(!flag)
        printf("they can't cross the river.\n");
}
