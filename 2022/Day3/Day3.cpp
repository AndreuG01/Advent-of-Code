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
    int total = 0;
    while (cin >> s) {
        vec_part2.PB(s);
        int length = len(s);
        string c1, c2;
        c1 = s.substr(0, length / 2);
        c2 = s.substr(length / 2, length / 2);
        
        char repeated;
        for (auto c : c1) {
            if (c2.find(c) != string::npos) repeated = c;
        }

        int val = 0;
        if (repeated >= 'a' && repeated <= 'z')
            val = (int)(repeated - 'a' + 1);
        else
            val = (int)(repeated - 'A' + 1 + 26);

        total += val;   
    }
    
    printf("Part 1 res: %d\n", total);

    string s1, s2, s3;
    total = 0;
    for (int i = 0; i < len(vec_part2); i++) {
        s1 = vec_part2[i];
        s2 = vec_part2[++i];
        s3 = vec_part2[++i];
        
        char repeated;
        for (auto c : s1) {
            if (s2.find(c) != string::npos && s3.find(c) != string::npos) {
                repeated = c;
            }
        }
        
        int val = 0;
        if (repeated >= 'a' && repeated <= 'z')
            val = (int)(repeated - 'a' + 1);
        else
            val = (int)(repeated - 'A' + 1 + 26);

        total += val;
    }

    printf("Part 2 res: %d\n", total);

    return 0;
}