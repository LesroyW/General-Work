package dsaj;

import java.util.Iterator;

/**
 * AbstractSet provides concrete implementation for methods that are
 * common to all sets, regardless of their implementation.
 * 
 * @author Alan Barnes
 * @author S H S Wong (modified by)
 * @version 11-10-2010
 *
 * @param <T>
 */
public abstract class AbstractSet<T> implements SetADT<T> {

	public boolean addAll (SetADT<T>  A) { 
		boolean hasBeenModified = false;
		/* Repeatedly applies add to the the elements of set A 
		 * one by one to this set.
		 */
		for(T element : A) {
			if(this.add(element)) {
				hasBeenModified = true;
			}
		}
		return hasBeenModified;
	}

	public boolean removeAll(SetADT<T>  A) {
		boolean hasBeenModified = false;
		/* Repeatedly applies remove to the the elements of set A 
		 * one by one to this set.
		 */
		Iterator<T> iter = A.iterator();
		while (iter.hasNext()) {
			if(this.remove(iter.next())) {
				hasBeenModified = true;
			}
		}
		return hasBeenModified;
	}

	public boolean retainAll(SetADT<T>  A) {
		boolean hasBeenModified = false;
		Iterator<T> iter = this.iterator();
		while (iter.hasNext()) {
			T elem = iter.next();
			if(!A.contains(elem)) {
				/* The current element does not appear in Set A. 
				 * Removes it from the set.
				 */
				hasBeenModified = this.remove(elem);
			}
		}
		return hasBeenModified;
	}

	public boolean isSubset(SetADT<T> A) {
		if(this.size() > A.size()) {
			/* As this set has more elements than Set A, 
			 * it cannot be a subset of Set A. 
			 */
			return false;
		}

		/* Checks through the elements in this set one by one
		 * to see if any of them is not a member of Set A.
		 */
		for(T element : this) {
			if(!A.contains(element)) {
				/* As there is an element in this set which 
				 * is not a member of Set A, this set cannot
				 * be a subset of Set A.
				 */
				return false;
			}
		}
		
		return true;
	}

	public boolean equals(SetADT<T> A) {
		/* If this set does not have the same number of elements
		 * as Set A, it cannot be the same as Set A.
		 */
		if(this.size() != A.size()) {
			return false;
		}
		/* This set is the same as Set A if:
		 * (1) this set is a subset of Set A, and
		 * (2) Set A is a subset of this set.
		 */
		return isSubset(A) && A.isSubset(this);
	}
}
