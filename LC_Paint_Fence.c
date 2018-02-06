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
   
    /* For same as  before its  k choices for previous and 1 choice for current
     * so 1*k = k
     */   
    same = k;
    /* For different previous can be choosen in k ways. But for the one choosen
     * current fence can be choosen in k-1 ways. So its k * (k-1)
     */
    diff = k*(k-1);
    
    prev_same = same;
    prev_diff = diff;
    
    /* If we plan to use the same as n-1th pole. n-1th and n-2nd pole should be different.
     * and we can just use the same color.  prev_diff * i
     * If we plan to uses a different color.
     * We can do it in k-1 way  over the n-th ways.
     * for n-1 th ways.. It is prev_same + prev_diff 
     * (prev_same + prev_diff ) * k-1
     */
    for (int i=3; i <=n; i++)
    {
        
        same = prev_diff;
        diff = (prev_same + prev_diff) * (k-1);
        prev_same = same;
        prev_diff = diff;
    }
 
    /* tota number of ways is the same + different */
    return (same+diff);
}
