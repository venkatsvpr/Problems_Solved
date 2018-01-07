"""
Isomorphic String
Find the position of a string. The same character should  be present on other side aswell.
XYZZZ ABCCC - If we find Z, the last point should also be there.
"""
bool isIsomorphic(char* s, char* t) 
{
    if ((s == NULL) && (t == NULL))
        return 0;
    
    char *spt = s;
    char *tpt = t;
    while (*spt != NULL)
    {
        int s_pos = strchr(s,*spt++) - s;
        int t_pos = strchr(t,*tpt++) - t;
        if (s_pos != t_pos)
            return 0;
    }
    return 1;    
}
