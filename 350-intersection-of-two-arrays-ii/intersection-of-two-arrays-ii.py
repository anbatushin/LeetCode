class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct1 = {}
        res = []
        for elem in nums1:
            dct1[elem] = dct1.get(elem, 0) + 1
        for elem in nums2:
            if dct1.get(elem, 0) > 0:
                res.append(elem)
                dct1[elem] -= 1
        return res