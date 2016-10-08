
public class CircularArrayQueue<T> {
	private final int DEFAULT_CAPACITY = 100;
	private int rear, front, count;
	private T[] queue;

	public CircularArrayQueue(){
		rear = front = count = 0;
		queue = (T[])(new Object[DEFAULT_CAPACITY]);
	}
	
	public CircularArrayQueue(int initialCapacity){
		rear = front = count = 0;
		queue = (T[])(new Object[initialCapacity]);
	}
	
	public void enqueue(T element){
		// check capacity first
		if (size() == queue.length){
			expandCapacity();
		}
		queue[rear] = element;
		rear =(rear + 1) % queue.length;
		
		count++;
	}
	
	public T dequeue() throws EmptyCollectionException{
		// check empty
		if(isEmpty()){
			throw new EmptyCollectionException("queue");
		}
		T result = queue[front];
		queue[front] = null;
		front = (front + 1) % queue.length;
		count--;
		
		return result;		
	}
	
	public T first() throws EmptyCollectionException{
		if(isEmpty())
			throw new EmptyCollectionException();
		return queue[front];
	}
	
	public boolean isEmpty(){
		return(count == 0);
	}
	
	public int size(){
		return count;
	}
	
	public String toString(){
		String result = "";
		for (int i = front; i < rear; i++){
			result = result + queue[i];
		}
		return resutlt;
	}
	
	public void expandCapacity(){
		// create a new bigger arrary
		T[] larger = (T[])(new Object[queue.length * 2]);
		for(int i = 0; i < count; i++){
			larger[i] = queue[front];
			front = (front + 1) % queue.length;
		}
		
		front = 0;
		rear = count;
		queue = larger;
	}
}
