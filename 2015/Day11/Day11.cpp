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

bool increasing_straight(const string& s) {
    for (size_t i = 2; i < s.size(); i++) {
        char a = s[i], b = s[i - 1], c = s[i - 2];
        if (b == c + 1 && a == b + 1) return true;
    }
    return false;
}

bool letters(const string& s) {
    for (char c : s) {
        if (c == 'i' || c == 'o' || c == 'l') return false;
    }
    return true;
}

bool two_grams(const string& s) {
    int found = 0;
    size_t i = 1;
    while (i < s.size()) {
        if (s[i] == s[i - 1]) {
            found += 1;
            i += 2;  // skip so the pairs can't overlap
        } else {
            i += 1;
        }
    }
    return found >= 2;
}

bool is_valid(const string& s) {
    return increasing_straight(s) && two_grams(s) && letters(s);
}

string increment(string s) {
    int i = (int)s.size() - 1;
    while (i >= 0) {
        if (s[i] == 'z') {
            s[i] = 'a';  // wrap around and carry to the next letter on the left
            i -= 1;
        } else {
            s[i] += 1;
            break;
        }
    }
    return s;
}

int main(int argc, char** argv) {
    string file_content = read_text(argv[1]);

    string part_1_res = increment(file_content);
    while (!is_valid(part_1_res)) part_1_res = increment(part_1_res);

    string part_2_res = increment(part_1_res);
    while (!is_valid(part_2_res)) part_2_res = increment(part_2_res);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
