import java.awt.*;
import java.awt.event.*;

public class TankClient extends Frame {

	public void launchFrame(){
		this.setLocation(200,100);
		this.setSize(800, 600);
		this.setTitle("TankWar");
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				System.exit(0);
			}
		});
		this.setResizable(false);
		setVisible(true);
	}
	
	
	
	public static void main(String[] args) {
		TankClient tc = new TankClient();
		tc.launchFrame();
	}

}
