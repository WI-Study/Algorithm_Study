/*
https://www.acmicpc.net/problem/12865

평범한 배낭
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> weight(n);
    vector<int> value(n);
    
    for (int i = 0; i < n; i++) {
        cin >> weight[i] >> value[i];
    }

    vector<vector<int>> maxProfit(n + 1, vector<int>(k + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            if (j >= weight[i - 1]) {
                maxProfit[i][j] = max(maxProfit[i - 1][j], maxProfit[i - 1][j - weight[i - 1]] + value[i - 1]);
            } else {
                maxProfit[i][j] = maxProfit[i - 1][j];
            }
        }
    }

    cout << maxProfit[n][k] << endl;

    return 0;
}
