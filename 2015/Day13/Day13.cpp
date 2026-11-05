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

// happiness[{a, b}] = how much a's happiness changes when sitting next to b
map<pair<string, string>, int> happiness;

int total_happiness(const vector<string>& arrangement) {
    int total = 0;
    for (size_t i = 0; i < arrangement.size(); i++) {
        const string& a = arrangement[i];
        const string& b = arrangement[(i + 1) % arrangement.size()];  // the table is round
        total += happiness[{a, b}] + happiness[{b, a}];
    }
    return total;
}

int best_arrangement(const set<string>& people) {
    // The table is round, so rotations are the same seating: fix the first
    // person and only try every order of the rest
    vector<string> arrangement(people.begin(), people.end());
    int best = INT32_MIN;
    do {
        best = max(best, total_happiness(arrangement));
    } while (next_permutation(arrangement.begin() + 1, arrangement.end()));
    return best;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    set<string> people;
    for (string line : file_content) {
        // e.g. "Alice would gain 54 happiness units by sitting next to Bob."
        line.pop_back();
        vector<string> words = split(line);
        string person = words[0], neighbour = words.back();
        int amount = stoi(words[3]);
        happiness[{person, neighbour}] = words[2] == "gain" ? amount : -amount;
        people.insert(person);
        people.insert(neighbour);
    }

    int part_1_res = best_arrangement(people);

    // Part 2: add yourself, with 0 happiness towards and from everyone
    for (const string& person : people) {
        happiness[{"Me", person}] = 0;
        happiness[{person, "Me"}] = 0;
    }
    people.insert("Me");
    int part_2_res = best_arrangement(people);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
