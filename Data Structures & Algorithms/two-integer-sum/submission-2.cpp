class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> differences;
        for (int i = 0; i < nums.size(); ++i){
            int diff = target - nums[i];
            if (differences.find(diff) != differences.end()){
                vector<int> result = {differences[diff], i};
                return result;
            }
            else{
                differences[nums[i]] = i;
            }
        }
    }
};
