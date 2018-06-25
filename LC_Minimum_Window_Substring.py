def get_shortest_unique_substring(arr, str):
    def flush(level):
        print ("flush triggerd for ",level)
        count = 0
        for item in expect:
            if (expect[item] == -1):
                continue;
            if (expect[item] <= level):
                expect[item] = -1
                count += 1
        return count

    expect = dict()
    for item in arr:
      expect[item] = -1
      if (item not in str):
        return ""
    Shortest = str
    inc_count = 0
    for index,ch in enumerate(str):
        if (ch not in expect):
            continue
        if (expect[ch] == -1):
            expect[ch] = index
            inc_count += 1
        else:
            inc_count -= flush(expect[ch])
            if (inc_count < 0):
                inc_count = 0
            inc_count += 1
            expect[ch] = index
        print (expect)
        if (inc_count == len(arr)):
            print (expect)
            ma = float('-inf')
            mi = float('inf')
            for key in expect:
                mi = min (mi, expect[key])
                ma = max (ma, expect[key])
            print (mi,ma)
            if (ma-mi < len(Shortest)):
                Shortest = str[mi:ma+1]
    return Shortest
print (get_shortest_unique_substring(["x","y","z"], "xyyzyzyx"))
