/*
https://www.acmicpc.net/problem/1931
회의실 배정
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    vector<pair<int, int>> time;

    cin >> n;

    for(int i = 0; i < n; i++){ // 끝나는 시간이 중요!
        int start, end;
        cin >> start >> end;
        time.push_back(make_pair(end, start)); 
    }
    // 종료를 기준으로 정렬
    sort(time.begin(), time.end());

    int cnt = 0;
    int finish = 0;

    for(int i = 0; i < n; i++){
        int start = time[i].second;
        int end = time[i].first;

        if(start >= finish){
            cnt++;
            finish = end;
        }
    }


    cout << cnt;
    printf("\n");

}