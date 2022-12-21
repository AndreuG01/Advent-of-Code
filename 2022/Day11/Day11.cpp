#include <bits/stdc++.h>
#include <regex>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<int, int> vii;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair

#define endl '\n'
#define len(s) (int)s.size()
#define print(x) cout<<x<<'\n';
#define REP(i, a, b) for (int i = 0; i <= b; i++)
#define all(a) (a).begin(), (a).end()
#define print_big(x) cout << fixed << setprecision(0) << x << endl;
#define line(x) getline(cin, x)
#define string_lowercase(s) transform(s.begin(), s.end(), s.begin(), ::tolower);
#define char_tolower(c) if ('a' <= c && c <= 'z') c += 32
#define char_toupper(c) if ('a' <= c && c <= 'z') c -= 32

#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

ll mod = 1000000007;

#define MULT 0
#define ADD 1
#define DIVIDE 2
#define SUB 3

class Monkey {
    public:
        vector<ll> items;
        int operation;
        int true_dest;
        int false_dest;
        int divisible_test;
        ll worry_level;

        bool op1_old, op2_old;
        int op1, op2;

        int inspect_items = 0;

        void add_items(string &item_str) {
            vector<string> res = split(item_str, ',');
            
            for (auto num : res) {
                items.PB(stoll(num));
            }
            this->worry_level = items[0];
        }

        void add_operation(string &operation_str) {
            vector<string> result = split(operation_str, ' ');
            
            char op = result[3].at(0);
            switch (op) {
                case '+':
                    operation = ADD;
                    break;
                case '-':
                    operation = SUB;
                    break;
                case '*':
                    operation = MULT;
                    break;
                default:
                    break;
            }

            if (result[2] == "old") {
                op1_old = true;
            } else {
                op1_old = false;
                op1 = stoi(result[2]);
            }

            if (result[4] == "old") {
                op2_old = true;
            } else {
                op2_old = false;
                op2 = stoi(result[4]);

            }
        }

        ll compute_level() {
            switch (this->operation) {
                case ADD:
                    if (op1_old && op2_old) {
                        return worry_level + worry_level;
                    } else if (op1_old) {
                        // print(worry_level);
                        return worry_level + op2;
                    } else if (op2_old) {
                        return op1 + worry_level;
                    } else {
                        return op1 + op2;
                    }
                case MULT:
                    if (op1_old && op2_old) {
                        return worry_level * worry_level;
                    } else if (op1_old) {
                        return worry_level * op2;
                    } else if (op2_old) {
                        return op1 * worry_level;
                    } else {
                        return op1 * op2;
                    }
            }
            return 0;
        }

        void set_true_dest(int true_dest) {
            this->true_dest = true_dest;
        }
        
        void set_false_dest(int false_dest) {
            this->false_dest = false_dest;
        }

        void set_divisible_test(int divisible) {
            this->divisible_test = divisible;
        }

        void set_worry_level(int level) {
            this->worry_level = level;
        }

    private:
        vector<string> split(const string& str, char delimiter) {
            vector<string> tokens;
            stringstream ss(str);
            string token;
            while (getline(ss, token, delimiter)) {
                tokens.push_back(token);
            }
            return tokens;
        }
};


void compute_monkeys(vector<Monkey> &monkeys, bool part_a) {
    int mod = 1;
    for (auto m : monkeys) {
        mod *= m.divisible_test;
    }

    int max_rounds = 10000;
    if (part_a) max_rounds = 20;

    for (int round = 1; round <= max_rounds; round++) {
        for (int i = 0; i < len(monkeys); i++) {
            Monkey curr_monkey = monkeys[i];
            for (int j = 0; j < len(curr_monkey.items); j++) {
                ll worry_level = curr_monkey.items[j];
                if (part_a) monkeys[i].set_worry_level(worry_level);
                else monkeys[i].set_worry_level(worry_level % mod);
                
                worry_level = monkeys[i].compute_level();
                if (part_a) worry_level /= 3;
                else worry_level = worry_level % mod;
                
                if (worry_level % monkeys[i].divisible_test == 0) {
                    monkeys[monkeys[i].true_dest].items.PB(worry_level);
                } else {
                    monkeys[monkeys[i].false_dest].items.PB(worry_level);
                }
                monkeys[i].inspect_items++;
            }
            monkeys[i].items = vector<ll>();   
        }
    }
}

ll get_solution(vector<Monkey> &monkeys) {
    ll max_1 = 0, max_2 = 0;
    for (int i = 0; i < len(monkeys); i++) {
        Monkey curr_monkey = monkeys[i];
        if (curr_monkey.inspect_items > max_1) {
            max_2 = max_1;
            max_1 = curr_monkey.inspect_items;
        } else if (curr_monkey.inspect_items > max_2) {
            max_2 = curr_monkey.inspect_items;
        }
    }
    
    return max_1 * max_2;
}


int main() {
    fast;
    string s;
    string operation_str, items_str;
    smatch match_item, match_operation, match_divisible, match_true, match_false;

    int divisible = 0;
    int true_dest = 0;
    int false_dest = 0;
    vector<Monkey> monkeys_a, monkeys_b;
    auto idx_items = regex("  Starting items: (.*)");
    auto operation = regex("  Operation: (.*)");
    auto divisible_regex = regex("  Test: divisible by ([0-9]+)");
    auto true_regex = regex("    If true: throw to monkey ([0-9]+)");
    auto false_regex = regex("    If false: throw to monkey ([0-9]+)");

    while (getline(cin, s)) {
        regex_match(s, match_item, idx_items);
        regex_match(s, match_operation, operation);
        regex_match(s, match_divisible, divisible_regex);
        regex_match(s, match_true, true_regex);
        regex_match(s, match_false, false_regex);
        
        if (match_item.str(0) != "") {
            items_str = match_item.str(1);
        } else if (match_operation.str(0) != "") {
            operation_str = match_operation.str(1);
        } else if (match_divisible.str(0) != "") {
            divisible = stoi(match_divisible.str(1));
        } else if (match_true.str(0) != "") {
            true_dest = stoi(match_true.str(1));
        } else if (match_false.str(0) != "") {
            false_dest = stoi(match_false.str(1));
            Monkey m;
            m.add_items(items_str);
            m.add_operation(operation_str);
            m.set_divisible_test(divisible);
            m.set_true_dest(true_dest);
            m.set_false_dest(false_dest);
            monkeys_a.PB(m);
            monkeys_b.PB(m);
        }   
    }


    compute_monkeys(monkeys_a, true);
    compute_monkeys(monkeys_b, false);

    
    ll sol_a, sol_b;
    sol_a = get_solution(monkeys_a);
    sol_b = get_solution(monkeys_b);

    printf("Res part a: %lld\n", sol_a);
    printf("Res part b: %lld\n", sol_b);
    
    return 0;
}