#include <cstdio>
#include <queue>
#define maxn 101
using namespace std;
int m, s, c;
int num;
int nn;
struct node {
    int x, y, step;
};
node foot[maxn][maxn];
node path[maxn];
int state[maxn][maxn];
bool vis[maxn][maxn];
int c_bus[maxn * maxn];
int c_fol[maxn * maxn];
int len;
void print() {
    int a = 0, b = 0;
    for (int i = len - 1; i >= 0; i--) {
        path[i].x = foot[a][b].x;
        path[i].y = foot[a][b].y;
        a = path[i].x;
        b = path[i].y;
    }
    for (int i = 0; i <= len; i++) {
        printf("(%d,%d)", path[i].x, path[i].y);
        if (i != len )
            printf(" -> ");
    }
    printf("\n");
}
int BFS() {
    queue<node> q;
    q.push((node) {
        m, s, 0
    });
    while (!q.empty()) {
        node p = q.front();
        q.pop();
        if (p.x == 0 && p.y == 0)return p.step;
        if (vis[p.x][p.y])continue;
        for (int i = 0; i < nn; i++) {
            node n;
            if (p.step % 2 != 0) {
                n.x = p.x + c_bus[i];
                n.y = p.y + c_fol[i];
            } else {
                n.x = p.x - c_bus[i];
                n.y = p.y - c_fol[i];
            }
            n.step = p.step + 1;
            if ((n.x >= 0) && (n.x <= m) && (n.y >= 0) && (n.y <= s)) {
                if (!vis[n.x][n.y] && state[n.x][n.y] == 1) {
                    q.push(n);
                    foot[n.x][n.y] = (node) {
                        p.x, p.y
                    };
                }
            }
        }
    }
    return 0;
}
void init() {
    num = m;
    nn = (c + 1) * (c + 2) / 2 - 1;
    //in case i,there are c_bus merchants and c_fols servants on thee boat
    for (int i = 0; i < nn; ) {
        for (int j = c; j >= 1; j--) {
            for (int k = j; k >= 0; k--, i++) {
                c_bus[i] = k;
                c_fol[i] = j - k;
            }
        }
    }
    int abs = m - s;
    for (int i = 0; i < num + 1; i++) {
        state[0][i] = 1;
        state[num][i] = 1;
        for (int j = i - abs; j <= i; j++)
            state[i][j] = 1;
    }
}

int main() {
    printf("Input: Number of the Merchant, Servant and Capacity of boat: ");
    scanf("%d %d %d", &m, &s, &c);
    if (m < s) {
        printf("They can't cross the river.\n");
        return 0;
    }
    init();
    len = BFS();
    if (!len)
        printf("They can't cross the river.\n");
    else print();
    return 0;
}