import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;

public class Egg {
	public int getRow() {
		return row;
	}

	public void setRow(int row) {
		this.row = row;
	}

	public int getColumn() {
		return column;
	}

	public void setColumn(int column) {
		this.column = column;
	}




	int row, column;
	int width = Yard.BLOCK_SIZE;
	int height = Yard.BLOCK_SIZE;
	private static Random r = new Random();
	
	public Egg(int row, int column) {
		this.row = row;
		this.column = column;
	}
	
	public Egg(){
		this(r.nextInt(Yard.ROWS - 2) + 2, r.nextInt(Yard.COLUMNS));
	}
	
	public void reAppear(){
		this.row = r.nextInt(Yard.ROWS - 2) + 2;
		this.column = r.nextInt(Yard.COLUMNS);
	}
	
	public Rectangle getRect(){
		return new Rectangle(Yard.BLOCK_SIZE * column, Yard.BLOCK_SIZE * row, width, height);
	}
	
	public void draw(Graphics g){
		Color c = g.getColor();
		g.setColor(Color.GREEN);
		g.fillOval(Yard.BLOCK_SIZE * column, Yard.BLOCK_SIZE * row , width, height);
		g.setColor(c);
	}




	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
