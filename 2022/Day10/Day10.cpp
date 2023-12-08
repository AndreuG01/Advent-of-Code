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

void draw(int cycle, int val) {
    int pos_draw = (cycle % 40) + 1;
    if (pos_draw < val + 1 || pos_draw > val + 3) {
        cout << ".";
    } else {
        cout << "#";
    }
    if (pos_draw == 1) {
        cout << endl;
    }
}

int main() {
    fast;
    string s;
    smatch match;
    auto re = regex("addx (-?[0-9]+)");

    int cycles = 0;
    int target_cycles = 20;
    int num_register = 1;
    int total = 0;
    while (getline(cin, s)) {
        regex_match(s, match, re);
        if (match.str(0) != "") {
            int v = stoi(match.str(1));
            cycles += 1;
            draw(cycles, num_register);
            if (cycles == target_cycles) {
                total += cycles * num_register;
                target_cycles += 40;
            }
            cycles += 1;
            draw(cycles, num_register);
            if (cycles == target_cycles) {
                target_cycles += 40;
                total += cycles * num_register;
            }
            num_register += v;
        } else {
            cycles++;
            draw(cycles, num_register);
            if (cycles == target_cycles) {
                target_cycles += 40;
                total += cycles * num_register;
            }
        }
    }
    print(total);
    return 0;
}