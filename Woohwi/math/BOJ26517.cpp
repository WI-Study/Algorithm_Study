/*
https://www.acmicpc.net/problem/26517
연속인가?
*/

#include <iostream>

using namespace std;

int main(){
    long long k;
    long long a, b, c, d;

    cin >> k;

    cin >> a >> b >> c >> d;

    int x1 = a * k + b;
    int x2 = c * k + d;

    if(x1 == x2){
        cout << "Yes " << x1;
        printf("\n");
    }else{
        cout << "No";
        printf("\n");
    }

}