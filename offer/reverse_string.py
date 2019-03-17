def reserve(s):
    temp = s.split()
    return ' '.join(temp[::-1])


def rotate_string(s, n):
    if not s:
        return ''
    n %= len(s)
    return s[n:] + s[:n]
