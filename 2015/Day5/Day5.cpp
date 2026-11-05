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

bool three_vowels(const string& s) {
    int count = 0;
    for (char c : s) {
        if (string("aeiou").find(c) != string::npos) count += 1;
    }
    return count >= 3;
}

bool repeated_chars(const string& s) {
    for (size_t i = 1; i < s.size(); i++) {
        if (s[i] == s[i - 1]) return true;
    }
    return false;
}

bool substrings(const string& s) {
    for (const string& sub : {"ab", "cd", "pq", "xy"}) {
        if (s.find(sub) != string::npos) return false;
    }
    return true;
}

bool two_grams(const string& s) {
    map<string, size_t> first_seen;
    for (size_t i = 0; i + 1 < s.size(); i++) {
        string pair = s.substr(i, 2);
        auto found = first_seen.find(pair);
        if (found != first_seen.end() && i - found->second >= 2) return true;
        first_seen.insert({pair, i});
    }
    return false;
}

bool three_grams(const string& s) {
    for (size_t i = 0; i + 2 < s.size(); i++) {
        if (s[i] == s[i + 2]) return true;
    }
    return false;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    int part_1_res = 0;
    int part_2_res = 0;

    for (const string& s : file_content) {
        if (three_vowels(s) && repeated_chars(s) && substrings(s)) part_1_res += 1;
        if (two_grams(s) && three_grams(s)) part_2_res += 1;
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
