class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int min = prices[0];
        
        for(int i = 0; i < prices.size(); i++) {
            if(prices[i] < min) {           // 최소값을 찾기
                min = prices[i];
            }

            if((prices[i] - min) > max) {   // 최대 이득 찾기
                max = prices[i] - min;
            }
        }

        return max;
    }
};