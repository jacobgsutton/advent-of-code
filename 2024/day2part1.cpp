#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    string line;
    stringstream ss;
    bool safe = true, inc = false;
    int safe_cnt = 0, prev=-1, curr=-1, diff=-1, i;
    while(getline(cin, line)) {
        ss.str(line);
        i = 0;
        while(ss >> curr) {
            diff=curr-prev;
            if(i==1) inc = diff > 0 ? true : false;
            if(prev != -1 && (!abs(diff) || abs(diff) > 3 || (diff < 0 && inc) || (diff > 0 && !inc))) {
                safe=false;
                break;
            }
            prev=curr;
            ++i;
        }
        if(safe) ++safe_cnt;
        safe=true;
        prev=-1;
        ss.clear();
    }
    cout << safe_cnt;
}