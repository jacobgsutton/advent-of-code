#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans=0, i = 0, j, tmp, dx, dy;
    char start_heading, heading, next_heading, tmp2;
    pair<int, int> pos, start_pos;
    string line, state;
    vector<string> m;
    unordered_set<string> collisions;

    while(getline(cin, line)) {
        m.push_back(line);
        if((tmp=line.find(tmp2='^')) != string::npos || (tmp=line.find(tmp2='>')) != string::npos || 
            (tmp=line.find(tmp2='<')) != string::npos || (tmp=line.find(tmp2='v')) != string::npos) {
            start_pos.first = tmp;
            start_pos.second = i;
            start_heading = tmp2;
        } 
        ++i;
    }
    //Super slow and fully brute force. May try to think of a faster clever solution later.
    for(i=0; i < m.size(); ++i)
        for(j=0; j < m[0].size(); ++j) {
            if(m[i][j]=='#' || m[i][j]==start_heading) continue;
            m[i][j]='#';
            pos=start_pos;
            heading=start_heading;
            while(true) {
                switch(heading) {
                    case '^': dx=0; dy=-1; next_heading='>'; break;
                    case '>': dx=1; dy=0; next_heading='v';break;
                    case '<': dx=-1; dy=0; next_heading='^';break;
                    case 'v': dx=0; dy=1; next_heading='<';break;
                }
                if(0 > pos.first+dx || pos.first+dx >= m.size() || 0 > pos.second+dy || pos.second+dy >= m.size()) break;
                else if(m[pos.second+dy][pos.first+dx]=='#') {
                    if(collisions.contains(state=to_string(pos.first)+","+to_string(pos.second)+","+heading)) {
                        ++ans;
                        break;
                    }
                    collisions.insert(state);
                    heading=next_heading;
                }
                else {
                    pos.first += dx;
                    pos.second += dy;
                }
            }
            m[i][j]='.';
            collisions.clear();
        }
    cout << ans;
}
