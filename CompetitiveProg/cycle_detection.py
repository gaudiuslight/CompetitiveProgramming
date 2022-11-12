class Node(object):
    value = int
    next = None
    prev = None
    
    def __init__(self, n, next_node=None, prev_node=None):
        self.value = n
        self.next = next_node
        self.prev = prev_node
    
    def __str__(self):
        return "Node value: {}".format(self.value)

def initialize_nodes():
    prev_node = None
    head_node = None
    cyclic_node = None
    for n in range(1, 9):
        current_node = Node(n)
        if prev_node:
            prev_node.next = current_node
            current_node.prev = prev_node
        if n == 1:
            head_node = current_node
            cyclic_node = current_node
        #elif n == 7:
        #    cyclic_node = current_node
        elif n == 8:
            current_node.next = cyclic_node
        prev_node = current_node
    
    return head_node

list_node = initialize_nodes()

# floyd's tortoise and hare algo
def detect_cycle(head):
    if not head.next:
        return None  
    hare_node = head.next.next
    tortoise_node = head.next
    cycle_detected = None
    while hare_node.next and hare_node.next.next:
        hare_node = hare_node.next.next
        tortoise_node = tortoise_node.next
        if tortoise_node == hare_node:
            cycle_detected = hare_node
            break
            
    if cycle_detected is None:
        return None
    else:
        while head != cycle_detected:
            head = head.next
            cycle_detected = cycle_detected.next
        return head


cyclic_node = detect_cycle(list_node)
print("My Cyclic Node is!")
print(cyclic_node)