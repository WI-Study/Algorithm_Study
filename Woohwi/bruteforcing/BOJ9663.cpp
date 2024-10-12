/*
https://www.acmicpc.net/problem/9663
N-Queen
*/

#include <iostream>
#include <cmath>
using namespace std;

int N;              // N개의 퀸을 놓을 체스판 크기
int result = 0;     // 가능한 배치의 수
int queen[15];      // queen[i]는 i번째 행에 놓인 퀸의 열 위치를 저장

// 퀸을 놓을 수 있는지 확인하는 함수
bool isPossible(int row) {
    for (int i = 0; i < row; i++) {
        // 같은 열에 있거나, 대각선에 위치한 경우 공격받음
        if (queen[i] == queen[row] || abs(queen[row] - queen[i]) == row - i) {
            return false;
        }
    }
    return true;
}

// 백트래킹 함수: n번째 행에 퀸을 놓기
void solveNQueen(int row) {
    // 모든 행에 퀸을 다 놓았다면, 가능한 배치이므로 result++
    if (row == N) {
        result++;
        return;
    }

    // 0번 열부터 N-1번 열까지 퀸을 놓을 수 있는지 시도
    for (int i = 0; i < N; i++) {
        queen[row] = i;  // row번째 행의 i번째 열에 퀸을 놓음
        if (isPossible(row)) {
            solveNQueen(row + 1);  // 다음 행으로 넘어감
        }
    }
}

int main() {
    // N 입력
    cin >> N;

    // N-Queen 문제 해결
    solveNQueen(0);

    // 가능한 배치의 수 출력
    cout << result << endl;

    return 0;
}

