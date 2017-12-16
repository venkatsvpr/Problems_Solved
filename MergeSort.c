/* Simple Merge Sort LOGIC */
#include <stdio.h>
#include <stdlib.h>

void
Merge (int arr[], int left, int right, int mid)
{
    int i,j,k;
    int left_size = mid - left + 1;
    int right_size = right - mid;

    int *L = (int *) malloc (sizeof(left_size));
    int *R = (int *) malloc (sizeof(right_size));

    for (i=0; i<left_size; i++)
        L[i] = arr[left+i];

    for (i=0; i<right_size; i++)
        R[i] = arr[mid + 1 + i];

    i = 0; 
    j = 0;
    k = left;

    while ( i<left_size  && j<right_size)
    {
        if (L[i] <= R[j])
        {
            arr[k++] = L[i++];
        }
        else
        {
            arr[k++] = R[j++];
        }
    
    }
    
    /* Copy the remaining of left partition if any */
    while (i<left_size)
    {
        arr[k++] = L[i++];
    }

    
    while (j<right_size)
    {
        arr[k++] = R[j++];
    }
    return;
}

void MergeSort (int arr[], int left, int right)
{
    if (left < right)
    {
        int mid = (left + right -1) /2;
        MergeSort (arr, left, mid);
        MergeSort (arr, mid+1, right);
        Merge (arr, left, right, mid);  
    }
    return;
}

void PrintArray (int *a, int size)
{
    printf ("\r\nPrinting Array..\r\n");
    for (int i = 0; i <size; i++)
    {
        printf ("%d ",a[i]);
    }
    return;
}

int main()
{
    int arr[] = { 2.8, 1,10,3, 14,16,6};
    int size_arr = sizeof (arr)/sizeof(arr[0]);

    printf (" Before Sorting .. \r\n");
    PrintArray (arr, size_arr);
    
    MergeSort(arr, 0, size_arr-1);
    PrintArray (arr, size_arr);
    return 0;
}
