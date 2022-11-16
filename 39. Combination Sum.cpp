class Solution
{
public:
    vector<vector<int>> ans;
    void solve(int i, vector<int> &arr, vector<int> &temp, int target)
    {
        if (target == 0)
            ans.push_back(temp);
        ;
        if (target < 0 || i == arr.size())
            return;

        solve(i + 1, arr, temp, target);
        temp.push_back(arr[i]);
        solve(i, arr, temp, target - arr[i]);
        temp.pop_back();
    }
    vector<vector<int>> combinationSum(vector<int> &arr, int target)
    {

        ans.clear();
        vector<int> temp;
        solve(0, arr, temp, target);
        ans.erase(unique(ans.begin(),ans.end()),ans.end());
        return ans;
    }
};