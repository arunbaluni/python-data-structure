# This is a LinkedList Program in Python


# Class to create node instances to create a linkedlist
class node(object):
	def __init__(self, value):
		self.value = value
		self.next  = None

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_node_address(self):
		return self.next

	def set_node_address(self, next):
		self.next = next;


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.count = 0

	def insert(self, value):
		new_node = node(value)
		new_node.set_value(value)
		new_node.set_node_address(None)

		if(self.head == None):
			self.head = new_node
			self.count += 1
		else:
			counter = self.head
			while(counter.get_node_address() != None):
				counter = counter.get_node_address()
				continue

			counter.set_node_address(new_node)
			self.count += 1

	def get_list_count(self):
		print("Length of linkedlist = ", self.count)
		return self.count

	def display_linked_list(self):
		temp_node = self.head

		while(temp_node!=None):
			print("Node", temp_node.get_value())
			temp_node = temp_node.next

		print("Full LinkedList is printed")

	def delete_first_node_in_linkedlist(self):
		self.head = self.head.get_node_address()
		self.count -= 1

	def find_value_in_list(self, search_value):
		temp_node = self.head
		index = 0

		while(index < self.count):
			index += 1

			if(temp_node.get_value() == search_value):
				break
			else:
				temp_node = temp_node.get_node_address()
				continue
		return index

	def search_and_delete_node_in_linkedlist(self, search_value):
		index_value = self.find_value_in_list(search_value)
		temp_node = self.head

		if(index_value == 1):
			self.delete_first_node_in_linkedlist()
		else:
			for i in range(index_value - 2):
				temp_node = temp_node.get_node_address()
				continue

			temp_node.set_node_address(temp_node.get_node_address().get_node_address())
			self.count -= 1

		print("Seached value", search_value, " is found at position ", index_value, " from start is deleted now")



# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.insert(100)
itemlist.insert(132)
itemlist.insert(159)
itemlist.insert(1005)
itemlist.display_linked_list()
itemlist.search_and_delete_node_in_linkedlist(49)
itemlist.display_linked_list()
itemlist.search_and_delete_node_in_linkedlist(38)
itemlist.display_linked_list()
itemlist.search_and_delete_node_in_linkedlist(100)
itemlist.display_linked_list()