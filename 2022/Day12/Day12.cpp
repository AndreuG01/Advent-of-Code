#include <bits/stdc++.h>
#include <regex>


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

template <class E> class SearchNode {
public:
    E e;
    int cost;

    SearchNode(E e, int cost = 0) : e{e}, cost{cost} {}

    bool operator<(const SearchNode<E>& other) const{
        return cost > other.cost; // Order is reversed to order nodes in increasing cost.
    }
};

// FIXME: Store any information of the edge here. If no info is needed leave it as this.
struct edgeInfo {
    int cost = 1;
};

template <class E> class Graph {
public:
    unordered_map<E, unordered_map<E, edgeInfo>> g;
    bool d;

    Graph(int n, bool directed = true) : d{directed} {
        g.reserve(n);
    }

    void addEdge(E a, E b, edgeInfo ei = edgeInfo()) { // edgeInfo is an optional parameter
        g[a][b] = ei;
        if (!d) g[b][a] = ei;
    }

    void removeEdge(E a, E b) {
        g[a].erase(a);
        if (!d) g[b].erase(a);
    }

    const unordered_map<E, edgeInfo>& childs (E e) const {
        return g.at(e);
    }

    void visit (E u) const { // FIXME: Modify as needed
        cout << u << " ";
    }

    int ucost(E start, E goal) const {
        unordered_set<E> v {start}; // visited nodes
        priority_queue<SearchNode<E>> f; // frontier
        f.emplace(start);

        while (!f.empty()) {
            auto curr = f.top();
            f.pop();
            visit(curr.e);
            
            if (curr.e == goal) return curr.cost; // FIXME: Modify as needed

            for (auto const& [c, ei] : childs(curr.e)) {
                if (v.count(c) == 0) {
                    f.emplace(c, curr.cost + ei.cost); // Enqueue adjacent node
                    v.insert(c); // Add them to visited 
                }
            }
        }
        return -1;
    }
};

int main() {
    fast;
    string s;
    vector<vector<char>> grid(5);
    int line_num = 0;

    Graph<char> g(40, false);
    
    while (getline(cin, s)) {
        for (auto c : s) grid[line_num].PB(c);
        line_num++;
    }

    for (int i = 0; i < len(grid); i++) {
        for (int j = 0; j < len(grid[0]); j++) {
            cout << grid[i][j];
        }
        cout << endl;
    }



    
    return 0;
}