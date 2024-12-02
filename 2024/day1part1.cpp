#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b,sum;
    vector<int> list1, list2;
    while(cin >> a >> b) {
        if(a == -1 && b == -1) break;
        list1.push_back(a);
        list2.push_back(b);
    }
    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    for(int i = 0; i < list1.size(); ++i) {
        sum += abs(list1[i] - list2[i]);
    }
    cout << sum;
}