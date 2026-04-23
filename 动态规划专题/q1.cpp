#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int max_subarray(const vector<int>& nums) {
    int cur = nums[0];
    int ans = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        cur = max(cur + nums[i], nums[i]);
        ans = max(ans, cur);
    }
    return ans;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    cout << max_subarray(nums) << endl;
    return 0;
}