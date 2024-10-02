/*
https://www.acmicpc.net/problem/11399
ATM
*/

#include <iostream>
#include <algorithm>

using namespace std;

void schedule(int *time, int n);

int main(){
    int n;
    cin >> n;
    int *time = new int[n];

    for(int i = 0; i < n; i++){
        cin >> time[i];
    }

    sort(time, time+n);

    schedule(time, n);

    delete[] time; 
}

void schedule(int *time, int n){
    int sum = 0;
    int totalsum = 0;
    for(int i = 0; i < n; i++){
       sum += time[i];
       totalsum += sum;
    }

    cout << totalsum << endl;
}