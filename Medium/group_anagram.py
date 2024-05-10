class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for word in strs:
            count = [0] * 26

            for s in word:
                count[ord(s) - ord("a")] += 1

            if tuple(count) not in temp:
                temp[tuple(count)] = [word]

            else:
                temp[tuple(count)].append(word)

        return temp.values()
