def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    k = n + m
    is_even = False

    if k % 2 != 0:
        length = (k + 1) // 2
    else:
        length = (k // 2) + 1
        is_even = True


    i = 0
    j = 0
    new_list = []

    for o in range(length):
        if i < n:
            if j < m:
                if nums1[i] <= nums2[j]:
                    new_list.append(nums1[i])
                    i += 1
                else:
                    new_list.append(nums2[j])
                    j += 1
            else:
                new_list.append(nums1[i])
                i += 1
        else:
            new_list.append(nums2[j])
            j += 1

    return (new_list[length - 1] + new_list[length - 2]) / 2 if is_even else new_list[length - 1]
