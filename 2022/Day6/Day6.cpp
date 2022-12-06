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

    string s;

    while (cin >> s) {
        for (int i = 0; i < len(s) - 4; i++) {
            char c1 = s[i];
            char c2 = s[i + 1];
            char c3 = s[i + 2];
            char c4 = s[i + 3];
            if (!(c1 == c2 || c1 == c3 || c1 == c4 || c2 == c3 || c2 == c4 || c3 == c4)) {
                printf("Part 1 res: %d\n", i + 4);
                break;
            }
        }
        for (int i = 0; i < len(s) - 14; i++) {
            set<char> marker;
            for (int j = i; j < i + 14; j++) {
                marker.insert(s[j]);
            }
            if (len(marker) == 14) {
                printf("Part 2 res: %d\n", i + 14);
                break;
            }
            
        }
    }


    return 0;
}