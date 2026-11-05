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

// C++ has no MD5 in its standard library, so here is a small one
array<uint8_t, 16> md5(const string& message) {
    static const uint32_t S[64] = {
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
    };
    static uint32_t K[64];
    static bool ready = false;
    if (!ready) {
        for (int i = 0; i < 64; i++) K[i] = (uint32_t)(4294967296.0 * abs(sin((double)(i + 1))));
        ready = true;
    }

    string data = message;
    uint64_t bit_length = (uint64_t)message.size() * 8;
    data.push_back((char)0x80);
    while (data.size() % 64 != 56) data.push_back(0);
    for (int i = 0; i < 8; i++) data.push_back((char)((bit_length >> (8 * i)) & 0xff));

    uint32_t a0 = 0x67452301, b0 = 0xefcdab89, c0 = 0x98badcfe, d0 = 0x10325476;
    for (size_t chunk = 0; chunk < data.size(); chunk += 64) {
        uint32_t M[16];
        memcpy(M, data.data() + chunk, 64);
        uint32_t A = a0, B = b0, C = c0, D = d0;
        for (int i = 0; i < 64; i++) {
            uint32_t F;
            int g;
            if (i < 16) { F = (B & C) | (~B & D); g = i; }
            else if (i < 32) { F = (D & B) | (~D & C); g = (5 * i + 1) % 16; }
            else if (i < 48) { F = B ^ C ^ D; g = (3 * i + 5) % 16; }
            else { F = C ^ (B | ~D); g = (7 * i) % 16; }
            F = F + A + K[i] + M[g];
            A = D;
            D = C;
            C = B;
            B = B + ((F << S[i]) | (F >> (32 - S[i])));
        }
        a0 += A;
        b0 += B;
        c0 += C;
        d0 += D;
    }

    array<uint8_t, 16> digest;
    memcpy(digest.data(), &a0, 4);
    memcpy(digest.data() + 4, &b0, 4);
    memcpy(digest.data() + 8, &c0, 4);
    memcpy(digest.data() + 12, &d0, 4);
    return digest;
}

int main(int argc, char** argv) {
    string file_content = read_text(argv[1]);

    int part_1_res = 0;
    int part_2_res = 0;
    bool part_1_done = false;

    int count = 1;
    while (true) {
        array<uint8_t, 16> res = md5(file_content + to_string(count));
        // Each byte is two hex digits
        bool five_zeros = res[0] == 0 && res[1] == 0 && res[2] < 16;
        bool six_zeros = res[0] == 0 && res[1] == 0 && res[2] == 0;
        if (five_zeros && !part_1_done) {
            part_1_res = count;
            part_1_done = true;
        }
        if (six_zeros) {
            part_2_res = count;
            break;
        }
        count += 1;
    }

    cout << "Part 1 res: " << part_1_res << '\n';
    cout << "Part 2 res: " << part_2_res << '\n';
}
