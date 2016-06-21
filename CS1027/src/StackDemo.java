import java.util.*;

public class StackDemo {
	
	public static void showPush(Stack st, int a){
		st.push(new Integer(a));
		System.out.println("push(" + a + ")");
		System.out.println("stack:" + st);
		
	}
	
	public static void showPop(Stack st){
		System.out.print("pop -> ");
		Integer a = (Integer)st.pop();
		System.out.println(a);
		System.out.println("stack: " + st);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack st = new Stack();
		System.out.println("stack: " + st);
		showPush(st, 42);
		showPush(st, 66);
	    showPush(st, 99);
	    
	    boolean isEmpty = st.empty();
	    Integer a = (Integer)st.peek();
	    Integer b = (Integer)st.search(42);
	    System.out.println(isEmpty);
	    System.out.println(a );
	    System.out.println(b);
	    showPop(st);
	    showPop(st);
	    try{
	    	showPop(st);
	    }catch (EmptyStackException e){
	    	System.out.println("empty stack");
	    }
		
	}

}
