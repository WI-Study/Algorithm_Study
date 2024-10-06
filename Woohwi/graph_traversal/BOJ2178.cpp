/*
https://www.acmicpc.net/problem/2178
미로 탐색
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef vector<vector<int>> matrix;

int RL[] = { -1, 1, 0, 0 };
int TD[] = { 0, 0, -1, 1 };

void bfs(matrix &maze, int a, int b);

int main() {
    int n, m;
    cin >> n >> m;

    matrix maze(n, vector<int>(m)); 

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &maze[i][j]);
        }
    }

    bfs(maze, 0, 0);

    cout << maze[n-1][m-1] << endl;
}

void bfs(matrix &maze, int a, int b) {
    int n = maze.size();
    int m = maze[0].size();

    queue<pair<int, int>> q;
    q.push({a, b});

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int move_x = x + RL[i];
            int move_y = y + TD[i];

            if (move_x >= 0 && move_y >= 0 && move_x < n && move_y < m && maze[move_x][move_y] == 1) {
                maze[move_x][move_y] = maze[x][y] + 1;
                q.push({move_x, move_y});
            }
        }
    }
}
