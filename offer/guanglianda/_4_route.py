def route_r(house, route):
    if len(house) == 0:
        return None
    # 需要归并，将 route 的节点插入已经排好序的 house 中，判断前后距离，取最大。
    # 最大值更新到 全局变量中取最大
    house.sort()  # 如果不是按顺序需要先进行排序
    # 想的暴力解法,如下
    r = 0
    for i in route:
        for j in range(len(house)-1):
            if house[j] <= i and house[j + 1] >= i:
                temp = max(i - house[j], house[j + 1] - i)
                r = temp if temp > r else r
    return r


if __name__ == "__main__":
    print(route_r([1, 2, 3], [2]))
    print(route_r([1, 2, 3], [2]))
