#include <bits/stdc++.h>

using namespace std;

int main() {
    const string xmas = "XMAS";
    const string samx = "SAMX";
    string line;
    int i=0, j, cnt=0, r, c;
    vector<string> rows;
    while(getline(cin, line))
        rows.push_back(line);
    r=rows.size();
    c=rows[0].size();
    for(; i < r; ++i) {
        for(j=0; j < c; ++j) {
            if(rows[i][j] == 'X') {
                if(j<=c-4 && rows[i].substr(j,4) == xmas) ++cnt;
                if(j>=3 && rows[i].substr(j-3,4) == samx) ++cnt;
                if(i<=r-4 && rows[i+1][j]=='M' && rows[i+2][j]=='A' && rows[i+3][j]=='S') ++cnt;
                if(i>=3 && rows[i-1][j]=='M' && rows[i-2][j]=='A' && rows[i-3][j]=='S') ++cnt;
                if(j<=c-4 && i>=3 && rows[i-1][j+1]=='M' && rows[i-2][j+2]=='A' && rows[i-3][j+3]=='S') ++cnt;
                if(j<=c-4 && i<=r-4 && rows[i+1][j+1]=='M' && rows[i+2][j+2]=='A' && rows[i+3][j+3]=='S') ++cnt;
                if(j>=3 && i>=3 && rows[i-1][j-1]=='M' && rows[i-2][j-2]=='A' && rows[i-3][j-3]=='S') ++cnt;
                if(j>=3 && i<=r-4 && rows[i+1][j-1]=='M' && rows[i+2][j-2]=='A' && rows[i+3][j-3]=='S') ++cnt;
            }
        }
    }
    cout << cnt;
}

