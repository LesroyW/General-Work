package exercisesForLinkedLists;

// Exercises based on http://users.csc.calpoly.edu/~jdalbey/103/Demo/LinkedListExercises/

public class linkedListExercises {

	public class linkedListExercise1
	{
		//Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next);
		//	     
		//Solution
		//	     head.next = head.next.next;
	}

	public class linkedListExercise2 {

		//		 Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next);//	      
		//	     Node Q = new Node('q', head.next.next);
		//	   //Solution
		//	     head.next = head.next.next;

	}

	public class linkedListExercise3
	{
		//Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next);//	      
		//	     Node Q = new Node('q', head.next.next);

		//Solution
		//		Q.next = head.next;
	}

	public class linkedListExercise4 {
		////		Setup
		//		
		//		Node head = new Node('P', null );
		////	     head.next = new Node('1', null);
		////	     head.next.next = new Node('2', null);
		////	     head.next.next.next = new Node('3', null);
		////	     Node R = new Node('r', head.next.next.next);		      
		////	     
		////		Solution
		////	     R.next = head.next.next;
		//		
	}

	public class linkedListExercise5
	{
		//		Setup
		//		
		//		
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next);	
		//		
		//	    Solution 
		//	     
		//	     head.next.info = R.next.info;

	}


	public class linkedListExercise6
	{
		//		Setup
		//		Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next);
		//		
		//		
		//		Solution
		//		  head.next.info = head.next.next.next.info;

	}

	public class linkedListExercise7
	{
		//		//Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node R = new Node('r', head.next.next.next); 
		//	     
		//	     //Solution
		//	     R.next.next = head.next;

	}


	public class linkedListExercise8
	{
		//		//Setup
		//		Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	     Node Q = new Node('q', head.next.next);
		//	    
		//	     //Solution
		//		 Q.next.next.next = head.next;

	}

	public class linkedListExercise9
	{
		//		//Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('1', null);
		//	     head.next.next = new Node('2', null);
		//	     head.next.next.next = new Node('3', null);
		//	  
		//	     //Solution
		//	    head.next.next.next.next = head.next;
		//		

	}


	public class linkedListExercise10
	{
		//		//Setup
		//		 Node head = new Node('P', null );
		//	     head.next = new Node('A', null);
		//	     head.next.next = new Node('B', null);
		//	     head.next.next.next = new Node('C', null);
		//	     Node Q = new Node('q', head.next.next.next);
		//	     //Solution
		//	  head.next.next  = Q.next;

	}
	public class linkedListExercise11
	{
		//		Setup
		//		Node head = new Node('P', null );
		//	     head.next = new Node('A', null);
		//	     head.next.next = new Node('B', null);
		//	     head.next.next.next = new Node('C', null);
		//	   
		//Solution	     
		//	  head.next.next  = head.next.next.next;


	}
	
	public class linkedListExercise12
	{
//	//Setup
//	Node head = new Node('P', null );
//	head.next = new Node('_', null);
//	head.next.next = new Node('_', null);
//	head.next.next.next = new Node('_', null);
//	head.next.next.next.next = new Node('F',null);
//	Node Q = new Node ('q', head.next);
//	
//	//Solution
//	
//	Node n = Q;
//   while(n.next != null)
//  {
//  	n = n.next;
//  	Q.next = n;
//  }
	}
	
	
	public class linkedListExercise13
	{
////Setup
//		Node head = new Node('P', null );
//		head.next = new Node('a', null);
//		head.next.next = new Node('b', null);
//		head.next.next.next = new Node('c', null);
//		head.next.next.next.next = new Node('F',null);
//		Node Q = new Node ('q', head.next);
////Solution
//		
//		Node n = Q;
//        while(n.next != null && n.info != 'c')
//        {
//        	n = n.next;
//        	Q.next = n;
//        }
		
	}
	
	public class linkedListExercise14
	{
//        //Solution
//		Node head = new Node('P', null );
//		head.next = new Node('A', null);
//		head.next.next = new Node('B', null);
//		head.next.next.next = new Node('C', null);
//		head.next.next.next.next = new Node('D',null);
		
	}
	public class linkedListExercise15
{
		//Setup
//		Node head = new Node('P', null );		
//		head.next = new Node('B', null);
//		head.next.next = new Node('C', null);
//		Node Q = new Node('q', null);
//
//		//Solution
//		
//		Node A = new Node('A', head.next);
//		head.next = A;

	}
	public class linkedListExercise16
	{
////Setup
//		Node head = new Node('P', null );		
//		head.next = new Node('A', null);
//		head.next.next = new Node('B', null);
//		head.next.next.next = new Node('C', null);
//		//Solution
//        head.next.next.next.next = new Node('D', null);
	}
	public class linkedListExercise17
	{
////Setup
//		Node head = new Node('P', null );		
//		head.next = new Node('A', null);
//		head.next.next = new Node('B', null);
//		head.next.next.next = new Node('C', null);
//		//Solution
//		Node Q = new Node('Q', head.next);
//		head.next = head.next.next;
//		head.next.next.next = Q.next;
//		Q.next = null;
	}
	public class linkedListExercise18
	{
////Setup
//		Node head = new Node('P', null );		
//		head.next = new Node('A', null);
//		head.next.next = new Node('B', null);
//		head.next.next.next = new Node('C', null);
//		//Solution
//		head.next.next.next.next = head.next;
//		head.next = head.next.next;
	}
	public class linkedListExercise19
	{
//		//Setup
//		Node head = new Node('P', null );		
//		head.next = new Node('E', null);
//		head.next.next = new Node('H', null);
//		head.next.next.next = new Node('M', null);
//		
//		Node head2 = new Node('Q', null);
//		head2.next = new Node('B', null);		
//		head2.next.next = new Node('F', null);
//		head2.next.next.next = new Node('G', null);
//		head2.next.next.next.next = new Node('R', null);
//		
//		//Solution
//		head.next.next.next.next = head2.next.next.next.next;
//		head2.next.next.next.next = head.next.next;
//		head.next.next = head2.next.next;
//		head2.next.next = head.next;
//		head.next = head2.next;
//		head2.next = null;

	}
	public class linkedListExercise20
	{
//		//Setup
//		Node head = new Node('P', null);
//		head.next = new Node('A', null);
//		head.next.next = new Node('B', null);
//		head.next.next.next = new Node('C', null);
//		head.next.next.next.next = new Node('D', null);
//		
//		Node head2 = new Node('R', null);
//		Node head3 = new Node('Q', null);
//		
//		//Solution
//		head2.next = head.next;
//		
//		head.next = head2.next.next.next.next;
//		head.next.next = head2.next.next.next;
//		head.next.next.next = head2.next.next;
//		head.next.next.next.next = head2.next;
//		head2.next = null;
	}

	public static void main(String[] args) {


	}	
}
