package exercisesForLinkedLists;

import static org.junit.jupiter.api.Assertions.*;


import org.junit.jupiter.api.Test;

class linkedlistTestCases {


	private final ProblemStatement problemStatement = new ProblemStatement();
		
	
	@Test
	void testcase2() {
		
		Node A = new Node('A', null);
		A.next = new Node('B', null);
		A.next.next = new Node('C', null);
		A.next.next.next = new Node('D', null);
		A.next.next.next.next = new Node('E', null);
		A.next.next.next.next.next = new Node('F', null);
		
		assertEquals("hBCDEF", problemStatement.removeLetter(A));
	}
	
	@Test
	void testcase3()
	{
		Node A = new Node('F', null);
		A.next = new Node('E', null);
		A.next.next = new Node('D', null);
		A.next.next.next = new Node('C', null);
		A.next.next.next.next = new Node('B', null);
		A.next.next.next.next.next = new Node('A', null);
		
		assertEquals("hFEDCB", problemStatement.removeLetter(A));
	}
	
	@Test
	void testcase4()
	{
		Node A = new Node('A', null);
		A.next = new Node('A', null);
		A.next.next = new Node('A', null);
		A.next.next.next = new Node('B', null);
		A.next.next.next.next = new Node('C', null);
		A.next.next.next.next.next = new Node('D', null);
		
		assertEquals("hBCD", problemStatement.removeLetter(A));
	}
	
	@Test
	void testcase5()
	{
		Node A = new Node('D', null);
		A.next = new Node('C', null);
		A.next.next = new Node('B', null);
		A.next.next.next = new Node('A', null);
		A.next.next.next.next = new Node('A', null);
		A.next.next.next.next.next = new Node('A', null);
		
		assertEquals("hDCB", problemStatement.removeLetter(A));
	}
	
	@Test
	void testcase7()
	{
		Node A = new Node('A', null);
		A.next = new Node('A', null);
		A.next.next = new Node('A', null);
		A.next.next.next = new Node('A', null);
		A.next.next.next.next = new Node('A', null);
		A.next.next.next.next.next = new Node('A', null);
		
		assertEquals(null, problemStatement.removeLetter(A));
	}
	
	
	@Test
	void testcase8()
	{
		Node A = new Node('B', null);
		A.next = new Node('C', null);
		A.next.next = new Node('D', null);
		A.next.next.next = new Node('E', null);
		A.next.next.next.next = new Node('F', null);
		A.next.next.next.next.next = new Node('G', null);
		
		assertEquals("hBCDEFG", problemStatement.removeLetter(A));
	}
	
	@Test
	void testcase9()
	{
		Node A = new Node('A', null);
		A.next = new Node('A', null);
		A.next.next = new Node('B', null);
		A.next.next.next = new Node('A', null);
		A.next.next.next.next = new Node('C', null);
		A.next.next.next.next.next = new Node('A', null);
		
		assertEquals("hBC", problemStatement.removeLetter(A));
	}

}
