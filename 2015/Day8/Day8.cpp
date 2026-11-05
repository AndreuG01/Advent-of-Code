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

int memory_length(const string& line) {
    string inner = line.substr(1, line.size() - 2);  // drop the surrounding quotes
    size_t i = 0;
    int mem_len = 0;
    while (i < inner.size()) {
        if (inner[i] == '\\') i += inner[i + 1] == 'x' ? 4 : 2;
        else i += 1;
        mem_len += 1;
    }
    return mem_len;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    int part_1_res = 0;
    int part_2_res = 0;

    for (const string& line : file_content) {
        part_1_res += line.size() - memory_length(line);
        // Encoding adds the 2 new quotes and one backslash for each " and backslash
        part_2_res += 2 + count(line.begin(), line.end(), '"') + count(line.begin(), line.end(), '\\');
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
