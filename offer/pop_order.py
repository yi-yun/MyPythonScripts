# 栈的压入弹出序列
def pop_order(push_stack, pop_stack):
    if not push_stack or not pop_order:
        return False
    stack = []
    while pop_stack:
        val = pop_stack[0]
        if stack and stack[-1] == val:
            stack.pop()
            pop_stack.pop(0)
        else:
            while push_stack:
                if val != push_stack[0]:
                    stack.append(push_stack.pop(0))
                else:
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break
        if not push_stack:
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False
    if not pop_stack:
        return True
    return False
