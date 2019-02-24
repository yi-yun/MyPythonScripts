def reverse_link(head):
    if not head or not head.next:
        return head
    then = head.next
    last = then.next
    head.next = None
    while then:
        then.next = head
        head = then
        then = last
        if then:
            last = then.next
    return head
