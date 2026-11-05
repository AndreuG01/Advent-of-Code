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
    string file_content = read_text(argv[1]);

    ll part_1_res = 0;
    ll part_2_res = 0;

    vector<ll> nums;
    regex number("[0-9]+");
    for (sregex_iterator it(file_content.begin(), file_content.end(), number), end; it != end; ++it) {
        nums.push_back(stoll(it->str()));
    }
    ll row = nums[0], col = nums[1];

    // Codes fill the grid by diagonals: (row, col) is on diagonal row + col - 1,
    // and all the diagonals before it hold 1 + 2 + ... + (diagonal - 1) codes
    ll diagonal = row + col - 1;
    ll position = diagonal * (diagonal - 1) / 2 + col;

    ll code = 20151125;
    for (ll i = 0; i < position - 1; i++) code = code * 252533 % 33554393;

    part_1_res = code;

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
