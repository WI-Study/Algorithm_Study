/* 
그래프 DFS, BFS
https://www.acmicpc.net/problem/1260

DFS는 스택, BFS는 큐를 이용해 구현보자
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

vector<int> graph[1001];
bool visited[1001];

void BFS(int start);
void DFS(int start);

int main(){
    int vertex_num, edge_num, start_vertex; // 정점 갯수, 간선 갯수, 시작 정점

    cin >> vertex_num >> edge_num >> start_vertex;

    //인접리스트 그래프
    for(int i = 0; i < edge_num; i++){
        int v1, v2;
        cin >> v1 >> v2;

        graph[v1].push_back(v2);
        graph[v2].push_back(v1);// 양방향
    }

    for(int i = 1; i <= vertex_num; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

     for (int i = 0; i <= vertex_num; i++) { // 방문체크 초기화
        visited[i] = false;
    }
    DFS(start_vertex);

    cout << endl;

    for (int i = 0; i <= vertex_num; i++) { 
        visited[i] = false;
    }
    BFS(start_vertex);

    return 0;
}

void DFS(int start){
    stack<int> s;
    s.push(start);
    visited[start] = true;
    cout << start << " ";

    while(!s.empty()){
        int vertex = s.top();
        s.pop();

        for(int i = 0; i < graph[vertex].size(); i++){ 
            int next = graph[vertex][i];
            if(!visited[next]){
                visited[next] = true;
                cout << next << " ";
                s.push(vertex); 
                s.push(next); 
                break;
            }
        }
    }
}

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    cout << start << " ";

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int i = 0; i < graph[v].size(); i++) {
            int next = graph[v][i];
            if (!visited[next]) {
                q.push(next);
                visited[next] = true;
                cout << next << " ";
            }
        }
    }

}
