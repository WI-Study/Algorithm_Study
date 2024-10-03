#include <iostream>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T, num;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        cin >> num;
        string ans;
        if (num == 1)
            ans = "Pairs for 1:\n";
        else if (num == 2)
            ans = "Pairs for 2:\n";
        else if (num == 3)
            ans = "Pairs for 3: 1 2\n";
        else if (num == 4)
            ans = "Pairs for 4: 1 3\n";
        else if (num == 5)
            ans = "Pairs for 5: 1 4, 2 3\n";
        else if (num == 6)
            ans = "Pairs for 6: 1 5, 2 4\n";
        else if (num == 7)
            ans = "Pairs for 7: 1 6, 2 5, 3 4\n";
        else if (num == 8)
            ans = "Pairs for 8: 1 7, 2 6, 3 5\n";
        else if (num == 9)
            ans = "Pairs for 9: 1 8, 2 7, 3 6, 4 5\n";
        else if (num == 10)
            ans = "Pairs for 10: 1 9, 2 8, 3 7, 4 6\n";
        else if (num == 11)
            ans = "Pairs for 11: 1 10, 2 9, 3 8, 4 7, 5 6\n";
        else if (num == 12)
            ans = "Pairs for 12: 1 11, 2 10, 3 9, 4 8, 5 7\n";
        cout << ans;
    }
}