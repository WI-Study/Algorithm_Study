/*
https://www.acmicpc.net/problem/14730
미적
謎紛芥索紀 (Small)
*/

#include <iostream>

using namespace std;

int main(){
    int n, coef, order;
    int sum = 0;

    cin >> n;

    for(int i = 0; i < n; i ++){
        cin >> coef >> order;
        sum += coef * order; 
    }

    cout << sum;
    printf("\n");

}