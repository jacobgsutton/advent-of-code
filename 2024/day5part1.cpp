#include <bits/stdc++.h>

using namespace std;

int main() {
    string line, page;
    vector<int> update;
    int x,y, mid, sum=0, i;
    bool seen[101], bad_ordering = false; 
    unordered_map<int, vector<int>> rules;
    unordered_set<int> in_update;

    while(getline(cin, line)) {
        if(line.empty()) break;
        x=stoi(line.substr(0, line.find('|')));
        y=stoi(line.substr(line.find('|')+1));
        if(!rules.count(x)) rules[x] = vector<int>();
        rules[x].push_back(y);
    }

    while(getline(cin, line)) {
        fill(begin(seen), end(seen), false);
        char *tok = strtok((char*)line.c_str(), ",");
        while(tok != nullptr) {
            update.push_back(atoi(tok));
            in_update.insert(atoi(tok));
            tok = strtok(nullptr, ",");
        }
        mid = update[update.size()/2];
        for(i=0; i < update.size(); ++i) {
            for(int x : rules[update[i]]) 
                if(in_update.contains(x) && seen[x]) {
                    bad_ordering = true;
                    goto END;
                }
            seen[update[i]] = true;
        }
        END:
        if(!bad_ordering) sum += mid;
        bad_ordering = false;
        update.clear();
        in_update.clear();
    }
    cout << sum;
}

