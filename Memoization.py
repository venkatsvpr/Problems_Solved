from time import gmtime, strftime
N = 40
X = [1,3,5]
def find_ways(N):
    if (N == 0):
        return 1
    elif (N < 0):
        return 0
    ct = 0
    for item in X:
        ct += find_ways(N-item)
    return ct

print ("Without Memoization")
print (strftime("start time %Y-%m-%d %H:%M:%S", gmtime()))
print (find_ways(N))
print (strftime("end time %Y-%m-%d %H:%M:%S", gmtime()))

def memo_find_ways(N):
    if N in d:
        return d[N]
    if (N == 0):
        d[0] = 1
        return 1
    elif (N < 0):
        return 0
    ans = 0
    for item in X:
        ans += memo_find_ways(N-item)
    d[N] = ans
    return ans

d = dict()
print ("With Memoization")
print (strftime("start time %Y-%m-%d %H:%M:%S", gmtime()))
print (memo_find_ways(N))
print (strftime("end time %Y-%m-%d %H:%M:%S", gmtime()))
