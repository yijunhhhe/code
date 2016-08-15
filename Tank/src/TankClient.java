import java.awt.Frame;

public class TankClient extends Frame {

	public void launchFrame(){
		this.setLocation(200,200);
		this.setSize(800, 600);
		setVisible(true);
	}
	
	
	
	public static void main(String[] args) {
		TankClient tc = new TankClient();
		tc.launchFrame();
	}

}
