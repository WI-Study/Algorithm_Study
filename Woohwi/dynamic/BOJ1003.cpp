#include <iostream>
#define MAX 41

using namespace std;

int memo0[MAX] = {1, 0};  // 0 호출 횟수
int memo1[MAX] = {0, 1};  // 1 호출 횟수

void fibonacci(int n) {
    for (int i = 2; i <= n; i++) {
        if (memo0[i] == 0 && memo1[i] == 0) {  // 중복계산 피하기
            memo0[i] = memo0[i-1] + memo0[i-2];
            memo1[i] = memo1[i-1] + memo1[i-2];
        }
    }

    cout << memo0[n] << " " << memo1[n] << endl;
}

int main() {
    int num;
    cin >> num;
    
    for (int i = 0; i < num; i++) {
        int n;
        cin >> n;
        fibonacci(n);
    }

    return 0;
}
