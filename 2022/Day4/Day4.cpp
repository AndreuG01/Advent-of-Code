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

    vector<string> vec_part2;
    
    string s;
    int total_1 = 0;
    int total_2 = 0;
    smatch match;
    auto re = regex("([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)");
    int a1, a2, b1, b2;
    while (cin >> s) {
        regex_match(s, match, re);
        a1 = stoi(match.str(1));
        a2 = stoi(match.str(2));
        b1 = stoi(match.str(3));
        b2 = stoi(match.str(4));
        
        if ((b1 >= a1 && b2 <= a2) || (a1 >= b1 && a2 <= b2)) {
            total_1 += 1;
        }
        if (!(a2 < b1 || a1 > b2)) {
            printf("%d-%d,%d-%d\n", a1, a2, b1, b2);
            total_2 += 1;
        }
    }
    
    printf("Part 1 res: %d\n", total_1);
    printf("Part 2 res: %d\n", total_2);

    return 0;
}