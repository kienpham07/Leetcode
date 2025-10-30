#Question 49 (Leetcode): Group Anagrams - Solution 2 - Optimal
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for w in strs:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1

            key = tuple(freq)
            hash_map[key].append(w)  # {A: [cat, tac],
                                     #   B: [bat, tab], ... }
                                     # A and B are frequency of letters
        return list(hash_map.values())