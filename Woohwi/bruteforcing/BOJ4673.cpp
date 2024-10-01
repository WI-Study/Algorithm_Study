/*
https://www.acmicpc.net/problem/4673

셀프넘버
*/

#include <iostream>
#define MAX 10001

using namespace std;

int checkSelf(int n);

int main(){
    bool arr[MAX] = {false};

    for(int i = 1; i < MAX; i++){
        int n = checkSelf(i);

        if(n < 10001){
            arr[n] = true;
        }
    }

    for(int i = 1; i < MAX; i++){
        if(!arr[i]){
            cout << i << endl;
        }
    }

    return 0;
}

int checkSelf(int n){

    int num = n;
    while (n != 0)
    {
        num = num + (n % 10);
        n /= 10;
    }

    return num;
    
}