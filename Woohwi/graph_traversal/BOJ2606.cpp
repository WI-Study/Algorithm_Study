/*
https://www.acmicpc.net/problem/2606

바이러스
*/

#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;


void dfs(int currentNode);

int main(){
    int n, m;
    int cnt = 0;
    cin >> n >> m;

    graph.resize(n+1);
    visited.resize(n+1);

    for(int i = 0; i < m; i++){
        int x, y;
        cin >> x >> y;

        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    dfs(1);

    for(int i = 2; i <= n; i++){
        if(visited[i]){
            cnt++;
        }
    }

    cout << cnt << "\n";

    return 0;

}

void dfs(int currentNode){
    visited[currentNode] = 1;
    for(int i = 0; i < graph[currentNode].size(); i++){
        
        int nextNode = graph[currentNode][i];
        if(!visited[nextNode]){
            dfs(nextNode);
        }
    }
}