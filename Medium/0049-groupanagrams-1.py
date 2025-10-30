#Question 49 (Leetcode): Group Anagrams - Solution 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_word = []
        for word in strs:
            sort_letter = "".join(sorted(word))
            sort_word.append(sort_letter)

        hash_map = {}  # value: index
        result = []
        for i in range(len(strs)):
            key = sort_word[i]
            if key in hash_map:
                result[hash_map[key]].append(strs[i])
            else:
                result.append([strs[i]])
                hash_map[key] = len(result) - 1
        return result