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

// C++ has no JSON in its standard library, so here is a small parser for what the input uses
struct Value {
    enum Type { NUMBER, STRING, ARRAY, OBJECT } type;
    ll number = 0;
    string text;
    vector<Value> children;  // array elements or object values
};

Value parse_value(const string& s, size_t& i);

string parse_string(const string& s, size_t& i) {
    size_t end = s.find('"', i + 1);
    string text = s.substr(i + 1, end - i - 1);
    i = end + 1;
    return text;
}

Value parse_value(const string& s, size_t& i) {
    Value value;
    if (s[i] == '[' || s[i] == '{') {
        bool is_object = s[i] == '{';
        char closing = is_object ? '}' : ']';
        value.type = is_object ? Value::OBJECT : Value::ARRAY;
        i += 1;
        while (s[i] != closing) {
            if (s[i] == ',') i += 1;
            if (is_object) {
                parse_string(s, i);  // the key
                i += 1;              // the colon
            }
            value.children.push_back(parse_value(s, i));
        }
        i += 1;
    } else if (s[i] == '"') {
        value.type = Value::STRING;
        value.text = parse_string(s, i);
    } else {
        value.type = Value::NUMBER;
        size_t used;
        value.number = stoll(s.substr(i, 20), &used);
        i += used;
    }
    return value;
}

ll sum_numbers(const Value& obj, bool ignore_red = false) {
    // Walk the JSON recursively and add up every number found
    if (obj.type == Value::NUMBER) return obj.number;
    if (obj.type == Value::STRING) return 0;
    if (obj.type == Value::OBJECT && ignore_red) {
        // Part 2: skip any object (not array) that has "red" as a value
        for (const Value& child : obj.children) {
            if (child.type == Value::STRING && child.text == "red") return 0;
        }
    }
    ll total = 0;
    for (const Value& child : obj.children) total += sum_numbers(child, ignore_red);
    return total;
}

int main(int argc, char** argv) {
    string file_content = read_text(argv[1]);

    size_t i = 0;
    Value json_obj = parse_value(file_content, i);

    ll part_1_res = sum_numbers(json_obj);
    ll part_2_res = sum_numbers(json_obj, true);

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
