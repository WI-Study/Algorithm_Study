/*
https://www.acmicpc.net/problem/11047
동전 0
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void cal(int n, int target, vector<int> arr);

int main(){
    int n, target;
    cin >> n >> target;

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cal(n, target, arr);

}

void cal(int n, int target, vector<int> arr){
    int sum = 0;

    for(int i = n -1; i >= 0; i--){
        if(arr[i] <= target){
            sum += target / arr[i];
            target %= arr[i];
        }
    }

    cout << sum;
    printf("\n");
}
