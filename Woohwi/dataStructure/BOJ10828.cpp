/*
https://www.acmicpc.net/problem/10828

스택구현
*/

#include <iostream>
#define MAX 10001

using namespace std;

typedef struct
{
    int key;
}element;

element stack[MAX];
int top = -1;

void push(element item);
element pop();
bool empty();
void stackFull();
void size();


int main(){

    int instruct_num;
    cin >> instruct_num;

    for(int i = 0 ; i < instruct_num; i++){
        element item;
        string command;
        cin >> command;

        if(command == "push"){
            int value;
            cin >> value;
            item.key = value;
            push(item);
        }
        else if(command == "pop"){
            if(empty()){
                cout << -1 << endl;
            }
            else{
                cout << pop().key << endl;
            }

        }
        else if(command == "size"){
            size();
        }
        else if(command == "empty"){
            cout << empty() << endl;
        }
        else if(command == "top"){
            if(empty()){
                cout << -1 << endl;
            }
            else {
                cout << stack[top].key << endl;
            }
        }
    }




    return 0;
}

void push(element item){
    if(top >= MAX-1){
        stackFull();
    }
    stack[++top] = item;
}

element pop(){
    return stack[top--];
}

void size(){
    cout << top+1 << endl;
}

void stackFull(){
    cout << "stack is full!" << endl;
}

bool empty(){
    return top == -1;
}



