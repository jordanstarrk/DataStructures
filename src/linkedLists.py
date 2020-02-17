# -----------------------------------------------------------
# Python3 implementation of a LinkedList class with 4 methods.
#
# -----------------------------------------------------------
from nodes import Node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def peek_head(self):
    return self.head_node.get_value()
  
  def insert_front_node(self, new_value):
    new_node = Node(new_value)
    new_node.set_link_node(self.head_node)
    self.head_node = new_node
  
  def length_of_list_iterative(self):
    count = 0
    cur_node = self.head_node

    while cur_node:
      count += 1
      cur_node = cur_node.get_link_node()
      return count
  
  def string_list(self):
    str_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        str_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_link_node()
    return str_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_link_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_link_node(next_node.get_link_node())
          current_node = None
        else:
          current_node = next_node


# -----------------------------------------------------------
# Uncomment below to see an example of using the LinkedList. 
# I create the LinkedList with an initial node, and then add 
# two Nodes to the LinkedList.
# -----------------------------------------------------------

# linked_list_sample = LinkedList("initial node")
# linked_list_sample.insert_front_node("second node")
# linked_list_sample.insert_front_node("third node")
# print(linked_list_sample.string_list())
