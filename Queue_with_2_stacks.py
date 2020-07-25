# This program will implement Queue with 2 Stacks

# node class to act as Data Structure
class node:
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

# LinkedList implementation for creating Stack using node data structure
class Stack(node):
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
		return temp_node.get_value()

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

	def display_stack(self, isDequeued):
		temp_node = self.head

		if self.isEmpty():
			print("Stack is empty")
		else:
			if(isDequeued == False):
				new_list = []
				print("\n### Queue data ###")
				while(temp_node!=None):
					new_list.append(temp_node.get_value())
					temp_node = temp_node.next

				# Point i to the last element in list
				i = len(new_list) - 1 

				# Iterate till 1st element and keep on decrementing i
				while i >= 0 :
					print(new_list[i], "->", end = "" )
					i -= 1
				print("\n")

			else:
				print("\n### Queue data ###")
				while(temp_node!=None):
					print(temp_node.get_value(), "->", end = "" )
					temp_node = temp_node.next
				print("\n")

# Class implementation of Queue with enqueue() & dequeue() function to add/delete elements in Queue using Stack
class Queue(Stack):
	def __init__(self):
		super().__init__()
		self.stack1 = Stack()
		self.stack2 = Stack()
		self.isDequeued = False

	def enqueue(self, value):
		if(self.isDequeued):
			while(self.stack2.isEmpty() != True):
				self.stack1.push(self.stack2.pop())
		self.stack1.push(value)
		self.isDequeued = False

		print("Queue additon ->", value)


	def dequeue(self):
		if(self.stack1.isEmpty() and self.stack2.isEmpty()):
			print("Queue is empty")

		if(self.isDequeued == False):
			while(self.stack1.isEmpty() != True):
				self.stack2.push(self.stack1.pop())
		
		print("\nQueue deletion ->", self.stack2.pop())

		self.isDequeued = True


	def display_queue(self):

		if(self.isDequeued == True):
			self.stack2.display_stack(self.isDequeued)
		else:
			self.stack1.display_stack(self.isDequeued)


# create a linked list and insert some items
queue = Queue()
queue.enqueue(38)
queue.enqueue(49)
queue.enqueue(13)
queue.enqueue(15)
queue.display_queue()
queue.dequeue()
queue.display_queue()
queue.enqueue(100)
queue.display_queue()
queue.enqueue(132)
queue.enqueue(159)
queue.enqueue(1005)
queue.display_queue()
queue.dequeue()
queue.dequeue()
queue.display_queue()