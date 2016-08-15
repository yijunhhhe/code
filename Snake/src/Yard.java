import java.awt.Frame;
import java.awt.Graphics;
import java.awt.*;
import java.awt.event.*;
import java.awt.Component;

public class Yard extends Frame {
	
	private boolean flag = true;
	
	public static final int ROWS = 30;
	public static final int COLUMNS = 30;
	public static final int BLOCK_SIZE = 15;
	
	Snake s = new Snake(this);
	Egg egg = new Egg();
	Image offScreenImage = null;
	public void launch(){
		this.setLocation(200,200);
		this.setSize(COLUMNS * BLOCK_SIZE, ROWS * BLOCK_SIZE);;
		this.addWindowListener(new WindowAdapter());
		this.setVisible(true);
		this.addKeyListener(new KeyMonitor());
		new Thread(new PaintThread()).start();;
	}
	
	public class WindowAdapter implements WindowListener{

		@Override
		public void windowOpened(WindowEvent e) {
			
		}

		@Override
		public void windowClosing(WindowEvent e) {
			System.exit(0);
		}

		@Override
		public void windowClosed(WindowEvent e) {
			
		}

		@Override
		public void windowIconified(WindowEvent e) {
			
		}

		@Override
		public void windowDeiconified(WindowEvent e) {
			
		}

		@Override
		public void windowActivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeactivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}
		
	}
	
	public static void main(String[] args) {
		new Yard().launch();
	}
	
	public void stop(){
		flag = false;
	}
	
	
	
	
	public void paint(Graphics g) {
		Color c = g.getColor();
		g.setColor(Color.GRAY);
		g.fillRect(0, 0, COLUMNS * BLOCK_SIZE, ROWS * BLOCK_SIZE);
		g.setColor(Color.DARK_GRAY);
		for(int i = 1; i < ROWS ; i++){
			g.drawLine(0, BLOCK_SIZE * i, COLUMNS * BLOCK_SIZE, BLOCK_SIZE * i);
		}
		for(int i = 1; i < COLUMNS ; i++){
			g.drawLine(BLOCK_SIZE * i, 0, BLOCK_SIZE * i, BLOCK_SIZE * ROWS);
		}
		g.setColor(c);
		s.eat(egg);
		egg.draw(g);
		s.draw(g);
	}
	
	public void update(Graphics g){
		if(offScreenImage == null){
			offScreenImage = this.createImage(COLUMNS * BLOCK_SIZE, BLOCK_SIZE * ROWS);
		}
		Graphics gOff = offScreenImage.getGraphics();
		paint(gOff);
		g.drawImage(offScreenImage, 0, 0, null);
	}
	
	
	private class PaintThread implements Runnable{
		public void run() {
			while(flag){
				repaint();
				try{
					Thread.sleep(200);
				} catch( InterruptedException e){
					e.printStackTrace();
				}
			}
			
		}
	}
	
	private class KeyMonitor extends KeyAdapter{
		public  void keyPressed(KeyEvent e){
			s.keyPressed(e);
		}
	}

}
