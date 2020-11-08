package exerciseForBinaryTree;

public class binaryTree {

	binaryTreeNode root;
	
	private binaryTreeNode addRecursive(binaryTreeNode current, int val)
	{
		if(current == null)
		{
			return new binaryTreeNode(val);
		}
		
		if(val < current.value)
		{
			current.left = addRecursive(current.left, val);
		} else if(val > current.value)
		{
			current.right = addRecursive(current.right, val);
		} else
		{
			
		}
		
		return current;
	}
	
	
	public void traverseInOrder(binaryTreeNode node)
	{
		if(node != null)
		{
			traverseInOrder(node.left);
			System.out.println(node.value);
			traverseInOrder(node.right);
		}
	}
	
	public void preOrder(binaryTreeNode node)
	{
		if(node != null) {
			System.out.println(node.value);
		traverseInOrder(node.left);		
		traverseInOrder(node.right);
		}
	}
	
	public void postOrder(binaryTreeNode node)
	{
		if(node != null) {
			
		traverseInOrder(node.left);		
		traverseInOrder(node.right);
		System.out.println(node.value);
		}
	}

	
	public void add(int val)
	{
		root = addRecursive(root, val);
	}
	
	public Boolean containsRecursive(binaryTreeNode current, int val)
	{
		if(current == null)
		{
			return false;
		}
		
		if(current.value == val)
		{
			return true;
		}
		
		if(val < current.value)
		{
			return containsRecursive(current.left, val);
		} else {
			return containsRecursive(current.right, val);
		}
	}
	
	private binaryTreeNode deleteRecursive(binaryTreeNode current, int val)
	{
		if(current == null)
		{
			return null;
		}
		
		if(current.value == val)
		{
			if(current.left == null && current.right == null)
			{
				return null;
			}
			
			if(current.right == null)
			{
				return current.left;
			}
			
			if(current.left == null)
			{
				return current.right;
			}
			
			int smallestvalue = findSmallestValue(current.right);
			current.value = smallestvalue;
			current.right = deleteRecursive(current.right, smallestvalue);
			return current;
		}		
		
		
		return val < current.value		
		? deleteRecursive(current.left, val)
		: deleteRecursive(current.right, val);
		
	}
	
	private int findSmallestValue(binaryTreeNode root) {
		return root.left == null ? root.value : findSmallestValue(root.left);
	}
	
	public void delete(int val)
	{
		root = deleteRecursive(root, val);
	}
	
	public static void main(String[] args)
	{
		binaryTree bTree = new binaryTree();
		
		bTree.add(10);
		bTree.add(20);
		bTree.add(7);
		bTree.add(3);
		bTree.add(29);
		bTree.delete(10);
		System.out.println("In Order:");
		bTree.traverseInOrder(bTree.root);
		System.out.println("pre Order:");
		bTree.preOrder(bTree.root);
		System.out.println("Post Order:");
		bTree.postOrder(bTree.root);
		if(bTree.containsRecursive(bTree.root, 1) == true)
		{
		System.out.println("Correct");
		} else {
			System.out.println("Does not exist");
		}
	}
}
