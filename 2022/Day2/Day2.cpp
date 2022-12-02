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

// PART 2:  X -> we need to lose
//          Y -> we need to draw
//          Z -> we need to win

int main() {
    fast;
    string op, you;
    int total_1 = 0;
    int total_2 = 0;
    while (cin >> op >> you) {
        if (op == "A") { // Rock
            if (you == "X") { // Rock draw +1
                total_1 += 3 + 1;
                total_2 += 0 + 3; // We need to lose (scissors)
            } else if (you == "Y") { // Paper win +2
                total_1 += 8;
                total_2 += 3 + 1; // We need to draw (rock)
            } else {
                total_1 += 3;
                total_2 += 6 + 2; // We need to win (paper)
            }
        } else if (op == "B") { // Paper
            if (you == "Y") { // Paper draw +2
                total_1 += 5;
                total_2 += 3 + 2; // We need to draw (paper)
            } else if (you == "Z") { // Scissors win +3
                total_1 += 9;
                total_2 += 6 + 3; // We need to win (scissors)
            } else{
                total_1 += 1;
                total_2 += 0 + 1; // We need to lose (rock)
            } 
        } else if (op == "C") { // Scissors
            if (you == "X") {
                total_1 += 7;
                total_2 += 0 + 2; // We need to lose (paper)
            } else if (you == "Z") {
                total_1 += 6;
                total_2 += 6 + 1; // We need to win (rock)
            } else {
                total_1 += 2;
                total_2 += 3 + 3; // We need to draw (scissors)
            }
        }
    }
    printf("Part 1 res: %d\n", total_1);
    printf("Part 2 res: %d\n", total_2);

    return 0;
}