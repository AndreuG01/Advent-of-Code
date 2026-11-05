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

    ll part_1_res = 0;
    ll part_2_res = 0;

    for (const string& line : file_content) {
        vector<string> elem = split(line, 'x');
        ll l = stoll(elem[0]);
        ll w = stoll(elem[1]);
        ll h = stoll(elem[2]);

        ll a_side_1 = l * w;
        ll a_side_2 = w * h;
        ll a_side_3 = h * l;

        ll p_side_1 = 2 * l + 2 * w;
        ll p_side_2 = 2 * w + 2 * h;
        ll p_side_3 = 2 * h + 2 * l;

        part_1_res += 2 * a_side_1 + 2 * a_side_2 + 2 * a_side_3 + min({a_side_2, a_side_1, a_side_3});
        part_2_res += min({p_side_1, p_side_2, p_side_3}) + l * w * h;
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
