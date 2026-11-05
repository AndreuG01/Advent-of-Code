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

struct Reindeer {
    int speed, fly_time, rest_time;
    int distance = 0;
    int seconds_left;  // in the current state
    bool flying = true;
    int points = 0;
};

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    vector<Reindeer> results;
    for (const string& line : file_content) {
        vector<string> elems = split(line);
        Reindeer reindeer;
        reindeer.speed = stoi(elems[3]);
        reindeer.fly_time = stoi(elems[6]);
        reindeer.rest_time = stoi(elems[elems.size() - 2]);
        reindeer.seconds_left = reindeer.fly_time;
        results.push_back(reindeer);
    }

    const int N = 2503;
    int max_val = 0;

    for (int i = 0; i < N; i++) {
        for (Reindeer& reindeer : results) {
            if (reindeer.flying) reindeer.distance += reindeer.speed;
            reindeer.seconds_left -= 1;

            if (reindeer.seconds_left == 0) {
                // Switch between flying and resting
                reindeer.flying = !reindeer.flying;
                reindeer.seconds_left = reindeer.flying ? reindeer.fly_time : reindeer.rest_time;
            }
        }
        max_val = 0;
        for (const Reindeer& reindeer : results) max_val = max(max_val, reindeer.distance);
        for (Reindeer& reindeer : results) {
            if (reindeer.distance == max_val) reindeer.points += 1;
        }
    }

    int part_1_res = max_val;
    int part_2_res = 0;
    for (const Reindeer& reindeer : results) part_2_res = max(part_2_res, reindeer.points);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
