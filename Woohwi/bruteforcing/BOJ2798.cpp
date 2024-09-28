/*
https://www.acmicpc.net/problem/2798

블랙잭
*/

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n,m;
    cin >> n >> m;

    vector<int> card(n);
    for(int i = 0; i < n; i++){
        cin >> card[i];
    }

    int maxHap = 0;

    for(int i = 0; i < n-2; i++){
        for(int j = i+1; j < n-1; j++){
            for(int k = j+1; k < n; k++){
                int cardHap = card[i] + card[j] + card[k];
                if(cardHap <= m && cardHap > maxHap){
                    maxHap = cardHap;
                }
            }
        }
    }

    cout << maxHap << endl;
}