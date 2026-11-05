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

const int MASK = 0xFFFF;  // signals are 16-bit

// Instructions are not in order, so first store how each wire is computed,
// then resolve wires recursively (memoized) when asked for
map<string, vector<string>> circuit;
map<string, int> cache;

bool is_number(const string& s) {
    return all_of(s.begin(), s.end(), [](char c) { return isdigit((unsigned char)c); });
}

int signal(const string& name) {
    if (is_number(name)) return stoi(name);
    auto cached = cache.find(name);
    if (cached != cache.end()) return cached->second;

    const vector<string>& operation = circuit[name];
    int result;
    if (operation.size() == 1) {
        // e.g. "123 -> x" or "lx -> a"
        result = signal(operation[0]);
    } else if (operation.size() == 2) {
        // NOT x
        result = ~signal(operation[1]) & MASK;
    } else {
        const string& action = operation[1];
        if (action == "AND") result = signal(operation[0]) & signal(operation[2]);
        else if (action == "OR") result = signal(operation[0]) | signal(operation[2]);
        else if (action == "LSHIFT") result = (signal(operation[0]) << stoi(operation[2])) & MASK;
        else result = signal(operation[0]) >> stoi(operation[2]);
    }
    cache[name] = result;
    return result;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    int part_1_res = 0;
    int part_2_res = 0;

    for (const string& line : file_content) {
        size_t arrow = line.find(" -> ");
        circuit[line.substr(arrow + 4)] = split(line.substr(0, arrow));
    }

    if (circuit.count("a")) {
        part_1_res = signal("a");

        // Part 2: override wire b with part 1's signal, reset all wires and rerun
        circuit["b"] = {to_string(part_1_res)};
        cache.clear();
        part_2_res = signal("a");
    } else {
        // The example has no wire "a": show every wire instead
        for (const auto& [wire, operation] : circuit) cout << wire << ": " << signal(wire) << '\n';
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
