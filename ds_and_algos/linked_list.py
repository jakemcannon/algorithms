
# Remember the user never interfaces with the node class
# It is a subclass for the linkedlist
# The linkedlist class will interface with the node class
class node:
	# I believe this is the "constructor"
	# So we are saying our node class is going to have a data field
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:

	def __init__(self):
		self.head = node()

	# This implementation does not offer adding to specific index
	def append(self, data):
		# Remember, we want to add a new node
		# So we need to create it first
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next

		cur.next = new_node

	# This method is o(N)
	# The Java implementation sets lenth as an attribute of LinkedList class
	# Then increments via the add method
	# However, I think not having the length is more similar to Leetcode
	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def display(self):
		elems = []
		cur = self.head
		print(cur.data)
		while cur.next != None:
			cur = cur.next
			elems.append(cur.data)
		print(elems)

	def get(self, index):
		if index < 0 or index >= self.length():
			print("ERROR: GET index out of range")
			return None
		id_x = 0
		cur = self.head
		while True:
			cur = cur.next
			if id_x == index:
				return cur.data
			id_x += 1


	# fyi this got massively confusing
	# because the head initially starts off as head == None
	def remove(self, index):
		if index < 0 or index >= self.length():
			print("ERROR: GET index out of range")
			return None
		id_x = 0
		cur_node = self.head
		while True:
			# print("cur_node:" + str(cur_node.data))
			# print("cur_node.next:" + str(cur_node.next.data))
			prev_node = cur_node
			# print("prev_node:" + str(prev_node.data))
			# print(" ")

			cur_node = cur_node.next
			# print("cur_node:" + str(cur_node.data))
			# print("cur_node.next:" + str(cur_node.next.data))
			# print("prev_node:" + str(prev_node.data))
			# print("prev_node.next:" + str(prev_node.next.data))
			print(" ")
			if id_x == index:
				prev_node.next = cur_node.next
				# print("cur_node:" + str(cur_node.data))
				# print("cur_node.next:" + str(cur_node.next.data))
				# print("prev_node:" + str(prev_node.data))
				# print("prev_node.next:" + str(prev_node.next.data))
				return
			id_x += 1

	# def copy(self):


l = linked_list()

l.display()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.display()

l2 = linked_list()
# How to copy a linked list
print("Copied LinkedList")
while l.head.next != None:
	l2.append(l.head.next.data)
	l.head = l.head.next
l2.display()




