/*
https://www.acmicpc.net/problem/10830

행렬제곱

*/

#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<int>> matrix;

matrix powerMatrix(matrix a, long long b);
matrix multiply(matrix a, matrix b);

int main(){
    int n;
    long long b;

    cin >> n >> b;

    matrix a(n, vector<int>(n));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
        }
    }

    matrix jegop = powerMatrix(a, b);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << jegop[i][j] << " ";
        }
        printf("\n");
    }
}

matrix powerMatrix(matrix a, long long b){
    int size = a.size();
    matrix result(size, vector<int>(size,0));

    for(int i = 0; i < size; i++){
        result[i][i] = 1;
    }

    while (b>0)
    {
        if(b%2==1){
            result = multiply(result, a);
        }
        a = multiply(a, a);
        b /= 2;
    }
    
    return result;
}

matrix multiply(matrix a, matrix b){
    int n = a.size();
    matrix c(n, vector<int>(n, 0));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            for(int k = 0; k < n; k++){
                c[i][j] += a[i][k] * b[k][j];
            }
            c[i][j] %= 1000;
        }
    }

    return c;
}