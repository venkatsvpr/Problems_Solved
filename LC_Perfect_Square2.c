# Perfect Square
# https://leetcode.com/problems/perfect-squares/
int numSquares(int n) 
{
    while (n % 4 != 0)
    {
        n = n/4;
    }
    
    if (n%8 == 7)
    {
        return 4;
    }

    int ub = sqrt(n);
    for (int a = 0; a <= ub; a++)
    {
        for (int b = a; b <=ub; b++)
        {
            int c =sqrt(n-(a*a) - (b*b));
            if ((a*a)+(b*b)+(c*c) == n)
                return !!a + !!b + !!c;
        }
    }
    return 4;
}
