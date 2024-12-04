#include <bits/stdc++.h>

using namespace std;

bool is_match(int i, int j, vector<string> &m, const vector<string> &subimg) {
    int r = m.size(), c = m[0].size(), sub_r = subimg.size(), sub_c = subimg[0].size(), k = i, l, y=0, x;
    for(; y < sub_r; ++k, ++y) {
        if(k >= r) return false;
        for(l=j, x=0; x < sub_c; ++l, ++x) {
            if(l >= c) return false;
            if(subimg[y][x] != '.' && subimg[y][x] != m[k][l]) return false;
        }
    }
    return true;
}

int main() {
    const vector<string> img1 = {"M.S",".A.","M.S"};
    const vector<string> img2 = {"S.M",".A.","S.M"};
    const vector<string> img3 = {"M.M",".A.","S.S"};
    const vector<string> img4 = {"S.S",".A.","M.M"};
    string line;
    int i=0, j, cnt=0, r, c;
    vector<string> m;
    while(getline(cin, line))
        m.push_back(line);
    r=m.size();
    c=m[0].size();
    for(; i < r; ++i) {
        for(j=0; j < c; ++j) {
            if(m[i][j] == 'M' && is_match(i, j, m, img1) || is_match(i, j, m, img3)) ++cnt;
            else if(m[i][j] == 'S' && is_match(i, j, m, img2) || is_match(i, j, m, img4)) ++cnt;
        }
    }
    cout << cnt;
}

