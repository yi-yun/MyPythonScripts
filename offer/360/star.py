n = int(input())
n, m = map(int, input().split())
line = [[0]*n]*n
for i in range(n):
    line[i] = input().split(' ')
print(line)
