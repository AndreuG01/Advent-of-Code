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

void combinations_sum(int num_elems, int total, vector<int>& amounts, const function<void(const vector<int>&)>& visit) {
    if (num_elems == 1) {
        // The last value has to be whatever is left
        amounts.push_back(total);
        visit(amounts);
        amounts.pop_back();
        return;
    }
    for (int first = 0; first <= total; first++) {
        amounts.push_back(first);
        combinations_sum(num_elems - 1, total - first, amounts, visit);
        amounts.pop_back();
    }
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    vector<vector<int>> multipliers(4);
    vector<int> calories;

    for (string line : file_content) {
        line.erase(remove(line.begin(), line.end(), ','), line.end());
        vector<string> splited_elems = split(line);
        multipliers[0].push_back(stoi(splited_elems[2]));
        multipliers[1].push_back(stoi(splited_elems[4]));
        multipliers[2].push_back(stoi(splited_elems[6]));
        multipliers[3].push_back(stoi(splited_elems[8]));
        calories.push_back(stoi(splited_elems[10]));
    }

    ll part_1_res = 0;
    ll part_2_res = 0;

    vector<int> amounts;
    combinations_sum(file_content.size(), 100, amounts, [&](const vector<int>& curr) {
        ll curr_res = 1;
        for (const vector<int>& prop : multipliers) {
            ll total = inner_product(prop.begin(), prop.end(), curr.begin(), 0LL);
            curr_res *= max(total, 0LL);
        }
        part_1_res = max(part_1_res, curr_res);
        // Part 2: only cookies with exactly 500 calories
        if (inner_product(calories.begin(), calories.end(), curr.begin(), 0) == 500) {
            part_2_res = max(part_2_res, curr_res);
        }
    });

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
