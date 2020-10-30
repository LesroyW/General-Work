package exercisesForLinkedLists;

public class ProblemStatement {

	
	
	
	
	public String removeLetter(Node node)
	{
		
		
		
		Node head = new Node('h', null);
		Node tail = new Node('t', null);
		Node P = head;
		P.next = node;
		head.next = node;
		tail.next = node;
			   
	   
	    while(head.next.info == 'A')
	    {
	    	head.next = head.next.next;
	    }
	    
	    while(P != null)
	    {
	    	if(P.info != 'A')
    	    {
    	    	tail.next = P;
    	    }
	    		P = P.next;  	        	
	    }	    
	    tail.next.next = null;
		
		String listOutput = "";
		
		P = head;
		P.next = head.next;
		
		while(P != null)
		{
		
			listOutput += P.info;
			
					P = P.next;
		}
		
	
		return listOutput;
	}
	
}
