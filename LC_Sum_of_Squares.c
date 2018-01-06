/*
 * Sum of Squares
 */
bool judgeSquareSum(int c) 
{
    if (c == 0)
        return 1;
    int ub  = sqrt(c);
    for (int i = 1; i<=ub; i++)
    {
        int b = sqrt(c - (i*i));
        if ((b*b + i*i) == c)
        {
            return 1;
        }
    }
    return 0;
}
