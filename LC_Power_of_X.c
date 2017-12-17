/* Power x^n
 * https://leetcode.com/problems/powx-n/
 */
double myPow(double x, int n) 
{
    double answer=1;
    if (n == 0)
        return answer;
    
    answer = myPow (x, n/2);
    if (n%2 == 0)
        return answer*answer;
    else
    {
        if (n > 0)
            return x * answer * answer;
        else
            return (answer * answer)/x;
    }  
}
