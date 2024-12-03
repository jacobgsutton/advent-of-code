#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    string s="", line;
    int sum=0;
    regex mul_regex("(mul\\(\\d+,\\d+\\))");
    regex integer_regex("\\d+");
    while(getline(cin, line)) s.append(line);
    auto muls_begin = sregex_iterator(s.begin(), s.end(), mul_regex);
    auto muls_end = sregex_iterator();
    for(sregex_iterator i = muls_begin; i != muls_end; ++i) {
        smatch mul = *i;
        auto numbers_begin = sregex_iterator(mul.str().begin(), mul.str().end(), integer_regex);
        sum += stoi((*numbers_begin).str()) * stoi((*(++numbers_begin)).str());
    }
    cout << sum;
}