from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0
        for w in words:
            chars_count = Counter(chars)

            isSub = True
            for c in w:
                if c not in chars_count or chars_count[c] == 0:
                    isSub = False
                    break

                chars_count[c] -= 1

            if isSub:
                res += len(w)
            
        return res