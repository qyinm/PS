#include<iostream>
#include<queue>
#include<algorithm>
#include<set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);


    int tc;
    cin >> tc;

    for(int t = 0; t < tc; t++) {
        int len_input;
        multiset<int> q;

        char oper;
        int data;
        int all_data = 0;
        cin >> len_input;
       

        for(int iter = 0; iter < len_input; iter++) {
            cin >> oper >> data;
            
            if (oper == 'I') {
                all_data++;
                q.insert(data);
            }

            if (oper == 'D') {
                if (all_data == 0) {
                    continue;
                }
                all_data--;
                if (data == -1) {
                    q.erase(q.begin());
    
                } else if (data == 1) {
                    q.erase(--q.end());
                }
            }
        }


        if (all_data != 0) {
            cout << *(--q.end()) << " " << *q.begin() << "\n";
        } else {
            cout << "EMPTY\n";
        }
    }
}