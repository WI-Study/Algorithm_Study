/*
https://www.acmicpc.net/problem/2609
최소공배수 최대공약수
유클리드 호제법
*/

#include <iostream>

using namespace std;

int gcd(int a, int b);
int lcm(int a, int b, int n);

int main() {
    int n, m;
    cin >> n >> m;

    int maxGongyakNum = gcd(n, m);
    int minGongbaeNum = lcm(n, m, maxGongyakNum);

    cout << maxGongyakNum << endl;
    cout << minGongbaeNum << endl;

    return 0;
}

int gcd(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int lcm(int a, int b, int n) {
    return (a * b) / n;
}

