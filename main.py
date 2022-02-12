def merge(nums1, m, nums2, n):
    if m != len(nums1):
        while len(nums1) != m:
            del nums1[-1]
    elif n != len(nums2):
        while len(nums2) != n:
            del nums2[-1]

    if not nums1 or not nums2:
        if not nums1:
            for key, value in enumerate(nums2):
                nums1.append(nums2[key])

    elif nums1[0] > nums2[0]:
        dede = nums1[:m]
        while len(nums1) != 0:
            for key, value in enumerate(nums1):
                del nums1[key]
        while m + n != len(nums1):
            for key, value in enumerate(nums2):
                nums1.append(nums2[key])
            for key, value in enumerate(dede):
                nums1.append(dede[key])
        for key, value in enumerate(nums1[:-1]):
            if nums1[key] > nums1[key + 1]:
                x = nums1[key]
                nums1[key] = nums1[key + 1]
                nums1[key + 1] = x
            for key, value in enumerate(nums1[:-1]):
                if nums1[key] > nums1[key + 1]:
                    x = nums1[key]
                    nums1[key] = nums1[key + 1]
                    nums1[key + 1] = x
    else:
        while m + n != len(nums1):
            for key, value in enumerate(nums2):
                nums1.append(nums2[key])
        for key, value in enumerate(nums1[:-1]):
            if nums1[key] > nums1[key + 1]:
                x = nums1[key]
                nums1[key] = nums1[key + 1]
                nums1[key + 1] = x
            for key, value in enumerate(nums1[:-1]):
                if nums1[key] > nums1[key + 1]:
                    x = nums1[key]
                    nums1[key] = nums1[key + 1]
                    nums1[key + 1] = x


class Solution(object):
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    print(nums1)
