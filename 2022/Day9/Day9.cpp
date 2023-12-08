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

void print_positions(vector<pair<int, int>> &vec) {
    for (int i = 0; i < len(vec); i++) {
        cout << "(" << vec[i].first << "," << vec[i].second << ") ";
    }
    cout << endl;
}

int main() {
    fast;
    string s;
    smatch match;
    
    set<pair<int, int>> tail_pos_1;
    set<pair<int, int>> tail_pos_2;


    vector<pair<int, int>> positions(10, MP(0, 0));
    print_positions(positions);


    int head_x = 0, head_y = 0;
    int tail_x = 0, tail_y = 0;
    
    tail_pos_1.insert(MP(tail_x, tail_y));
    tail_pos_2.insert(MP(tail_x, tail_y));
    
    auto re = regex("(R|U|L|D) ([0-9]+)");
    while (getline(cin, s)) {
        regex_match(s, match, re);
        string dir = match.str(1);
        int steps = stoi(match.str(2));
        if (dir == "U") {
            for (int i = 0; i < steps; i++) {
                for (int j = 0; j < 10; j++) {
                    head_x = positions[len(positions) - j - 1].first; head_y = positions[len(positions) - j - 1].second;
                    tail_x = positions[len(positions) - j - 2].first; tail_y = positions[len(positions) - j - 2].second;
                    
                    if (head_x == tail_x && head_y == tail_y) {
                        head_y++;
                    } else {

                        head_y++;
                        if (abs(head_y - tail_y) > 1) {
                            if (head_x > tail_x) {
                                tail_x++;
                            } else if (head_x < tail_x) {
                                tail_x--;
                            }
                            tail_y++;
                        }
                    }
                    // tail_pos_1.insert(MP(tail_x, tail_y));
                    tail_pos_1.insert(MP(tail_x, tail_y));
                    positions[len(positions) - 1 - j] = MP(head_x, head_y);
                    positions[len(positions) - 2 - j] = MP(tail_x, tail_y);
                    // cout << "head position (" << head_x << " " << head_y << ")" << endl;
                    // cout << "tail position (" << tail_x << " " << tail_y << ")" << endl;
                }
            }
            // print("-----");

        } else if (dir == "D") {
            for (int i = 0; i < steps; i++) {
                for (int j = 0; j < 10; j++) {
                    head_x = positions[len(positions) - j - 1].first; head_y = positions[len(positions) - j - 1].second;
                    tail_x = positions[len(positions) - j - 2].first; tail_y = positions[len(positions) - j - 2].second;
                    if (head_x == tail_x && head_y == tail_y) {
                        head_y--;
                    } else {

                        head_y--;
                        if (abs(tail_y - head_y) > 1) {
                            if (head_x > tail_x) {
                                tail_x++;
                            } else if (head_x < tail_x) {
                                tail_x--;
                            }
                            tail_y--;
                        }
                    }
                    tail_pos_1.insert(MP(tail_x, tail_y));
                    // cout << "head position (" << head_x << " " << head_y << ")" << endl;
                    // cout << "tail position (" << tail_x << " " << tail_y << ")" << endl;
                    positions[len(positions) - 1 - j] = MP(head_x, head_y);
                    positions[len(positions) - 2 - j] = MP(tail_x, tail_y);
                }
            }
            // print("-----");
            
        } else if (dir == "R") {
            for (int i = 0; i < steps; i++) {
                for (int j = 0; j < 10; j++) {
                    head_x = positions[len(positions) - j - 1].first; head_y = positions[len(positions) - j - 1].second;
                    tail_x = positions[len(positions) - j - 2].first; tail_y = positions[len(positions) - j - 2].second;
                    if (head_x == tail_x && head_y == tail_y) {
                        head_x++;
                    } else {

                        head_x++;
                        if (abs(tail_x - head_x) > 1) {
                            if (head_y > tail_y) {
                                tail_y++;
                            } else if (head_y < tail_y) {
                                tail_y--;
                            }
                            tail_x++;
                        }
                    }
                    tail_pos_1.insert(MP(tail_x, tail_y));
                    // cout << "head position (" << head_x << " " << head_y << ")" << endl;
                    // cout << "tail position (" << tail_x << " " << tail_y << ")" << endl;
                    positions[len(positions) - 1 - j] = MP(head_x, head_y);
                    positions[len(positions) - 2 - j] = MP(tail_x, tail_y);
                }
            }
            // print("-----");

        } else {
            for (int i = 0; i < steps; i++) {
                for (int j = 0; j < 10; j++) {
                    head_x = positions[len(positions) - j - 1].first; head_y = positions[len(positions) - j - 1].second;
                    tail_x = positions[len(positions) - j - 2].first; tail_y = positions[len(positions) - j - 2].second;
                    if (head_x == tail_x && head_y == tail_y) {
                        head_x--;
                    } else {

                        head_x--;
                        if (abs(tail_x - head_x) > 1) {
                            if (head_y > tail_y) {
                                tail_y++;
                            } else if (head_y < tail_y) {
                                tail_y--;
                            }
                            tail_x--;
                        }
                    }
                    tail_pos_1.insert(MP(tail_x, tail_y));
                    // cout << "head position (" << head_x << " " << head_y << ")" << endl;
                    // cout << "tail position (" << tail_x << " " << tail_y << ")" << endl;
                    positions[len(positions) - 1 - j] = MP(head_x, head_y);
                    positions[len(positions) - 2 - j] = MP(tail_x, tail_y);
                }
            // print("-----");

            }
        }
    }
    printf("Res part a: %d\n", len(tail_pos_1));
    return 0;
}