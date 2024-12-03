#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    string s="", line;
    int sum=0;
    regex commands_regex(R"((mul\(\d+,\d+\))|(don't\(\))|(do\(\)))");
    regex integer_regex(R"(\d+)");
    bool eval_muls = true;
    while(getline(cin, line)) s.append(line);
    auto commands_begin = sregex_iterator(s.begin(), s.end(), commands_regex);
    auto commands_end = sregex_iterator();
    for(sregex_iterator i = commands_begin; i != commands_end; ++i) {
        smatch command = *i, match;
        if(eval_muls && command.str().find("mul")!=string::npos) {
            auto numbers_begin = sregex_iterator(command.str().begin(), command.str().end(), integer_regex);
            sum += stoi((*numbers_begin).str()) * stoi((*(++numbers_begin)).str());
        }
        else if(command.str().find("don't")!=string::npos) eval_muls=false;
        else if(command.str().find("do")!=string::npos) eval_muls=true;
    }
    cout << sum;
}