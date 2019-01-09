/**
 * 
 */
package phonebook;

import java.util.Set;

/**
 * ++++
 * To model a contact as a key-value pair that may exist in the context of a map.
 * 
 * @author S H S Wong
 * @version 17 Nov 2006 17:35:45
 */
public interface Contact<K,V,P> {
	
	/**
	 * @return the key of this key-value pair
	 */
	K key();
	
	/**
	 * @return the value of this key-value pair
	 */
	V value();
	
	/**
	 * @return a set of phone records
	 */
	Set<P> phones();

}
