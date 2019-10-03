# Class for creating a node structure
class Node:

	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None

# Tree Class Main Class
class Tree:

	# This method create a new Node
	def create_node(self, value):

		# print("Node created.")
		return Node(value)

	# This method insert a node into a tree
	def insert_node(self, node, value):

		if node is None:

			# print("Root created.")
			return self.create_node(value)

		if value <=  node.data:

			print("Inserted left.")
			node.left = self.insert_node(node.left, value)

		elif value > node.data:

			print("Inserded Right.")
			node.right = self.insert_node(node.right, value)

		return node

	# THis method will delete a node from a tree
	def delete_node(self, node, value):

		if node is None:

			return None

		if value <=  node.data:

			node.left = self.delete_node(node.left, value)

		elif value > node.data:

			node.right = self.delete_node(node.right, value)
		
		else:
			
			if node.left==None and node.right==None:
				del node
			
			elif node.left==None:
				temp=node.right
				del node
				return temp
			
			elif node.right == None:
				temp = node.left
				del node
				return temp

		return node


	# Inorder trabersal for a tree
	# This gives a sorted order of sequence
	def traverse_Inorder(self, root):

		if root is not None:
			# print("Traversing start.")
			self.traverse_Inorder(root.left)
			print(root.data)
			self.traverse_Inorder(root.right)

	# PreOrder Traversal for a tree
	def traverse_preorder(self, root):
		
		if root is not None:
			# print("Traversing start.")
			print(root.data)
			self.traverse_Inorder(root.left)
			self.traverse_Inorder(root.right)

	# Post order traversal for a Tree
	def traverse_postorder(self, root):
		
		if root is not None:
			# print("Traversing start.")
			self.traverse_Inorder(root.left)
			self.traverse_Inorder(root.right)
			print(root.data)



# Main function
def main():

	root = None
	tree = Tree()
	root = tree.insert_node(root,10)
	arr=[10,30,40,70,80,90,100]
	for i in arr:
		tree.insert_node(root,i)

	tree.traverse_Inorder(root)
	tree.traverse_preorder(root)
	tree.traverse_postorder(root)

if __name__=="__main__":
	main()