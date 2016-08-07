import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class FlowLayout {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FlowLayout gui = new FlowLayout();
		gui.go();
	}
	
	public void go(){
		JFrame frame = new JFrame();
		JButton button = new JButton("click");
		JButton button1 = new JButton("me");
		JButton button2 = new JButton("plz");
		JPanel panel = new JPanel();
		JTextField field = new JTextField(20);
		JTextField field1 = new JTextField("Your name");
		panel.add(field1);
		panel.add(button);
		panel.add(button1);
		panel.add(button2);
		panel.setBackground(Color.darkGray);
		panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
		frame.getContentPane().add(BorderLayout.EAST, panel);
		frame.setSize(300, 300);
		frame.setVisible(true);		
		
	}
}
