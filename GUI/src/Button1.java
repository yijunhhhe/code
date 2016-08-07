import java.awt.BorderLayout;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Button1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Button1 gui = new Button1();
		gui.go();
	}
	
	public void go(){
		JFrame frame = new JFrame();
		JButton button = new JButton("click u mean it");
		Font bigFont = new Font("serif", Font.BOLD, 28);
		button.setFont(bigFont);
		frame.getContentPane().add(BorderLayout.NORTH,button);
		frame.setSize(300, 300);
		frame.setVisible(true);
	}

}
