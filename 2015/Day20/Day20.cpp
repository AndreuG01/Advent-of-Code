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
    int target = stoi(read_text(argv[1]));

    int part_1_res = 0;
    int part_2_res = 0;

    // House n gets 10 presents from each elf that divides n, and house target / 10 + 1
    // alone gets at least target presents from its own elf, so the answer can't be further away
    int limit = target / 10 + 1;
    vector<int> houses(limit + 1, 0);
    for (int elf = 1; elf <= limit; elf++) {
        for (int house = elf; house <= limit; house += elf) houses[house] += elf * 10;
    }

    for (int house = 1; house <= limit; house++) {
        if (houses[house] >= target) {
            part_1_res = house;
            break;
        }
    }

    // Part 2: each elf only visits 50 houses, but leaves 11 presents per house
    limit = target / 11 + 1;
    houses.assign(limit + 1, 0);
    for (int elf = 1; elf <= limit; elf++) {
        for (ll house = elf; house <= min((ll)elf * 50, (ll)limit); house += elf) houses[house] += elf * 11;
    }

    for (int house = 1; house <= limit; house++) {
        if (houses[house] >= target) {
            part_2_res = house;
            break;
        }
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
