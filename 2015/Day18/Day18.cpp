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

typedef vector<string> Grid;

vector<pair<int, int>> get_neighbors(int i, int j, int max_i, int max_j) {
    vector<pair<int, int>> neighbors;
    for (int a = -1; a <= 1; a++) {
        for (int b = -1; b <= 1; b++) {
            if (a == 0 && b == 0) continue;
            if (i + a >= 0 && i + a < max_i && j + b >= 0 && j + b < max_j) neighbors.push_back({i + a, j + b});
        }
    }
    return neighbors;
}

void turn_on_corners(Grid& grid) {
    int max_i = grid.size() - 1, max_j = grid[0].size() - 1;
    grid[0][0] = grid[0][max_j] = grid[max_i][0] = grid[max_i][max_j] = '#';
}

int simulate(Grid grid, int N, bool stuck_corners = false) {
    // grid is a copy, so each part starts from the input
    if (stuck_corners) turn_on_corners(grid);

    for (int turn = 0; turn < N; turn++) {
        vector<pair<int, int>> change;
        for (int i = 0; i < (int)grid.size(); i++) {
            for (int j = 0; j < (int)grid[i].size(); j++) {
                int on = 0;
                for (auto [x, y] : get_neighbors(i, j, grid.size(), grid[0].size())) {
                    if (grid[x][y] == '#') on += 1;
                }

                if (grid[i][j] == '#' && on != 2 && on != 3) change.push_back({i, j});
                else if (grid[i][j] == '.' && on == 3) change.push_back({i, j});
            }
        }

        // All lights change at the same time, so only apply the changes after checking every light
        for (auto [i, j] : change) grid[i][j] = grid[i][j] == '#' ? '.' : '#';

        if (stuck_corners) turn_on_corners(grid);
    }

    int total = 0;
    for (const string& row : grid) total += count(row.begin(), row.end(), '#');
    return total;
}

int main(int argc, char** argv) {
    Grid file_content = read_lines(argv[1]);

    bool is_example = string(argv[1]).find("example") != string::npos;
    int part_1_res = simulate(file_content, is_example ? 4 : 100);
    int part_2_res = simulate(file_content, is_example ? 5 : 100, true);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
