# -----------------------------------------------------------
# Python3 implementation of a Stack class with 3 core methods
# and 2 helper methods.
#
# -----------------------------------------------------------
from nodes import Node

class Stack:
  def __init__(self, limit=100):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_link_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the Stack!".format(value))
    else:
      print("Oops. Stack is full. Cant add {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_link_node()
      self.size -= 1
      print("Removing " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of items in the Stack.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing in the Stack!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0


# -----------------------------------------------------------
# Uncomment below to see an example of using the Stack. 
# I create a Stack with a capacity of y items. I push 7 items
# onto the Stack so it throws an error, then I remove items
# from the Stack. 
# -----------------------------------------------------------

# stack_example = Stack(6)

# stack_example.push("stack item #1")
# stack_example.push("stack item #2")
# stack_example.push("stack item #3")
# stack_example.push("stack item #4")
# stack_example.push("stack item #5")
# stack_example.push("stack item #6")
# stack_example.push("stack item #7")

# print("The first stack item is " + stack_example.peek())
# stack_example.pop()
# stack_example.pop()
# stack_example.pop()
# stack_example.pop()
# stack_example.pop()
# stack_example.pop()
