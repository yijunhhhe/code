/**
 * class represents an linked implementation of priority queue adt 
 * with some basic operations such as enqueue, dequeue etc.
 *
 * @author Yijun He
 */

public class LinkedPriorityQueue<T> implements PriorityQueueADT<T>
{
	   /*
	    * the size of the queue
	    */
	   private int count;
	   
	   /*
	    * reference to the front of the queue and the end of the queue
	    */
	   private PriorityNode<T> front, rear;

	   /**
	    * Creates an empty queue.
	    */
	   public LinkedPriorityQueue()
	   {
	      count = 0;
	      front = rear = null;
	   }

	   /**
	    * Adds the specified element to the rear of this queue.
	    *
	    * @param element  the element to be added to the rear of this queue
	    */
	   public void enqueue (T element)
	   {
		   PriorityNode<T> node = new PriorityNode<T>(element);

	      if (isEmpty())
	         front = node;
	      else{
	         rear.setNext (node);
	         node.setPriority(rear.getPriority() + 1);
	      }

	      rear = node;
	      count++;
	   }
	   
	   /**
	    * Addds the specified element to the rear of this queue
	    * @param element the element to be added to the rear of this queue
	    * @param p priority of the element
	    */
		public void enqueue(T element, double p) {
			PriorityNode<T> node = new PriorityNode<T>(element,p);
			PriorityNode<T> current = null; 
			PriorityNode<T> previous = null;
			if (isEmpty()){
		         front = node;
		         rear = node;
			} else{
			current = front;
						

			while (current != null && p > current.getPriority()){
				previous = current;
				current = current.getNext();			
			}
			
			if(current == null){
				previous.setNext(node);
				rear = node;
			} else if (previous == null){
				node.setNext(front);
				front = node;
			}else{
				previous.setNext(node);
				node.setNext(current);
			}
	}
			
			count++;
			
		}
		
		
	   /**
	    * Removes the element at the front of this queue and returns a
	    * reference to it. Throws an EmptyCollectionException if the
	    * queue is empty.
	    *
	    * @return                           the element at the front of this queue
	    * @throws EmptyCollectionException  if an empty collection exception occurs
	    */
	   public T dequeue() throws EmptyCollectionException
	   {
	      if (isEmpty())
	         throw new EmptyCollectionException ("queue");

	      T result = front.getElement();
	      front = front.getNext();
	      count--;

	      if (isEmpty())
	         rear = null;

	      return result;
	   }
	   
	   /**
	    * Returns a reference to the element at the front of this queue.
	    * The element is not removed from the queue.  Throws an
	    * EmptyCollectionException if the queue is empty.  
	    *
	    * @return                            a reference to the first element in
	    *                                    this queue
	    * @throws EmptyCollectionsException  if an empty collection exception occurs
	    */
	   public T first() throws EmptyCollectionException
	   {
		   if (isEmpty())
		      throw new EmptyCollectionException ("queue"); 

		   return front.getElement();
	   }

	   /**
	    * Returns true if this queue is empty and false otherwise. 
	    *
	    * @return  true if this queue is empty and false if otherwise
	    */
	   public boolean isEmpty()
	   {
		   return (count == 0);
	   }
	 
	   /**
	    * Returns the number of elements currently in this queue.
	    *
	    * @return  the integer representation of the size of this queue
	    */
	   public int size()
	   {
		   return count;
	   }

	   /**
	    * Returns a string representation of this queue. 
	    *
	    * @return  the string representation of this queue
	    */
	   public String toString()
	   {
		   String result = "";
		      PriorityNode<T> current = front;

		      while (current != null)
		      {
		         result = result + (current.getElement()).toString() + "\n";
		         current = current.getNext();
		      }

		      return result;
	   }

	
}
