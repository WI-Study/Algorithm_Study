/*
https://www.acmicpc.net/problem/10845

큐를 구현해봅자!
*/

#include <iostream>
#define MAX 10001

using namespace std;

typedef struct {
    int key;
} element;

element queue[MAX];
int qFront = -1;
int rear = -1;

void push(element item);
element pop();
int size();
bool empty();
int front();
int back();

int main() {
    int command_num;
    cin >> command_num;

    for (int i = 0; i < command_num; i++) {
        string command;
        cin >> command;

        if (command == "push") {
            int value;
            cin >> value;
            element item;
            item.key = value;
            push(item);
        } else if (command == "pop") {
            if(empty()){
                cout << -1 << endl;
            }else{
                cout << pop().key << endl;
            }
        } else if (command == "size") {
            cout << size() << endl;
        } else if (command == "empty") {
            cout << empty() << endl;
        } else if (command == "front") {
            cout << front() << endl;
        } else if (command == "back") {
            cout << back() << endl;
        }
    }

    return 0;
}

void push(element item) {
    if (rear == MAX - 1) {
        cout << "마이뭇따" << endl;
        return;
    }
    queue[++rear] = item;
}

element pop() {
    return queue[++qFront];
}

int size() {
    if (empty()) {
        return 0;
    }
    return rear - qFront;
}

bool empty() {
    return qFront >= rear;
}

int front() {
    if (empty()) {
        return -1;
    }
    return queue[qFront+1].key; 
}

int back() {
    if (empty()) {
        return -1;
    }
    return queue[rear].key;
}