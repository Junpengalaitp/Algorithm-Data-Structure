### LC 91. Decode Ways
* base case 1: if the string is empty, return 1
* base case 2: if the string starts with 0, return 0
* decode 1: recurse on substring(1)
* decode 2: recurse on substring(2) if the number is larger than 26, else is 0
* total ways = decode 1 + decode 2
* use cache to reduce duplicated calculation
