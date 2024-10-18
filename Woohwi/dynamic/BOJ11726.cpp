/*
https://www.acmicpc.net/problem/11726
2*N 타일링
*/


#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    int table[n];

    table[1] = 1;
    table[2] = 2;

    for(int i = 3; i <= n; i++){
        table[i] = (table[i-1]+table[i-2]) % 10007;
    }

    cout << table[n] << endl;


}