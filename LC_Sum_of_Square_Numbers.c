/* Sum of Square Numbers
 * https://leetcode.com/problems/sum-of-square-numbers/description/
 */
long int find_binary (long int num)
{
    if (num == 1)
        return 1;
    long int start,end,mid;
    start = 1;
    end = num;
    
    while(start<end)
    {
        mid = (start + end)/2;
        
        if (mid*mid == num)
        {
            return mid;
        }
        else if (mid*mid > num)
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
bool judgeSquareSum(long int c) 
{
    if (c == 0)
        return 1;
    for (long int i = 1; i*i<=c; i++)
    {
        long int answer =find_binary (c - (i*i));
        if (0 == (c - (i*i)))
            return 1;
        if (answer > 0)
            return 1;
    }
    return 0;
}
