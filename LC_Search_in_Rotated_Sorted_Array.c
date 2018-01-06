/* Search in Rotate Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * One half is sorted. If it is in the range search there else search onthe other side.
 * Do this like binary search. O(log n) 
 */
int search(int* nums, int numsSize, int target) 
{
    if (numsSize == 0)
    {
        return -1;  
    }
    int start,end,mid;
    start = 0;
    end = numsSize-1;
    mid = 0;
    while (1)
    {
        if (start > end)
        {
            break;
        }
        
        mid = (start + end)/2;
        
        if (nums[mid] == target)
        {
            return (mid);
        }
        
        if (nums[start] <= nums[mid])
        {
            if ((nums[start] <= target) && (target <= nums[mid]))
            {
                end = mid;          
            }
            else
            {
                start = mid+1;
            }
            continue;
        }
        
        if (nums[mid+1] <= nums[end])
        {
            if ((nums[mid+1] <= target) && (target <= nums[end]))
            {
                start = mid+1;
            }
            else
            {
                end = mid;
            }
            continue;
        }  
    }
    return -1;
    
}
