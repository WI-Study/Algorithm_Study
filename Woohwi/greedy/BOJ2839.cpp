/*
    https://www.acmicpc.net/problem/2839

    설탕배달
*/

#include <iostream>

using namespace std;

int main(){
    int n;
    int cnt = 0;

    cin >> n;

    while (n >= 0)
    {
        if(n % 5 == 0){
            cnt += n/5;
            cout << cnt << endl;
            return 0;
        }
        n -= 3;
        cnt ++;
    }
    
    cout << -1 << endl;
}