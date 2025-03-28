class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # create a table for memoization
        DPtable = {}
        str1_len = len(s) # column
        str2_len = len(t) # row
        # base cases
        for j in range(str1_len + 1):
            DPtable[(0, j)] = 1
        for i in range(1, str2_len + 1):
            DPtable[(i, 0)] = 0
    
        # fill in the table
        for i in range (1, str2_len + 1):
            for j in range(1, str1_len + 1):
                # if matching
                if (s[j-1] == t[i-1]):
                    DPtable[(i, j)] = DPtable[(i-1, j-1)] + DPtable[(i, j-1)]
                # if not matching
                else:
                    DPtable[(i, j)] = DPtable[(i, j-1)]

        return DPtable[(str2_len, str1_len)]

def main():
    num_test_cases= int(input())
    test_cases = []

    for _ in range(num_test_cases):
        strings_list = []
        str1, str2 = input().split()
        strings_list.append((str1, str2))

        test_cases.append(strings_list)

    sol = Solution()
    for case in test_cases:
        for str1, str2 in case:
            print(sol.numDistinct(str1, str2))
        
main()

