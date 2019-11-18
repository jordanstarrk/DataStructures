# -----------------------------------------------------------
# Python3 implementation of a Queue class with 3 core methods
# and 3 helper methods.
#
# -----------------------------------------------------------

from nodes import Node

class Queue:
  def __init__(self, queue_size_limit=None):
    self.front = None
    self.back = None
    self.queue_size_limit = queue_size_limit
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      add_item = Node(value)
      print("Adding " + str(add_item.get_value()) + " to the queue!")
      if self.is_empty():
        self.front = add_item
        self.back = add_item
      else:
        self.back.set_link_node(add_item)
        self.back = add_item
      self.size += 1
    else:
      print("Oops, no more room!")
         
  def dequeue(self):
    if self.get_size() > 0:
      remove_item = self.front
      print(str(remove_item.get_value()) + " item removed from queue!")
      if self.get_size() == 1:
        self.front = None
        self.back = None
      else:
        self.front = self.front.get_link_node()
      self.size -= 1
      return remove_item.get_value()
    else:
      print("The queue is empty!")
  
  def peek(self):
    if self.size > 0:
      return self.front.get_value()
    else:
      print("The queue is empty!")
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.queue_size_limit == None:
      return True
    else:
      return self.queue_size_limit > self.get_size()
    
  def is_empty(self):
    return self.size == 0


# -----------------------------------------------------------
# Uncomment below to see an example of using the queue. 
# I create a queue with a max capacity of 5 items. I enqueue
# 6 items to the queue and prevent Stack Overflow by returning
# some text. Then I dequque the items and likewise prevent 
# Stack underflow. 
# -----------------------------------------------------------

# lineup = Queue(5)
# print("Adding items to our queue line...\n------------")
# lineup.enqueue("first item")
# lineup.enqueue("second item")
# lineup.enqueue("third item")
# lineup.enqueue("fourth item")
# lineup.enqueue("fifth item")
# lineup.enqueue("sixth item")

# print("------------\nRemoving items from our queue line... " + lineup.peek())
# lineup.dequeue()
# lineup.dequeue()
# lineup.dequeue()
# lineup.dequeue()
# lineup.dequeue()
# lineup.dequeue()
