# Complete the countDuplicates function below.
def countDuplicates(numbers):
    if not numbers:
        return 0
    if len(numbers) == 0:
        return 0
    cnt = 0
    for i in numbers:
        if numbers.count(i) > 1:
            cnt += 1
    return cnt // 2
    # return len(numbers)-len(set(numbers))
