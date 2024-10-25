class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Реверсування однозв'язного списку:

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Приклад використання
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_linked_list(head)

# Виведення реверсованого списку
node = reversed_head
while node:
    print(node.value, end=" -> ")
    node = node.next
print("None")


# Сортування однозв'язного списку (злиттям):

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    return merge_sorted_lists(left, right)

def get_middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# Приклад використання
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head = merge_sort_linked_list(head)

# Виведення відсортованого списку
node = sorted_head
while node:
    print(node.value, end=" -> ")
    node = node.next
print("None")


# Об'єднання двох відсортованих однозв'язних списків:

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# Приклад використання
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_list = merge_two_sorted_lists(l1, l2)

# Виведення об'єднаного списку
node = merged_list
while node:
    print(node.value, end=" -> ")
    node = node.next
print("None")
