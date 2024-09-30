/*
https://www.acmicpc.net/problemset?sort=ac_desc&algo=95

소수찾기
*/

#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n);

int main(){
    int n;
    int cnt = 0;

    cin >> n;

    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        if(isPrime(num)){
            cnt++;
        }
    }

    cout << cnt << endl;
}

bool isPrime(int n){
    if(n<2){
        return false;
    }

    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            return false;
        }
    }

    return true;
}