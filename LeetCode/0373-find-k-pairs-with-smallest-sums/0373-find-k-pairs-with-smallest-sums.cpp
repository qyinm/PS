#include <queue>
#include <tuple>
#define tiii tuple<int, int, int>
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<tiii, vector<tiii>, greater<>> pq;
        vector<vector<int>> answer;
        for (int i = 0; i < nums2.size() && i < k; i++) {
            pq.push({nums1[0] + nums2[i], 0, i});
        }

        while (!pq.empty() && answer.size() < k) {
            auto [sum, one, two] = pq.top();
            pq.pop();
            answer.push_back({nums1[one], nums2[two]});

            if (one + 1 < nums1.size()) {
                pq.push({nums1[one+1] + nums2[two], one+1, two});
            }
        }
        return answer;
    }
};