class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        for(const auto& num: nums){
            if(seen.find(num) != seen.end()){
                seen[num]++;
            }
            else{
                seen[num] = 1;
            }
        }
        vector<int> o;
        for (int i = 0; i < k; ++i){
            auto max = max_element(seen.begin(), seen.end(), [] (const auto& p1, const auto& p2) {
                return p1.second < p2.second;  
        });
        o.push_back(max->first);
        seen[max->first] = 0;
        }
        return o;
    }
};
