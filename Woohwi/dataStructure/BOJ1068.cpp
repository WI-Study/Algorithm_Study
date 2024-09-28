/*
https://www.acmicpc.net/problem/1068

트리 리프노드 구하기
*/

#include <iostream>
#include <vector>

using namespace std;

void leafSearch(int node);

vector<int> tree[51];
int target;
int leaf = 0;

int main(){
    int root;
    int node_num;
    cin >> node_num;

    for(int i = 0; i < node_num; i++){
        int parent_index;
        cin >> parent_index;

        if(parent_index == -1){
            root = i;
        }
        else{
            tree[parent_index].push_back(i);
        }
    }

    cin >> target;

    leafSearch(root);

    cout << leaf;
}

void leafSearch(int node){
    bool child_check = false; // target이 삭제되고 부모가 리프가 되는경우

    if(node == target){
        return;
    }

    if(tree[node].empty()){
        leaf++;
        return;
    }
    for(int i = 0; i < tree[node].size(); i++){
        int child = tree[node][i];
        if(child != target){
            child_check = true;
            leafSearch(child);
        }
    }

    if(!child_check){
        leaf++;
    }
}