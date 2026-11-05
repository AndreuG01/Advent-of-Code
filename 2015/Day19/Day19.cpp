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

typedef vector<pair<string, string>> Rules;

int fewest_steps(const string& molecule, Rules rules) {
    // Work backwards from the molecule to "e". Every way down takes the same number
    // of steps, but a greedy path can get stuck, so restart with a new order if it does
    mt19937 generator(random_device{}());
    while (true) {
        shuffle(rules.begin(), rules.end(), generator);
        string curr = molecule;
        int steps = 0;
        bool changed = true;
        while (curr != "e" && changed) {
            changed = false;
            for (const auto& [source, target] : rules) {
                size_t i = curr.find(target);
                if (i != string::npos) {
                    curr.replace(i, target.size(), source);
                    steps += 1;
                    changed = true;
                    break;
                }
            }
        }
        if (curr == "e") return steps;
    }
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    string molecule = file_content.back();
    Rules replacements;
    for (const string& line : file_content) {
        size_t arrow = line.find(" => ");
        if (arrow != string::npos) replacements.push_back({line.substr(0, arrow), line.substr(arrow + 4)});
    }

    set<string> molecules;
    for (const auto& [source, target] : replacements) {
        size_t i = molecule.find(source);
        while (i != string::npos) {
            molecules.insert(molecule.substr(0, i) + target + molecule.substr(i + source.size()));
            i = molecule.find(source, i + 1);
        }
    }

    size_t part_1_res = molecules.size();
    int part_2_res = fewest_steps(molecule, replacements);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
