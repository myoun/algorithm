#include <iostream>
#include <vector>
#include <queue>

#define MAX 701
#define INF 1000000

using namespace std;

int n, result;
int c[MAX][MAX], f[MAX][MAX], d[MAX];
vector<int> a[MAX];

void maxFlow(int start, int end) {
    while (1) {
        fill(d, d + MAX, -1);
        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int x = q.front();
            q.pop();
            for (int i = 0; i < a[x].size(); ++i) {
                int y = a[x][i];

                if (c[x][y] - f[x][y] > 0 && d[y] == -1) {
                    q.push(y);
                    d[y] = x;
                    if (y == end) break;
                }
            }
        }
        if (d[end] == -1) break;
        int flow = INF;
        for (int i = end; i != start; i = d[i]) {
            flow = min(flow, c[d[i]][i] - f[d[i]][i]);
        }
        for (int i = end; i != start; i = d[i]) {
            f[d[i]][i] += flow;
            f[i][d[i]] -= flow;
        }
        result += flow;
    }
}

int main() {
    cin >> n;

    for (int i = 0; i < n; ++i) {
        char x, y;
        int z;
        cin >> x >> y >> z;
        a[x].push_back(y);
        a[y].push_back(x);
        c[x][y] += z;
        c[y][x] += z;
    }

    maxFlow('A', 'Z');

    cout << result << endl;
}