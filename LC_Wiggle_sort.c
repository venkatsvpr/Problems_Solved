// Wiggle Sort
void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    return;
}
void wiggleSort(int *nums, int numsSize) 
{
    int temp;
    int flag =1;
    if (numsSize <=1)
        return;
    
    for (int i= 0; i < numsSize-1; i++)
    {
        if (flag == 1)
        {
            if (nums[i] > nums[i+1])
            {
                swap((int *)(&nums[i]), (int *)(&nums[i+1]));
            }
            flag = 2;
        }
        else
        {
            if (nums[i] < nums[i+1])
            {
                swap((int *)(&nums[i]), (int *)(&nums[i+1]));
            }
            flag = 1; 
        }
    }
    return;
}
