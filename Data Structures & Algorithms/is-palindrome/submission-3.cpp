class Solution {
public:
    bool isPalindrome(string s) {
        s.erase(remove_if(s.begin(), s.end(), [] (char c) {
            return !isalnum(c);
        }), s.end());
        if (s.empty()){
            return true;
        }
        for (int i = 0; i <= s.length() / 2; ++i){
            if (tolower(s.at(i)) != tolower(s.at(s.length()-i-1))){
                return false;
            }
        }
        return true;
    }
};
