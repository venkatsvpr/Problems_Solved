"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""
# Function to return max sum such that
# no two elements are adjacent
def find_max_sum(arr):
  inc = arr[0]
  exc = 0
  for i in range(1,len(arr)):
	  inc,exc = max(inc,exc+arr[i]), max(inc,exc)
  return max(inc,exc)
# Driver program to test above function
arr = [1, 10, 3]
print (find_max_sum(arr))

# This code is contributed by Kalai Selvan
