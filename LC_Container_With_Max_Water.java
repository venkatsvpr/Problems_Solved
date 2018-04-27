class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxarea = -1;
        while (left <right) {
            maxarea = Math.max(maxarea, (right - left)*Math.min(height[left],height[right]));
            /* Move left to the right when the height of left is less than right */
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return maxarea;
    }
}
