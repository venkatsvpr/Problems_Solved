def substring_KMP (needle,haystack):
    fall_back  =  [0] * len(needle)
    i = 0
    j = i+1
    while (i <len(needle)) and (j < len(needle)):
        if (needle[i] == needle[j]):
            fall_back[j] = i+1
            i += 1
            j += 1
        else:
            if (i == 0):
                j += 1
            else:
                i  = fall_back[i-1]
    h_idx = n_idx = 0
    while (h_idx < len(haystack)) and (n_idx < len(needle)):
        if (haystack[h_idx] == needle[n_idx]):
            if (n_idx == (len(needle)-1)):
                return True
            h_idx += 1
            n_idx += 1
        elif (n_idx == 0):
            h_idx += 1
        else:
            n_idx = fall_back[n_idx-1]
    return False
