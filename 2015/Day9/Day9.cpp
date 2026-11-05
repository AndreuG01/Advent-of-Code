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

    // Distances work both ways, so store each pair in both directions
    map<pair<string, string>, int> distances;
    set<string> cities;
    for (const string& line : file_content) {
        vector<string> parts = split(line);  // "London to Dublin = 464"
        string a = parts[0], b = parts[2];
        int dist = stoi(parts[4]);
        distances[{a, b}] = dist;
        distances[{b, a}] = dist;
        cities.insert(a);
        cities.insert(b);
    }

    // Few cities, so trying every order is fast enough
    vector<string> route(cities.begin(), cities.end());
    int part_1_res = INT32_MAX;
    int part_2_res = 0;
    do {
        int length = 0;
        for (size_t i = 0; i + 1 < route.size(); i++) length += distances[{route[i], route[i + 1]}];
        part_1_res = min(part_1_res, length);
        part_2_res = max(part_2_res, length);
    } while (next_permutation(route.begin(), route.end()));

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
