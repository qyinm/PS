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
        map<ListNode*, int> cache;
        for (; head != NULL; head = head->next) {
            cache[head] += 1;
            if (cache[head] == 2) {
                return true;
            }
        }
        return false;
    }
};