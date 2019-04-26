def find(sou, target):
    left = 0
    right = len(sou) - 1
    mid = (left + right) // 2
    while left <= right:
        if sou[left] == target:
            return left
        if sou[right] == target:
            return right
        if sou[mid] == target:
            return mid
        if sou[left] < sou[mid]:
            if sou[left] < target < sou[mid]:
                left += 1
                right = mid - 1
            else:
                left = mid + 1
                right -= 1
        else:
            if target > sou[left] or target < sou[right]:
                left += 1
                right = mid - 1
            else:
                left = mid + 1
                right -= 1
        mid = (left+right)//2
    return -1


a = [8, 10, 20, 1, 3, 5, 6]
# print(find(a,))
