class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sortedS = "".join(sorted(i))
            if sortedS not in seen:
                seen[sortedS] = []
            seen[sortedS].append(i)
        return list(seen.values())

