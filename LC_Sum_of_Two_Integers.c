/*
sum = a ^ b
carry = a & b
*/
int getSum(int a, int b) 
{
    int sum = a;
    
    while (b != 0)
    {
        sum = a^b;
        b = (a&b)<<1;
        a = sum;
    }

    return sum;
}
