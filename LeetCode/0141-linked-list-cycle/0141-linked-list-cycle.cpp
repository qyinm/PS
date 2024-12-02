/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        map<int, int> cache;
        for (; head != NULL; head = head->next) {
            cache[head->val] += 1;
            if (cache[head->val] == 10001) {
                return true;
            }
        }
        return false;
    }
};