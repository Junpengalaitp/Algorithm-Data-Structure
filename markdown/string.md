### LC 686. Repeated String Match
* repeated length upper bound is (len(a) + len(b)) * 2
* check if all the chars in b are presented in a first


### LC 28. Implement strStr()
* O(n), loop from 0 to haystack length - needle length(inclusive), and check substring(i, i + needle length) equals to needle


### LC 344. Reverse String
* loop half the array and swap

### LC 161. One Edit Distance
* base case: if two string's length diff larger than 1, return false
* loop two strings, when the chars are different, if they have same length, return the remaining substring are equal
* if they have different length, return s.substring(i) equals to t.substring(i + 1)
* in the end, return the lengths diff is 1