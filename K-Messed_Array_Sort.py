"""
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        1 ≤ arr.length ≤ 100

    [input] integer k
        1 ≤ k ≤ 20

    [output] array.integer
"""
import Queue as q
def sort_k_messed_array(arr, k):
  # Nsqur or N log N
  # create a heap of size k
  # loop element by eelemt in arr:
  # when we reach size k in the heap. pop the mini elemen
  minheap  = q.PriorityQueue()
  Output = []
  for index,element in enumerate(arr):
    minheap.put(element)
    if (index >=k ):
      Output.append(minheap.get())
  count = 0
  while (count < k):
    Output.append(minheap.get())
    count += 1
  return Output
