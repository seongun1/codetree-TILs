#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool is_balanced_and_valid(const string &s) {
    int balance = 0;
    for (char c : s) {
        if (c == '(') {
            balance++;
        } else {
            balance--;
        }
        if (balance < 0) {
            return false;
        }
    }
    return balance == 0;
}

int main() {
    string tmp;
    cin >> tmp;

    int cnt = 0;
    for (size_t i = 0; i < tmp.size(); ++i) {
        char original = tmp[i];
        tmp[i] = (tmp[i] == '(') ? ')' : '(';  // Flip the bracket
        if (is_balanced_and_valid(tmp)) {
            cnt++;
        }
        tmp[i] = original;  // Restore the original bracket
    }

    cout << cnt << endl;
    return 0;
}