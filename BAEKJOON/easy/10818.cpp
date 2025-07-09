#include <iostream>
 
using namespace std;

int main() {
    int n;
    cin >> n;
    int min_num = 1000000, max_num = -1000000;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        if (num < min_num) {
            min_num = num;
        }
        if (num > max_num) {
            max_num = num;
        }
    }
    cout << min_num << " " << max_num << endl;
    return 0;
}