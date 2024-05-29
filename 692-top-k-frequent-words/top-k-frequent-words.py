class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dct = {}
        for word in words:
            dct[word] = dct.get(word, 0) + 1
        ans = sorted(dct.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in ans[:k]]
        