#define pi pair<int, int>
#define pdi pair<double, int>

#pragma GCC optimize("O3", "unroll-loops")
auto _=[]()noexcept{ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);return 0;}();

class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pdi> rate(n);

        for(int i=0; i<n; i++) {
            rate[i] = {((double)wage[i])/quality[i], quality[i]};
        }

        sort(rate.begin(), rate.end());

        double mon = DBL_MAX;

        priority_queue<int> pq;
        int kQSum = 0;

        for(int i=0; i<k-1; i++) {
            pq.push(rate[i].second);
            kQSum += rate[i].second;
        }

        for(int i=k-1; i<n; i++) {
            pq.push(rate[i].second);
            kQSum += rate[i].second;
            if(pq.size()>k) {
                kQSum -= pq.top();
                pq.pop();
            }
            mon = min(mon, rate[i].first*kQSum);
        }

        return mon;
    }
};