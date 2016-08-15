import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.KeyEvent;

public class Snake {
	private Node head = null;
	private Node tail = null;
	private int size = 0;
	
	private Node n = new Node(20,30,Dir.L);
	private Yard y;
	
	
	public Snake(Yard y){
		head = n;
		tail = n;
		size = 1;
		this.y = y;
	}
	
	public void addToTail(){
		Node node = null;
		switch(tail.dir){
		case L: 
			node = new Node(tail.row, tail.column + 1, tail.dir);
			break;
		case U:
			node = new Node(tail.row + 1, tail.column, tail.dir);
			break;
		case R:
			node = new Node(tail.row, tail.column - 1, tail.dir);
			break;
		case D:
			node = new Node(tail.row - 1, tail.column, tail.dir);
			break;
		}
		tail.next = node;
		head.previous = tail;
		tail = node;
		size++;
	}
	
	public void addToHead(){
		Node node = null;
		switch(tail.dir){
		case L :
			node = new Node(head.row, head.column - 1, head.dir);
			break;
		case U :
			node = new Node(head.row - 1, head.column, head.dir);
			break;
		case R :
			node = new Node(head.row, head.column + 1, head.dir);
			break;
		case D :
			node = new Node(head.row + 1, head.column, head.dir);
			break;
		}
		node.next = head;
		head.previous = node;
		head = node;
		size++;
	}
	
	public void draw(Graphics g){
		if(size <= 0) return;
		move();
		for(Node n = head; n != null; n = n.next){
			n.draw(g);
		}
		
	}
	
	private void move() {
		addToHead();
		deleteFromTail();
		checkDead();
	}
	
	private void checkDead(){
		if(head.row < 0 || head.column < 2 || head.row > Yard.ROWS || head.column > Yard.COLUMNS){
			y.stop();
		}
	}

	private void deleteFromTail() {
		if(size == 0) return;
		tail = tail.previous;
		tail.next = null;
		
	}

	private class Node{
		int width = Yard.BLOCK_SIZE;
		int height = Yard.BLOCK_SIZE;
		int row, column;
		Dir dir = Dir.R;
		Node next = null;
		Node previous = null;
		
		Node(int row, int column, Dir dir) {
			this.row = row;
			this.column = column;
			this.dir = dir;
		}
		
		void draw(Graphics g){
			Color c = g.getColor();
			g.setColor(Color.BLACK);
			g.fillRect(Yard.BLOCK_SIZE * column, Yard.BLOCK_SIZE * row , width, height);
			g.setColor(c);
		}
	}
	
	public void eat(Egg e){
		if(this.getRect().intersects(e.getRect())){
			e.reAppear();
			this.addToHead();
		}
	}
	
	private Rectangle getRect(){
		return new Rectangle(Yard.BLOCK_SIZE * head.column, Yard.BLOCK_SIZE * head.row, head.width, head.height);
	}
	
	
	public static void main(String[] args) {
		
	}

	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		switch(key) {
		case KeyEvent.VK_LEFT :
			if(head.dir != Dir.R)
				head.dir = Dir.L;
			break;
		case KeyEvent.VK_UP :
			if(head.dir != Dir.D)
				head.dir = Dir.U;
			break;
		case KeyEvent.VK_RIGHT :
			if(head.dir != Dir.L)
				head.dir = Dir.R;
			break;
		case KeyEvent.VK_DOWN :
			if(head.dir != Dir.U)
				head.dir = Dir.D;
			break;
		}
	}

	

}
