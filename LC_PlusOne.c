/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) 
{
    int to_add = 0;
    int carry = 0;
    for (int i=digitsSize-1; i>=0; i--)
    {
        if (i == digitsSize-1)
        {
            to_add =1;
        }
        else
        {
            to_add =0;
        }
        
      // printf ("<%d>:%d carry:%d \r\n",i,digits[i],carry);
        if (digits[i] == 9)
        {
            if (to_add == 1)
            {
                digits[i] = 0;
                carry = 1;
            }
            else if (carry == 1)
            {
                digits[i]=0;
                carry =1;
            }
                
        }
        else
        {
            digits[i] = digits[i]+to_add+carry;
            carry = 0;
            
        }
      // printf ("<digit is :%d> carry:%d \r\n",digits[i],carry);
    }
    int *number;
    if (carry==1)
    {
        number = (int *) malloc(sizeof(int)*digitsSize+1);
        number[0]= carry;
        for (int i=0;i<digitsSize; i++)
            number[i+1] = digits[i];
        *returnSize = digitsSize + 1;
    }
    else
    {
        number = (int *) malloc(sizeof(int)*digitsSize+1);
        for (int i=0;i<digitsSize; i++)
            number[i] = digits[i];
        *returnSize = digitsSize;
    }
    return number;
}
