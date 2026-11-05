#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

typedef long long ll;

string read_text(const char* path) {
    ifstream file(path);
    stringstream buffer;
    buffer << file.rdbuf();
    string text = buffer.str();
    while (!text.empty() && isspace((unsigned char)text.back())) text.pop_back();
    return text;
}

vector<string> read_lines(const char* path) {
    stringstream text(read_text(path));
    vector<string> lines;
    string line;
    while (getline(text, line)) lines.push_back(line);
    return lines;
}

vector<string> split(const string& s, char sep = ' ') {
    vector<string> parts;
    stringstream stream(s);
    string part;
    while (getline(stream, part, sep)) parts.push_back(part);
    return parts;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    vector<vector<int>> points(1000, vector<int>(1000, 0));
    vector<vector<int>> points_2(1000, vector<int>(1000, 0));

    for (const string& line : file_content) {
        vector<string> elems = split(line);
        // "toggle a,b through c,d" has 4 words, "turn on a,b through c,d" has 5
        string action = elems.size() == 4 ? "toggle" : elems[1];
        vector<string> nums_f = split(elems[elems.size() - 3], ',');
        vector<string> nums_t = split(elems[elems.size() - 1], ',');
        int f_x = stoi(nums_f[0]), f_y = stoi(nums_f[1]);
        int t_x = stoi(nums_t[0]), t_y = stoi(nums_t[1]);

        for (int x = f_x; x <= t_x; x++) {
            for (int y = f_y; y <= t_y; y++) {
                if (action == "off") {
                    points[x][y] = 0;
                    points_2[x][y] = max(0, points_2[x][y] - 1);
                } else if (action == "on") {
                    points[x][y] = 1;
                    points_2[x][y] += 1;
                } else {
                    points[x][y] = 1 - points[x][y];
                    points_2[x][y] += 2;
                }
            }
        }
    }

    ll part_1_res = 0;
    ll part_2_res = 0;
    for (int x = 0; x < 1000; x++) {
        for (int y = 0; y < 1000; y++) {
            part_1_res += points[x][y];
            part_2_res += points_2[x][y];
        }
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
