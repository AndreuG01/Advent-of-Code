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
    vector<vector<int>> trees(100);
    int idx = 0;
    while (cin >> s) {
        for (auto c : s) {
            trees[idx].PB((int)c - 48);
        }
        idx++;
    }

    int visible = 0;
    int max_score = 0;
    for (int i = 0; i < idx; i++) {
        for (int j = 0; j < len(trees[0]); j++) {
            bool is_visible1 = true;
            bool is_visible2 = true;
            bool is_visible3 = true;
            bool is_visible4 = true;
            int curr_tree = trees[i][j];
            int score_left = 0, score_right = 0, score_top = 0, score_bottom = 0, score = 0;
            
            // Left visible
            for (int col = j - 1; col >= 0; col--) {
                score_left++;
                if (trees[i][col] >= curr_tree) {
                    is_visible1 = false;
                    break;
                }
            }
            
            // Right visible
            for (int col = j + 1; col < len(trees[0]); col++) {
                score_right++;
                if (trees[i][col] >= curr_tree) {
                    is_visible2 = false;
                    break;
                }
            }

            // Top visible
            for (int row = i - 1; row >= 0; row--) {
                score_top++;
                if (trees[row][j] >= curr_tree) {
                    // printf("\t(TOP) %d, %d --> length %d\n", row, j, trees[row][j]);
                    is_visible3 = false;
                    
                    break;
                }
            }

            // Bottom visible
            for (int row = i + 1; row < idx; row++) {
                score_bottom++;
                if (trees[row][j] >= curr_tree) {
                    is_visible4 = false;
                    break;
                }
            }
            score = score_left * score_right * score_top * score_bottom;
            if (score >= max_score) max_score = score;

            if (is_visible1 || is_visible2 || is_visible3 || is_visible4) visible++;
        }
    }
    printf("Res part a: %d\n", visible);
    printf("Res part b: %d\n", max_score);
    return 0;
}