/**
 * 
 */
package addressBook;

import java.util.NoSuchElementException;

/**
 * This interface specifies the ADT list.
 * 
 * @author S H S Wong
 * @version 25 Nov 2006 11:19:28
 */
public interface List<E> {

	/**
	 * Add an element at a specified position in the list.
	 * 
	 * @param position
	 * @param element
	 */
	void addAt(int position, E element) 
			throws NoSuchElementException;
	
	/**
	 * Remove the element at a specified position.
	 * 
	 * @param position	the position of the element within the list
	 * @return	the element that is kept in the removed node.
	 * @throws NoSuchElementException
	 */
	E removeAt(int position) throws NoSuchElementException;
	
	/**
	 * Return the element at a specified position 
	 * @param position	the position within the list that the required element
	 * 					is kept.
	 * @return the required element
	 */
	E getElementAt(int position) throws NoSuchElementException;
	
	/**
	 * Return the size of the list 
	 * @return	the number of elements kept in the list.
	 */
	int size();
	
	/**
	 * Return a string representation of the list.
	 * @return	a string representation of the list.
	 */
	String toString();
	
}
