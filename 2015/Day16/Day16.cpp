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

    int part_1_res = 0;
    int part_2_res = 0;

    map<string, int> target = {
        {"children", 3}, {"cats", 7}, {"samoyeds", 2}, {"pomeranians", 3}, {"akitas", 0},
        {"vizslas", 0}, {"goldfish", 5}, {"trees", 3}, {"cars", 2}, {"perfumes", 1}
    };

    for (size_t i = 0; i < file_content.size(); i++) {
        string line = file_content[i];
        line.erase(remove(line.begin(), line.end(), ':'), line.end());
        line.erase(remove(line.begin(), line.end(), ','), line.end());
        vector<string> parts = split(line);

        bool matches = true;
        bool matches_2 = true;
        for (size_t idx = 2; idx < parts.size(); idx += 2) {
            const string& detect = parts[idx];
            int val = stoi(parts[idx + 1]);
            int expected = target[detect];
            if (expected != val) matches = false;

            // Part 2: cats and trees are lower bounds, pomeranians and goldfish upper bounds
            if (detect == "cats" || detect == "trees") {
                if (val <= expected) matches_2 = false;
            } else if (detect == "pomeranians" || detect == "goldfish") {
                if (val >= expected) matches_2 = false;
            } else if (expected != val) {
                matches_2 = false;
            }
        }
        if (matches) part_1_res = i + 1;
        if (matches_2) part_2_res = i + 1;
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
