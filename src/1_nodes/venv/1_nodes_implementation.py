#1_Nodes_implementation using Python3
# - Nodes are the fundamental building block of many data structures
# - They form the basis for linked lists, stacks, queues, trees, and more
# - An individual node contains data and links to other nodes
# - Nodes can only be linked to from a single other node
#
#Here we will create a Node class with 3 Methods: set link, get link, and get value

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

#Create 3 Nodes (front, middle, end)
front = Node("front node")

middle = Node("middle node")

end = Node("end node")

#Link nodes together to create [front] --> [middle] --> [end]
front.set_link_node(middle) # [front] --> [middle]
middle.set_link_node(end) # [front] --> [middle] --> [end]
# print(front.get_link_node().get_value())
# print(middle.get_link_node().get_value())

print(front.get_link_node().get_value()) #Test and see that the front link node will print 'middle node'

#Let's remove the middle node. To do this, change the link from the front node to link to the end node
front.set_link_node(end)
print(front.get_link_node().get_value()) #Test and see that the front link node will print 'end node'
