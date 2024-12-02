#include <bits/stdc++.h>

#define is_bad_diff(diff) (!abs(diff) || abs(diff) > 3 || (diff < 0 && assume_inc) || (diff > 0 && !assume_inc))

using namespace std;

bool is_safe(vector<int> &v, bool assume_inc) {
    bool safe = true, flag = false;
    for(int i = 0; i < v.size(); ++i) {
        if(i > 0 && is_bad_diff(v[i]-v[i-1])) {
            if(flag || (i+1 < v.size() && is_bad_diff(v[i+1]-v[i-1]) && i-2 > -1 && is_bad_diff(v[i]-v[i-2]))) {
                safe = false;
                break;
            }
            if(i+1 < v.size() && !is_bad_diff(v[i+1]-v[i-1])) ++i;
            flag = true;
        }
    }
    return safe;
}

int main() {
    ios_base::sync_with_stdio(false);
    string line;
    stringstream ss;
    vector<int> v;
    int safe_cnt = 0, curr;
    while(getline(cin, line)) {
        ss.str(line);
        while(ss >> curr) v.push_back(curr);
        if(is_safe(v, true) || is_safe(v, false)) ++safe_cnt;
        v.clear();
        ss.clear();
    }
    cout << safe_cnt;
}