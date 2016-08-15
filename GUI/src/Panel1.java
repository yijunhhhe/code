import java.awt.*;

public class Panel1 {

	public static void main(String[] args) {
		Frame frame = new Frame();
		Panel panel = new Panel();
		panel.setBackground(Color.black);
		panel.setBounds(10, 10, 100, 100);
		frame.setBounds(300, 500, 300, 300);
		frame.add(panel);
		frame.setVisible(true);
		
	}

}
