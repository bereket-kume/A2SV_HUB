# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(idx):
            result = []
            while idx < len(s) and s[idx] != ']':
                if not s[idx].isdigit():
                    result.append(s[idx])
                    idx += 1
                else:
                    k = 0
                    while idx < len(s) and s[idx].isdigit():
                        k = k * 10 + int(s[idx])
                        idx += 1
                    idx += 1
                    decoded_string, idx = helper(idx)
                    idx += 1
                    result.append(decoded_string * k)
            return "".join(result), idx
        
        ans, _ = helper(0)
        return ans