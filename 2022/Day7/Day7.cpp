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


class Directory {
    public:
        string dir_name;
        vector<Directory> dirs;
        vector<int> files;

        Directory(string &name) {
            dir_name = name;
            dirs = vector<Directory>();
            files = vector<int>();
        }

        Directory *find_directory(Directory *root, const string &name) {
            if (root->dir_name == name) {
                return root;
            }

            for (auto &child : root->dirs) {
                Directory *res = find_directory(&child, name);
                if (res != nullptr) {
                    return res;
                }
            }

            return nullptr;
        }

        void add_file(Directory *root, string &parent_dir_name, int file_size) {
            Directory *parent_dir = find_directory(root, parent_dir_name);

            if (parent_dir != nullptr) {
                parent_dir->files.PB(file_size);
            }
        }

        void add_directory(Directory *root, string &parent_dir_name, string &add_dir_name) {
            Directory *parent_dir = find_directory(root, parent_dir_name);

            if (parent_dir != nullptr) {
                Directory add_dir = Directory(add_dir_name);
                parent_dir->dirs.PB(add_dir);
            }
        }

        int size_files_dir() {
            int res = 0;
            for (auto file : this->files) {
                res += file;
            }

            // if (this->dirs.size() > 0) {
                for (auto dir : this->dirs) {
                    res += dir.size_files_dir();
                }
            // }

            return res;
        }

        void print_directory(int level) {
            print(this->dir_name);
            for (auto file : files) {
                for (int i = 0; i < level; i++) cout << "  ";
                print(file);
            }

            for (auto dir : dirs) {
                for (int i = 0; i < level; i++) cout << "  ";
                dir.print_directory(level + 1);
            }
        }
};


int main() {
    fast;

    string s;
    map<pair<char, int>, int> directories;
    smatch match;
    auto re_dir = regex("dir ([a-z]+)");
    auto re_file = regex("([0-9]+) ([a-z]+).?([a-z]+)?");
    auto re_dir_name = regex("\\$ cd (.+)");

    vector<string> order_dirs;
    set<string> all_dirs;
    vector<int> dir_sizes;
    vector<int> target_dirs;
    string root_name = "/";
    string parent_dir;
    Directory root = Directory(root_name);

    while (getline(cin, s)) {
        if (s[0] == '$') {
            regex_match(s, match, re_dir_name);
            if (match.str(0) != "") {
                if (match.str(1) == "..") order_dirs.pop_back();
                else {
                    order_dirs.PB(match.str(1));
                    all_dirs.insert(match.str(1));
                }
            }
        } else if ('1' <= s[0] && s[0] <= '9') {
            regex_match(s, match, re_file);
            root.add_file(&root, order_dirs.back(), stoi(match.str(1)));
            // cout << "adding file " << match.str(1) << " parent " << order_dirs.back() << endl;
        } else {
            regex_match(s, match, re_dir);
            string parent_dir = match.str(1);
            root.add_directory(&root, order_dirs.back(), parent_dir);
        }
    }

    root.print_directory(0);
    
    for (auto dir : all_dirs) {
        Directory *curr_dir = root.find_directory(&root, dir);
        int size = curr_dir->size_files_dir();
        if (size <= 100000) {
            target_dirs.PB(size);
        }
        cout << dir << " " << size << endl;
    }
    
    int res_a = 0;
    for (int i = 0; i < len(target_dirs); i++) {
        res_a += target_dirs[i];
    }

    printf("Part 1 res: %d\n", res_a);

    return 0;
}