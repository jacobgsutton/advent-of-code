#include <bits/stdc++.h>

using namespace std;

int main() {
    string line, page;
    vector<int> update;
    int x,y, sum=0, i;
    bool seen[101], bad_ordering = false; 
    unordered_map<int, unordered_set<int>> rules;
    unordered_set<int> in_update;

    while(getline(cin, line)) {
        if(line.empty()) break;
        x=stoi(line.substr(0, line.find('|')));
        y=stoi(line.substr(line.find('|')+1));
        if(!rules.count(x)) rules[x] = unordered_set<int>();
        rules[x].insert(y);
    }

    while(getline(cin, line)) {
        fill(begin(seen), end(seen), false);
        char *tok = strtok((char*)line.c_str(), ",");
        while(tok != nullptr) {
            update.push_back(atoi(tok));
            in_update.insert(atoi(tok));
            tok = strtok(nullptr, ",");
        }
        for(i=0; i < update.size(); ++i) {
            for(int x : rules[update[i]]) 
                if(in_update.contains(x) && seen[x]) {
                    bad_ordering = true;
                    goto END;
                }
            seen[update[i]] = true;
        }
        END:
        if(bad_ordering) {
            sort(update.begin(), update.end(), [&rules](int &x, int &y) {
                return rules[x].contains(y);
            });
            sum += update[update.size()/2];
        }
        bad_ordering = false;
        update.clear();
        in_update.clear();
    }
    cout << sum;
}

