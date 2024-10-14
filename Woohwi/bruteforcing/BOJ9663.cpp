/*
https://www.acmicpc.net/problem/9663
n-queens
*/

#include <iostream>
#include <cmath>
using namespace std;

int n;
int sum = 0;
int col[15];


bool promising(int row) {
    for (int i = 0; i < row; i++) {
        if (col[i] == col[row] || abs(col[row] - col[i]) == row - i) {
            return false;
        }
    }
    return true;
}

void cal(int row) {
    if (row == n) {
        sum++;
        return;
    }

    for (int i = 0; i < n; i++) {
        col[row] = i;
        if (promising(row)) {
            cal(row + 1);
        }
    }
}

int main() {
    cin >> n;


    cal(0);

    cout << sum << endl;

    return 0;
}

