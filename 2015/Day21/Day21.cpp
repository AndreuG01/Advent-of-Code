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

struct Item {
    int cost, damage, armor;
};

bool player_wins(int player_hp, int player_damage, int player_armor, int boss_hp, int boss_damage, int boss_armor) {
    while (true) {
        boss_hp -= max(1, player_damage - boss_armor);
        if (boss_hp <= 0) return true;
        player_hp -= max(1, boss_damage - player_armor);
        if (player_hp <= 0) return false;
    }
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    vector<int> boss;
    for (const string& line : file_content) boss.push_back(stoi(line.substr(line.find(": ") + 2)));
    int boss_hp = boss[0], boss_damage = boss[1], boss_armor = boss[2];

    vector<Item> weapons = {{8, 4, 0}, {10, 5, 0}, {25, 6, 0}, {40, 7, 0}, {74, 8, 0}};
    vector<Item> armors = {{13, 0, 1}, {31, 0, 2}, {53, 0, 3}, {75, 0, 4}, {102, 0, 5}};
    vector<Item> rings = {{25, 1, 0}, {50, 2, 0}, {100, 3, 0}, {20, 0, 1}, {40, 0, 2}, {80, 0, 3}};

    // Exactly 1 weapon, 0 or 1 armor, 0 to 2 rings
    vector<vector<Item>> armor_options = {{}};
    for (const Item& armor : armors) armor_options.push_back({armor});
    vector<vector<Item>> ring_options = {{}};
    for (size_t i = 0; i < rings.size(); i++) {
        ring_options.push_back({rings[i]});
        for (size_t j = i + 1; j < rings.size(); j++) ring_options.push_back({rings[i], rings[j]});
    }

    int part_1_res = INT32_MAX;
    int part_2_res = 0;

    for (const Item& weapon : weapons) {
        for (const vector<Item>& armor_option : armor_options) {
            for (const vector<Item>& ring_option : ring_options) {
                vector<Item> items = {weapon};
                items.insert(items.end(), armor_option.begin(), armor_option.end());
                items.insert(items.end(), ring_option.begin(), ring_option.end());

                int cost = 0, damage = 0, armor = 0;
                for (const Item& item : items) {
                    cost += item.cost;
                    damage += item.damage;
                    armor += item.armor;
                }
                if (player_wins(100, damage, armor, boss_hp, boss_damage, boss_armor)) part_1_res = min(part_1_res, cost);
                else part_2_res = max(part_2_res, cost);
            }
        }
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
