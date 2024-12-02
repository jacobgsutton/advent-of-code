#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b,sum;
    map<int, int> map;
    vector<int> list1;
    while(cin >> a >> b) {
        if(a == -1 && b == -1) break;
        if(!map.count(b)) map[b] = 0;
        ++map[b];
        list1.push_back(a);
    }
    for(int &x : list1)
        if(map.count(x))
            sum += x * map[x];
    cout << sum;
}