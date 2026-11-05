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

// spent, hp, mana, boss, shield, poison, recharge
typedef array<int, 7> State;

struct Spell {
    int cost, hp, boss, shield, poison, recharge;
};

// Effects at the start of a turn: returns the armor for this turn
int apply_effects(int& mana, int& boss, int& shield, int& poison, int& recharge) {
    int armor = shield > 0 ? 7 : 0;
    if (poison > 0) boss -= 3;
    if (recharge > 0) mana += 101;
    shield = max(shield - 1, 0);
    poison = max(poison - 1, 0);
    recharge = max(recharge - 1, 0);
    return armor;
}

vector<Spell> cast_spells(int hp, int mana, int boss, int shield, int poison, int recharge) {
    // Every spell that can be cast now
    vector<Spell> options = {
        {53, hp, boss - 4, shield, poison, recharge},      // Magic Missile
        {73, hp + 2, boss - 2, shield, poison, recharge},  // Drain
    };
    if (shield == 0) options.push_back({113, hp, boss, 6, poison, recharge});
    if (poison == 0) options.push_back({173, hp, boss, shield, 6, recharge});
    if (recharge == 0) options.push_back({229, hp, boss, shield, poison, 5});

    vector<Spell> affordable;
    for (const Spell& option : options) {
        if (option.cost <= mana) affordable.push_back(option);
    }
    return affordable;
}

int least_mana(int player_hp, int player_mana, int boss_hp, int boss_damage, bool hard = false) {
    // Dijkstra: always continue from the fight that has spent the least mana so far,
    // so the first won fight taken from the queue is the cheapest one
    priority_queue<State, vector<State>, greater<State>> queue;
    queue.push({0, player_hp, player_mana, boss_hp, 0, 0, 0});
    set<State> seen;

    while (!queue.empty()) {
        State state = queue.top();
        queue.pop();
        auto [spent, hp, mana, boss, shield, poison, recharge] = state;
        if (boss <= 0) return spent;
        if (!seen.insert(state).second) continue;

        // Player turn
        if (hard) {
            // Part 2: lose 1 HP at the start of each player turn, before effects
            hp -= 1;
            if (hp <= 0) continue;
        }

        apply_effects(mana, boss, shield, poison, recharge);
        if (boss <= 0) {
            queue.push({spent, hp, mana, boss, shield, poison, recharge});
            continue;
        }

        for (Spell spell : cast_spells(hp, mana, boss, shield, poison, recharge)) {
            // Boss turn
            int new_mana = mana - spell.cost;
            int armor = apply_effects(new_mana, spell.boss, spell.shield, spell.poison, spell.recharge);
            if (spell.boss > 0) {
                spell.hp -= max(1, boss_damage - armor);
                if (spell.hp <= 0) continue;
            }
            queue.push({spent + spell.cost, spell.hp, new_mana, spell.boss, spell.shield, spell.poison, spell.recharge});
        }
    }
    return -1;
}

// least_mana gives -1 when the fight can't be won
string show(int mana) {
    return mana == -1 ? "None" : to_string(mana);
}

int main(int argc, char** argv) {
    vector<string> file_content = read_lines(argv[1]);

    int boss_hp = stoi(file_content[0].substr(file_content[0].find(": ") + 2));
    int boss_damage = stoi(file_content[1].substr(file_content[1].find(": ") + 2));

    // The puzzle's examples use a weaker player
    bool is_example = string(argv[1]).find("example") != string::npos;
    int player_hp = is_example ? 10 : 50;
    int player_mana = is_example ? 250 : 500;

    string part_1_res = show(least_mana(player_hp, player_mana, boss_hp, boss_damage));
    string part_2_res = show(least_mana(player_hp, player_mana, boss_hp, boss_damage, true));

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
