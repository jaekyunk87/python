"""
Question : You have a linked list and want to find the kth to last node.
           Write a function kth_to_last_node() that takes an integer k and the head_node of a singly-linked list, and returns the kth to last node in the list
"""
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# first approach O(n) time and O(1)
def kth_to_last_node(k, head):
    # Step 1: get the length of the list
    # Start at 1, not 0
    # else we'd fail to count the head node!
    list_length = 1
    current_node = head

    # Traverse the whole list,
    # Counting all the nodes
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    # Step 2: Walk to the target node
    # Calculate how far to go, from the head,
    # to get to the kth to last node
    how_far_to_go = list_length-k
    current_node = head
    for i in range(how_far_to_go):
        current_node = current_node.next
    
    print(current_node.value)
    return current_node

# second approach that what if there is a "stick" that was k nodes wide. moving k node wide stick to all the way to last node. then easily find kth node from the last.
def kth_to_last_node2(k, head):
    left_node = head
    right_node = head

    # Move right_node to the kth node (make k wide stick)
    for _ in range(k-1):
        right_node = right_node.next

    # Starting with left_node on the head,
    # move left_node and right_node down the list,
    # maintaining a distance of k between them,
    # until right_node hits the end of the list

    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

    # Since left_node is k nodes behind right_node,
    # left_node is now the kth to last node!

    print(left_node.value)
    return left_node




# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)
kth_to_last_node2(2,a)

# can do this in O(n) time
# can do this o(1) space. if you are recursing, you are probably taking 0(n) space onm teh call stack!
