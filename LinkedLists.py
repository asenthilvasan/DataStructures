# Linked Lists in Python

pets = ["cats", "dogs", "birds"]


# Linked list representation
# node_c = Node("birds", None) # create a Node object

# node_head.prev = None
# node_head.data = "fish"
# node_head.next = node_a
#
# node_a.prev = node_head
# node_a.data = "cats"
# node_a.next = node_c
#
# # node_b is now skipped
# node_b.data = "dogs"
# node_b.next = node_c
#
# node_c.data = "birds"
# node_c.next = node_d
#
# node_d.data = "mouse"
# node_d.next = None


# Adding a node: beginning, end, or middle
# Removing a node: beginning, end, or middle

"""
Linked Lists:
1. Are comprised of nodes
2. The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
3. Can be unidirectional or bidirectional
4. Are a basic data structure, and form the basis for many other data structures
5. Have a single head node, which serves as the first node in the list
6. Require some maintenance in order to add or remove nodes
7. The methods we used are an example and depend on the exact use case and/or programming language being used
"""

# x = number of items
# Task: find the number 4 in this list
items = [1, 4, 5, 5, 6, 7] # 7x memory
# For every single item we look at, we still have to hold the entire list in memory

# node_head = 1
# node_head.next = node_a
#
# node_a = 4
#
# if node_head==4:
#   return
# else:
#   node = node.next

# We only have to look at two different nodes, space/memory of 2x
# We never have to hold more than one element at a time in memory, just one node at a time


# "Telephone" game
# Imagine having to remember everyone's interpretation of the words at the same time: much harder
# But, in the actual game, only have to remember the person before us and what they said


# Making the Node Class

# node_b.data = "dogs"
# node_b.next = node_c

class Node():
    def __init__(self, value, next_node=None):
        self.value = value # current value of the node
        self.next_node = next_node # the node it points to (or the node that follows this current node)

    def __str__(self):
        if self.get_next() != None:
            return "Node: {} -> {}".format(self.value, self.get_next().get_value())
        else:
            return "Node: {} -> None".format(self.value)

    # getter method: get an attribute/property of the object
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def other_str(self):
        next_value = self.next_node
        if next_value != None:
            prints = "This node is {}. The next node is {}".format(self.value, next_value.get_value())
        else:
            return "This node is {}. There is no next node.".format(self.value)
        return prints

    # setter method: set an attribute/property of the object
    def set_next(self, next):
        # use type() to check for built-in Python types, but not user-defined classes
        if isinstance(next, Node) == False:
            return
        self.next_node = next



# The .next of a node should always be a node itself, or None
# node_head.next_node = "sdfdslfgfd" # This will work, but we don't want to be able to do this

node_head = Node("hello")
print(node_head.get_next())
print(node_head.get_value())

node_a = Node("goodbye")
# node_head.set_next(node_a)
print(node_head.get_next())

node_head.set_next("sdfdslfgfd") # This will fail based on the condition in our setter function

# Recreate this as a list of nodes
pets = ["cats", "dogs", "birds"]

node_4 = Node("hamster")
node_3 = Node("birds", node_4)
node_2 = Node("dogs", node_3)
node_1 = Node("cats", node_2)
print(node_1)
print(node_2)
print(node_3)
print("\n")

# Linked List - made up of a series of nodes
class LinkedList:
    # self.engine
    # self.size

    # self.head_node
    # self.middle_node
    # self.tail_node

    def __init__(self, value=None):
        # the LinkedList constructor calls the Node constructor to make a new Node
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        # for loop: if we know how many times to loop/how many elements
        current_node = self.get_head_node()
        while (current_node.get_next() != None):
            current_node = current_node.get_next()
        return current_node

        # what happens when current_node.get_next() is None? What does this mean?

    # append to head
    def append_to_head(self, value=None):
        new_node = Node(value)
        self.head_node.set_next(new_node)

    def append_to_tail(self, value=None):
        tail = self.get_tail_node()
        tail.set_next(Node(value))

    def __str__(self):
        current_node = self.get_head_node()
        prints = "Linked List: Start"

        while current_node != None:
            prints += " -> " + str(current_node.get_value())
            current_node = current_node.get_next()
        return prints

      # s = set(1, 4, 5)
      # print(s) # "Set: {1, 4, 5}"

linked_list1 = LinkedList(6) # Creates a linked list with a starting head_node with the passed value
linked_list1.append_to_head(5)
linked_list1.append_to_tail(4)
linked_list1.append_to_tail(3)
linked_list1.append_to_tail(2)
linked_list1.append_to_tail(1)
print(linked_list1)
print(linked_list1.get_tail_node()) # trying to pass an argument, linked_list1


"""
import sys
print(2**31 - 1) # Java max integer
print(sys.maxsize) # python max integer

# Positive integer, with positive sign bit
# 0111 1111 1111 1111 1111 1111 1111 1111

# two's complement
"""
