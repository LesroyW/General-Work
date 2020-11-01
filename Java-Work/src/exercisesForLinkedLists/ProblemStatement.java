package exercisesForLinkedLists;

public class ProblemStatement {

	
	
	
	
	public String removeLetter(Node node)
	{
		if(node == null)
		{
			return null;
		}
						
		Node head = new Node('h', null);
		Node tail = new Node('t', null);
		Node P = head;
		P.next = node;
		head.next = node;
		tail.next = node;
			   
	   
	    while(head.next.info == 'A')
	    {
	    	head.next = head.next.next;
	    	if(head.next == null)
	    	{
	    		return null;
	    	}
	    }    
	   
	    while(P != null)
	    {		   	    	
	    		if(P.info != 'A')
		    	{
		    		tail.next = P;
		    		
		    	} 
	    	
	    		  P = P.next;      			        	
	    }	  
	  
		String listOutput = "";
		
		P = head;
		P.next = head.next;
		
		while(P != tail.next)
		{
		
			if(P.next.info == 'A')
			{
				P.next = P.next.next;
			}
			
			P = P.next;
			listOutput += P.info;
			
		}	
	
		return listOutput;
	}
	
}
