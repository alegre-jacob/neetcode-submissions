class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> s;

        for (const auto& num : tokens) {
            if (num == "+" || num == "-" || num == "*" || num == "/") {
                int sec = s.top(); s.pop();
                int fir = s.top(); s.pop();

                if (num == "+") s.push(fir + sec);
                else if (num == "-") s.push(fir - sec);
                else if (num == "*") s.push(fir * sec);
                else if (num == "/") s.push(fir / sec);
            } else {
                s.push(std::stoi(num));
            }
        }
        
        int result = s.top();
        s.pop();
        return result;
    }
};