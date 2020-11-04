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
	
	public static void main(String[] args)
	{
		binaryTree bTree = new binaryTree();
		
		bTree.add(10);
		bTree.add(20);
		bTree.add(7);
		bTree.add(3);
		System.out.println("In Order:");
		bTree.traverseInOrder(bTree.root);
		System.out.println("pre Order:");
		bTree.preOrder(bTree.root);
		System.out.println("Post Order:");
		bTree.postOrder(bTree.root);
	}
}
