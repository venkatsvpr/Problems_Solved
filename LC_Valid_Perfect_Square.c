/* Valid Perfect Square
 * 
 * https://leetcode.com/problems/valid-perfect-square/description/
 *
 * Start at the middle element and do binary search.
 * We can reach O(log n)
 */
bool isPerfectSquare(long int num) 
{
    if (num == 1)
        return 1;
    
    long int start,end,mid,prod;
    start = 1;
    end = num;
    
    while (start<end)
    {
        mid = (start + end)/2;
        prod = mid * mid;
        if (prod == num)
        {
            return 1;
        }
            
        if (prod > num)
        {
            end = mid;
        }
        else
        {
            start = mid+1;
        }
    }
    return 0;
}   
