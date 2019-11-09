# -----------------------------------------------------------
# Python3 implementation of a Node class with 3 methods.
# This can be used to implement more complex data structures
# like LinkedLists, Stacks, Queues, etc.
#
# author: Jordan Starr
# email: jordanstarrk@gmail.com
# -----------------------------------------------------------

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def set_link_node(self, link_node):
    self.link_node = link_node

  def get_link_node(self):
    return self.link_node

  def get_value(self):
    return self.value

# -----------------------------------------------------------
# Here is an example of using the nodes. I create 3 Nodes,
# link them together, and then remove the middle Node.
# -----------------------------------------------------------

# Create 3 Nodes.
front = Node("front node")
middle = Node("middle node")
end = Node("end node")

#Link 3 Nodes.
front.set_link_node(middle) # [front] --> [middle]
middle.set_link_node(end) # [front] --> [middle] --> [end]

print(front.get_link_node().get_value()) # Print to see that the front Node is linked with the 'middle node'

#Remove the 'middle' node.
front.set_link_node(end)
print(front.get_link_node().get_value()) # Print to see that the front Node is linked with the end Node.
