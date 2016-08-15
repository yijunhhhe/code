import java.awt.*;
import java.awt.event.*;

public class TankClient extends Frame {
	
	public static final int GAME_WIDTH = 800;
	public static final int GAME_HEIGHT = 600;
	
	int x = 50;
	int y = 50;
	
	Image offScreenImage = null;
	

	public void paint(Graphics g){
		Color c = g.getColor();	
		g.setColor(Color.red);
		g.fillOval(x, y, 30, 30);
		g.setColor(c);
		x++;
		y++;
	}
	
	public void update(Graphics g) {
		if(offScreenImage == null){
			offScreenImage = this.createImage(GAME_WIDTH, GAME_HEIGHT);		
		}
		Graphics gOffScreen = offScreenImage.getGraphics();
		Color c = gOffScreen.getColor();
		gOffScreen.setColor(Color.GREEN);
		gOffScreen.fillRect(0, 0, 800, 600);
		gOffScreen.setColor(c);
		paint(gOffScreen);
		g.drawImage(offScreenImage, 0, 0, null);
	}
	
	
	public void launchFrame(){
		this.setLocation(200,100);
		this.setSize(GAME_WIDTH, GAME_HEIGHT);
		this.setTitle("TankWar");
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				System.exit(0);
			}
		});
		this.setResizable(false);
		this.setBackground(Color.GREEN);
		this.addKeyListener(new KeyMonitor());
		setVisible(true);
		new Thread(new PaintThread()).start();
	}
	
	
	
	public static void main(String[] args) {
		TankClient tc = new TankClient();
		tc.launchFrame();
	}
	
	private class PaintThread implements Runnable{
		public void run(){
			while(true){
				repaint();
				try {
					Thread.sleep(30);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}
	private class KeyMonitor extends KeyAdapter{
		
		public void keyPressed(KeyEvent e) {
			int key = e.getKeyCode();
			if(key == com.sun.glass.events.KeyEvent.VK_RIGHT){
				
			}
		}
	}
}

