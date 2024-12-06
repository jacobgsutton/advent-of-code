#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans=1, i = 0, tmp, dx, dy;
    char heading, next_heading, tmp2;
    pair<int, int> pos;
    string line;
    vector<string> m;

    while(getline(cin, line)) {
        m.push_back(line);
        if((tmp=line.find(tmp2='^')) != string::npos || (tmp=line.find(tmp2='>')) != string::npos || 
            (tmp=line.find(tmp2='<')) != string::npos || (tmp=line.find(tmp2='v')) != string::npos) {
            pos.first = tmp;
            pos.second = i;
            heading = tmp2;
        } 
        ++i;
    }
    while(true) {
        switch(heading) {
            case '^': dx=0; dy=-1; next_heading='>'; break;
            case '>': dx=1; dy=0; next_heading='v';break;
            case '<': dx=-1; dy=0; next_heading='^';break;
            case 'v': dx=0; dy=1; next_heading='<';break;
        }
        if(0 > pos.first+dx || pos.first+dx >= m.size() || 0 > pos.second+dy || pos.second+dy >= m.size()) break;
        else if(m[pos.second+dy][pos.first+dx]=='#') heading=next_heading;
        else {
            m[pos.second][pos.first]='X';
            pos.first += dx;
            pos.second += dy;
            if(m[pos.second][pos.first]!='X') ++ans;
        }
    }
    cout << ans;
}
