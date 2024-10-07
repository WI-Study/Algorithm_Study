/*
https://www.acmicpc.net/problem/1463
1로 만들기
*/

#include <iostream>
#include <algorithm>
#define MAX 1000001

using namespace std;

int arr[MAX];

int main(){ 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    arr[1] = 0;

    for(int i = 2; i <= n; i++){
        arr[i] = arr[i - 1] + 1;

        if(i % 2 == 0)
        {
            arr[i] = min(arr[i], arr[i / 2] + 1);
        }
        if(i % 3 == 0)
        {
            arr[i] = min(arr[i], arr[i / 3] + 1);
        }
    }

    cout << arr[n] << endl;
}
