class _DoubleLinkedBase:
	""" A base class providing a doubly linked list representation."""

	class _Node:
		""" Lightweight, nonpublic class for storing a doubly linked node"""
		__slots__ = '_element', '_prev', '_next' # streamline memory

		def __init__(self, element, prev, next): # initialize node's fields
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		"""Create an empty list"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0 # number of elements

	def __len__(self):
		
		counter=0
		temp=self._header._next
		
		while temp._element is not None:
			counter=counter+1
			temp=temp._next

		return counter

		"""Return the number of elements in the list"""
		# ===== Start writing your code here =====
		pass # Remove this statement once you write your code
		# ===== End writing your code here =====
   
	def is_empty(self):
		if self._header==None : 
			return True
			

		# while self._header is None:
		# 	count=count+1
		# if count==self.__len__()+2:
		# 	print("empty")
		# else :
		# 	print("not empty")
		# 	return True
		 
		# """Return true if list is empty"""
	

	def _insert_between(self, e, predecessor, successor):
		"""Add element e between two existing nodes and return new node"""

		newest = self._Node(e, predecessor, successor)
		self.elnum=e
		self.predecessor=predecessor
		self.successor=successor
		self.predecessor._next=newest
		self.successor._prev=newest
		newest._prev=predecessor
		newest._next=successor
		
		return newest

		# newest._next=successor
		# newest._prev=predecessor
		# # ===== Start writing your code here =====
		pass # Remove this statement once you write your code
		# ===== End writing your code here =====

	def _delete_node(self, node):
		node._prev._next=node._next
		node._next._prev=node._prev
		node._prev=None
		node._next=None
		
		"""Delete nonsentinel node from the list and return its elements"""
		# ===== Start writing your code here =====
		pass # Remove this statement once you write your code
		# ===== End writing your code here =====





