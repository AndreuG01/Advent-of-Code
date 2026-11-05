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

typedef pair<int, int> pi;

pi move_position(pi position, char elem) {
    if (elem == '^') return {position.first, position.second + 1};
    if (elem == '>') return {position.first + 1, position.second};
    if (elem == '<') return {position.first - 1, position.second};
    return {position.first, position.second - 1};
}

int main(int argc, char** argv) {
    string file_content = read_text(argv[1]);

    pi curr_pos = {0, 0};
    set<pi> unique_pos = {curr_pos};
    for (char elem : file_content) {
        curr_pos = move_position(curr_pos, elem);
        unique_pos.insert(curr_pos);
    }
    size_t part_1_res = unique_pos.size();

    pi santas[2] = {{0, 0}, {0, 0}};  // Santa and Robo-Santa
    set<pi> visited = {{0, 0}};
    for (size_t i = 0; i < file_content.size(); i++) {
        santas[i % 2] = move_position(santas[i % 2], file_content[i]);
        visited.insert(santas[i % 2]);
    }
    size_t part_2_res = visited.size();

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
