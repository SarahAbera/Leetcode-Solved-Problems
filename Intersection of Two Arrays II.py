class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Count = Counter(nums1)
        nums2Count = Counter(nums2)

        answer = []
        for key,val in nums1Count.items():
            if key in nums2Count:
                intersect = min(val,nums2Count[key])
                for _ in range(intersect):
                    answer.append(key)

        return answer
