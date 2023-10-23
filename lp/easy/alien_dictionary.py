class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {c: i for i, c in enumerate(order)}


        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]

            for j in range(len(w1)):
                # if we reached end of w2 and we are still in bounds for w1, return False
                # that means w2 is a prefix of w1 which is not allowed
                if j == len(w2):
                    return False

                # if character at same index are not, same compare order and break
                # if we don't break, we will keep checking if next index at both words are in order - which is wrong logic
                if w1[j] != w2[j]:
                    if hmap[w1[j]] > hmap[w2[j]]:
                        return False
                    break
                  
        return True
    
# TC: O(len of all characters in words)
# SC: O(1)