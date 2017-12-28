// Paint Fence
// https://leetcode.com/problems/paint-fence/description/
int numWays(int n, int k) 
{
    if ((n<=0) || (k<=0))
    {
        return 0;
    }
    
    if (n == 0)
        return 0;
    else if (n == 1)
        return k;
    
    int same,diff,prev_same,prev_diff;
    same = diff = prev_same = prev_diff = 0;
    
    same = k;
    diff = k*(k-1);
    
    prev_same = same;
    prev_diff = diff;
    
    for (int i=3; i <=n; i++)
    {
        same = prev_diff;
        diff = (prev_same + prev_diff) * (k-1);
        prev_same = same;
        prev_diff = diff;
    }
 
    return (same+diff);
}
