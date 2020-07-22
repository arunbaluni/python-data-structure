# This example covers the stack data structure implementation using LinkedList

# Class to create node instances to create a linkedlist
class node(object):
	def __init__(self, value):
		self.value = value
		self.next  = None

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_linked_node_address(self):
		return self.next

	def set_linked_node_address(self, next):
		self.next = next;


class Stack(object):
	def __init__(self, head=None):
		self.head = head
		self.count = 0

	def push(self, value):
		new_node = node(value)
		new_node.set_value(value)
		new_node.set_linked_node_address(None)

		if(self.head == None):
			self.head = new_node 
			self.count += 1
		else:
			new_node.set_linked_node_address(self.head)
			self.head = new_node
			self.count += 1

	def pop(self):
		temp_node = self.head
		self.head = self.head.get_linked_node_address()
		temp_node.set_linked_node_address(None)
		self.count -= 1
		print("\nItem deleted from Stack ->", temp_node.get_value())


	def isEmpty(self):
		if(self.head == None):
			return True
		else:
			return False

	def peek(self):
		if(self.isEmpty()):
			print("Stack is empty")
		else:
			print("\nTop element in Stack -> ", self.head.get_value())

	def display_stack(self):
		temp_node = self.head

		if self.isEmpty():
			print("Stack is empty")
		else:
			print("### Stack data ###")
			while(temp_node!=None):
				print(temp_node.get_value(), "->", end = " ")
				temp_node = temp_node.next
			return

		#print("Full LinkedList is printed")



# create a linked list and insert some items
stack = Stack()
stack.push(38)
stack.push(49)
stack.push(13)
stack.push(15)
stack.push(100)
stack.push(132)
stack.push(159)
stack.push(1005)
stack.display_stack()
stack.peek()
stack.pop()
stack.display_stack()
stack.peek()
stack.pop()
stack.display_stack()