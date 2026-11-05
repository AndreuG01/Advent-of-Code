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

    vector<int> nums;
    for (const string& line : file_content) {
        for (const string& elem : split(line)) nums.push_back(stoi(elem));
    }

    int part_1_res = 0;
    int part_2_res = 0;

    int target = string(argv[1]).find("example") != string::npos ? 25 : 150;

    // Each bit of mask says if a container is used, so same-size containers stay different.
    // ways[size] counts the matching groups with that many containers.
    vector<int> ways(nums.size() + 1, 0);
    for (int mask = 1; mask < (1 << nums.size()); mask++) {
        int total = 0;
        int size = 0;
        for (size_t i = 0; i < nums.size(); i++) {
            if (mask & (1 << i)) {
                total += nums[i];
                size += 1;
            }
        }
        if (total == target) ways[size] += 1;
    }

    for (int curr_res : ways) {
        part_1_res += curr_res;
        // Part 2: sizes go up, so the first size with a match is the minimum
        if (part_2_res == 0) part_2_res = curr_res;
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
