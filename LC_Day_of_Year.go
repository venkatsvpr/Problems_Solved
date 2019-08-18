```
1154: Day of Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
```
func dayOfYear(date string) int {
    var count int64
    daysOfMonth := [] int64 {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    s := strings.Split(date,"-")
    month, _ := strconv.ParseInt(s[1], 10, 64)
    intDate, _ := strconv.ParseInt(s[2], 10, 64)
    intYear, _ := strconv.ParseInt(s[0], 10, 64)
    if (month > 2) && isLeap(intYear){
        count += 1
    }
    month -= 1
    for i  := int64(0); i < month; i++ {
        count += daysOfMonth[i]
    }
    count += int64(intDate)
    return int(count);
}

func isLeap(year int64) bool {
    if (year % 4 == 0){
        if (year %100 == 0){
            if (year % 400 == 0){
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    } else {
        return false;
    }
}