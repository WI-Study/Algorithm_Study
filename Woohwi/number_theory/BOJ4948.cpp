/*
https://www.acmicpc.net/problem/4948
베르트랑 공준
*/

#include <iostream>
#include <vector>
#define MAX 123456 * 2

using namespace std;

vector<bool> arr(MAX+1, 1);

void cal(){
    arr[0] = arr[1] = false;

    //에라토리뭐시기의 체
    for(int i = 2; i*i <= MAX; i++){
        if(arr[i]){
            for(int j = i*i; j <= MAX; j += i){
                arr[j] = false;
            }
        }
    }
}

int printprime(int n){
    int cnt = 0;

    cal();

    for(int i = n+1; i <= 2 * n; i++){
        if(arr[i]){
            cnt++;
        }
    }

    return cnt;
}

int main(){
    
    while (1)
    {
        int n;
        cin >> n;
        if(n == 0){
            break;
        }

        cout << printprime(n) << endl;
    }
    

    return 0;

}
