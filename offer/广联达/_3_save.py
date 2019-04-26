# 有点类似哈夫曼树
def fun(people, limit):
    # 考虑边界
    if len(people) == 0 or not people:
        return 0
    if len(people) == 1 and limit > people[0]:
        return 1
    people.sort()  # 先排序
    if people[-1] > limit:
        return -1
    # print(people)
    cnt = 0
    index = 0
    while index < len(people):
        if index == len(people) - 1:
            cnt += 1
            break
        if people[index] + people[index + 1] <= limit:
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    return cnt


if __name__ == "__main__":
    print(fun([3, 1, 1, 2], 3))
    print(fun([3, 4, 3, 5], 5))
