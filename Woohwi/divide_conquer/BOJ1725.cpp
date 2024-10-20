/*
https://www.acmicpc.net/problem/1725
히스토그램
*/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int maxDimesion(vector<int> &height){
    stack<int> s;
    int maxArea = 0;
    int n = height.size();

    for (int i = 0; i <= n; i++) {
        int newH;
        if (i == n) {
            newH = 0;
        } 
        else {
            newH = height[i];
        }

        while (!s.empty() && height[s.top()] > newH) {
            int h = height[s.top()];
            s.pop();

            int w;
            if (s.empty()) {
                w = i;
            } 
            else {
                w = i - s.top() - 1;
            }
            maxArea = max(maxArea, h * w);
        }
        s.push(i);
    }
    return maxArea;
    

}

int main(){
    int num;
    cin >> num;

    vector<int> height(num);

    for(int i = 0; i < num; i++){
        cin >> height[i];
    }

    int res = maxDimesion(height);

    cout << res << endl;

}