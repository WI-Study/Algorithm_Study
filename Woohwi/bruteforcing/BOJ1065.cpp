/*
https://www.acmicpc.net/problem/1065
한수
*/

#include <iostream>

using namespace std;

int hansu(int n);

int main(){
    int num, res;
    cin >> num;

    res = hansu(num);

    cout << res << endl; 
}

int hansu(int n){
    int cnt = 0;

    if(n<100){
        return n;
    }
    else{
        cnt = 99;
        for(int i = 100; i <= n; i++){
            int a = i/100;
            int b = (i%100)/10;
            int c = i%10;

            if((a-b)==(b-c)){
                cnt++;
            }

        }
    }

    return cnt;

}