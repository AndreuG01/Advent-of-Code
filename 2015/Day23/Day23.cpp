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

vector<vector<string>> instructions;

map<string, ll> run(map<string, ll> registers) {
    int pc = 0;
    while (pc >= 0 && pc < (int)instructions.size()) {
        const vector<string>& instruction = instructions[pc];
        const string& action = instruction[0];
        if (action == "hlf") {
            registers[instruction[1]] /= 2;
        } else if (action == "tpl") {
            registers[instruction[1]] *= 3;
        } else if (action == "inc") {
            registers[instruction[1]] += 1;
        } else if (action == "jmp") {
            pc += stoi(instruction[1]);
            continue;
        } else if (action == "jie" && registers[instruction[1]] % 2 == 0) {
            pc += stoi(instruction[2]);
            continue;
        } else if (action == "jio" && registers[instruction[1]] == 1) {  // jump if ONE, not if odd
            pc += stoi(instruction[2]);
            continue;
        }
        pc += 1;
    }
    return registers;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    for (string line : file_content) {
        line.erase(remove(line.begin(), line.end(), ','), line.end());
        instructions.push_back(split(line));
    }

    map<string, ll> registers = run({{"a", 0}, {"b", 0}});
    // The puzzle's example asks for register a
    bool is_example = string(argv[1]).find("example") != string::npos;
    ll part_1_res = is_example ? registers["a"] : registers["b"];

    // Part 2: same program, but register a starts at 1
    ll part_2_res = run({{"a", 1}, {"b", 0}})["b"];

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
