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

typedef vector<ll> Group;

ll prod(const Group& group) {
    ll result = 1;
    for (ll weight : group) result *= weight;
    return result;
}

Group without(const Group& weights, const Group& group) {
    Group rest = weights;
    for (ll weight : group) rest.erase(find(rest.begin(), rest.end(), weight));
    return rest;
}

// All groups of exactly size packages that add up to target
void combinations(const Group& weights, size_t start, int size, ll target, Group& curr, vector<Group>& groups) {
    if (size == 0) {
        if (target == 0) groups.push_back(curr);
        return;
    }
    for (size_t i = start; i < weights.size(); i++) {
        if (weights[i] > target) continue;
        curr.push_back(weights[i]);
        combinations(weights, i + 1, size - 1, target - weights[i], curr, groups);
        curr.pop_back();
    }
}

vector<Group> groups_of_size(const Group& weights, int size, ll target) {
    vector<Group> groups;
    Group curr;
    combinations(weights, 0, size, target, curr, groups);
    return groups;
}

bool can_split(const Group& weights, int num_groups, ll target) {
    if (num_groups == 1) return accumulate(weights.begin(), weights.end(), 0LL) == target;
    for (size_t size = 1; size <= weights.size(); size++) {
        for (const Group& group : groups_of_size(weights, size, target)) {
            if (can_split(without(weights, group), num_groups - 1, target)) return true;
        }
    }
    return false;
}

ll best_entanglement(const Group& weights, int num_groups) {
    ll target = accumulate(weights.begin(), weights.end(), 0LL) / num_groups;
    // Sizes go up, so the first size with a valid group has the fewest packages
    for (size_t size = 1; size <= weights.size(); size++) {
        vector<Group> groups = groups_of_size(weights, size, target);
        sort(groups.begin(), groups.end(), [](const Group& a, const Group& b) { return prod(a) < prod(b); });
        for (const Group& group : groups) {
            // The rest of the packages also have to split into equal groups
            if (can_split(without(weights, group), num_groups - 1, target)) return prod(group);
        }
    }
    return 0;
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    Group weights;
    for (const string& line : file_content) weights.push_back(stoll(line));

    ll part_1_res = best_entanglement(weights, 3);
    ll part_2_res = best_entanglement(weights, 4);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
