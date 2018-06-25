"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
Input =[5, 1, 1, 5]
incl = Input[0] 
excl = 0
for i in range(1,len(Input)):
    prev_inc = incl
    incl = max(incl,excl+Input[i])
    excl = max(prev_inc,excl)
print (max(incl,excl))
