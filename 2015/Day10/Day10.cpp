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

string look_and_say(const string& s) {
    int count = 1;
    char val = s[0];
    string new_str;
    for (size_t i = 1; i < s.size(); i++) {
        if (s[i] == val) {
            count += 1;
        } else {
            new_str += to_string(count);
            new_str += val;
            count = 1;
        }
        val = s[i];
    }
    new_str += to_string(count);
    new_str += val;
    return new_str;
}

int main(int argc, char** argv) {
    string seq = read_text(argv[1]);

    size_t part_1_res = 0;
    size_t part_2_res = 0;

    for (int i = 0; i < 50; i++) {
        seq = look_and_say(seq);
        if (i == 39) part_1_res = seq.size();
    }
    part_2_res = seq.size();

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
