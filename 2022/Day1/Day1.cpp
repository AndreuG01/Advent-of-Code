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
    int total = 0;
    priority_queue<int> calories;
    
    while (getline(cin, curr)) {
        if (curr == "") {
            calories.push(total);
            total = 0;
        } else {
            total += stoi(curr);
        }
    }
    calories.push(total);
    
    int a, b, c;
    a = calories.top(); calories.pop();
    b = calories.top(); calories.pop();
    c = calories.top();
    
    printf("Part 1 res: %d\n", a);
    printf("Part 2 res: %d\n", a + b + c);

    return 0;
}