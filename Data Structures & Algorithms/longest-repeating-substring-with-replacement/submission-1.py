class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_count = collections.defaultdict(int)

        left = 0

        maxF = 0
        maxL = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            maxF = max(maxF, char_count[s[right]])

            windowL = right - left + 1

            charsReplace = windowL - maxF

            if charsReplace > k:
                char_count[s[left]] -= 1

                left = left + 1

            maxL = max(maxL, right - left + 1)

        return maxL
