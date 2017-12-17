/* Median of two sorted array. 
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 */
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) 
{
    int middle1, middle2;
    middle1 = middle2 = 0;
    if ((nums1Size + nums2Size)%2 == 0)
    {
        middle1 = ((nums1Size + nums2Size)/2)-1;
        middle2 = middle1 + 1;
    }
    else
    {
        middle1 = ((nums1Size + nums2Size)/2);
    }
    
    int elem1,elem2;
    
    int i,j,k;
    elem1 = elem2 =0;
    i = j = k =0;
    int count = 0;
    for (;;)
    {
 #       printf("count %d middle1 :%d middle2 %d elem1 %d elem2 %d i %d j %d num1size %d num2size %d\r\n",count,middle1,middle2,elem1,elem2,i,j,nums1Size,nums2Size);

        if (count > middle1)
        {
            if (middle2 == 0)
            {
      #          printf ("break 1\r\n");
                break;
            }
        }
        
        if (middle2)
        {
            if(middle2 < count)
            {
                #printf ("break 2\r\n");
                break;
            }
        }
        
       
        if (i == nums1Size)
        {
          #  printf ("check 1 \r\n");
            if (count == middle1)
            {
                elem1 = nums2[j];
            }
            else if (middle2 &&
                    (count == middle2))
            {
                elem2 = nums2[j];
            }
            j++;
            count++;
            continue;
        }
        else if (j == nums2Size)
        {
          #  printf ("num1 less than num2 \r\n");
            if (count == middle1)
            {
                elem1 = nums1[i];
            }
            else if (middle2 &&
                    (count == middle2))
            {
                elem2 = nums1[i];
            }
            i++;
            count++;
            continue;
            
        }
        else if (nums1[i]<nums2[j])
        {
         #   printf ("num1 less than num2 \r\n");
            if (count == middle1)
            {
                elem1 = nums1[i];
            }
            else if (middle2 &&
                    (count == middle2))
            {
                elem2 = nums1[i];
            }
            i++;
            count++;
            continue;
        }
        else if (nums2[j]<=nums1[i])
        {
          #  printf (" elese 3\r\n");
            if (count == middle1)
            {
                elem1 = nums2[j];
            }
            else if (middle2 &&
                    (count == middle2))
            {
                elem2 = nums2[j];
            }
            j++;
            count++;
        }
    }
   # printf ("elem1:%d elem2:%d middle1:%d middle2:%d\r\n",elem1, elem2, middle1, middle2);
    if (middle2 == 0)
    {
        return elem1;
    }
    
    return ((double)(elem1+elem2)/2);
}
