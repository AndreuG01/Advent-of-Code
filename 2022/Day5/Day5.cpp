#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<int, int> vii;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair

#define endl '\n'
#define len(s) (int)s.size()
#define print(x) cout<<x<<'\n';
#define REP(i, a, b) for (int i = 0; i <= b; i++)
#define all(a) (a).begin(), (a).end()
#define print_big(x) cout << fixed << setprecision(0) << x << endl;
#define line(x) getline(cin, x)
#define string_lowercase(s) transform(s.begin(), s.end(), s.begin(), ::tolower);
#define char_tolower(c) if ('a' <= c && c <= 'z') c += 32
#define char_toupper(c) if ('a' <= c && c <= 'z') c -= 32

#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

ll mod = 1000000007;



int main() {
    fast;

    string curr;
    // I will not be using a stack since the input comes in reverse order
    vector<vector<char>> stacks_part1(10);
    vector<vector<char>> stacks_part2(10);

    auto re = regex("move ([0-9]+) from ([0-9]+) to ([0-9]+)");
    smatch match;
    int max_vec = 0;
    bool fill_done = false;
    
    while(getline(cin, curr)) {
        regex_match(curr, match, re);
        if (match.str(0) != "") {
            int how, from, to;
            how = stoi(match.str(1));
            from = stoi(match.str(2));
            to = stoi(match.str(3));
            
            for (int i = 0; i < how; i++) {
                // Remove first element from the vector
                char remove1 = stacks_part1[from - 1][0];
                char remove2 = stacks_part2[from - 1][(how - i - 1)];
                
                stacks_part1[from - 1].erase(stacks_part1[from - 1].begin());
                stacks_part2[from - 1].erase(stacks_part2[from - 1].begin() + (how - i - 1));
                
                
                // Insert into the first position
                stacks_part1[to - 1].insert(stacks_part1[to - 1].begin(), remove1);
                stacks_part2[to - 1].insert(stacks_part2[to - 1].begin(), remove2);
            }

        } else {
            int idx = 0;
            for (auto c : curr) {
                idx++;
                if (c == '1') fill_done = true;
                if (!fill_done) {
                    if (c != ' ' && c != '[' && c != ']') {
                        stacks_part1[idx / 4].PB(c);
                        stacks_part2[idx / 4].PB(c);
                    }
                }
            }
        }
    }

    for (int i = 0; i < len(stacks_part1); i++) {
        if (len(stacks_part1[i]) > 0) max_vec++;
    }
    cout << "Part 1 res: ";
    for (int i = 0; i < max_vec; i++) {
        cout << stacks_part1[i][0];
    }
    cout << endl;
    
    cout << "Part 2 res: ";
    for (int i = 0; i < max_vec; i++) {
        cout << stacks_part2[i][0];
    }
    cout << endl;


    return 0;
}