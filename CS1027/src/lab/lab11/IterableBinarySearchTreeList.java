import java.util.Iterator;

public class IterableBinarySearchTreeList extends LinkedBinaryTree {
	
	
	public Iterator iteratorInOrderDescending(){
		ArrayUnorderedList tempList = new ArrayUnorderedList();
        inorder(root, tempList);

        return tempList.iterator();
	}
	
	private void inorderDescending(BinaryTreeNode node, ArrayUnorderedList tempList){
		if (node != null) {
			inorderDescending(node.getRight(), tempList);
            tempList.addToRear(node.getElement());
            inorderDescending(node.getLeft(), tempList);
        }
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
