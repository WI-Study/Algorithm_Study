/*
https://www.acmicpc.net/problem/1929

소수 구하기
에라토스테네스 쓰깅
*/

#include <iostream>
#include <vector>

using namespace std;

void eratos(int n, int m);

int main(){
    int n, m;
    cin >> n >> m;

    eratos(n, m);
   
    return 0;
}

void eratos(int n, int m){
    vector<int> arr(m+1, true);
    arr[0] = arr[1] = false;

    for(int i = 2; i * i < m; i++){
        for (int j = i * i; j <= m; j += i) {
                arr[j] = false;
        }
    }

    for(int i = n; i <=m; i++){
        if(arr[i] == true){
            cout << i << endl;
        }
    }

}