import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.event.*;

public class SimpleGui1B{
	JButton buttonColor, buttonLabel;
	JFrame frame;
	JLabel label;
	public static void main(String[] args){
		SimpleGui1B gui = new SimpleGui1B();
		gui.go();
	}
	
	public void go(){
		frame = new JFrame();
		label = new JLabel("label");
		buttonColor  = new JButton("click me");
		buttonLabel = new JButton("change label");
		MyDrawPanel panel = new MyDrawPanel();
		
	
		buttonLabel.addActionListener(new LabelListener());
		buttonColor.addActionListener(new ColorListener());
		
		frame.getContentPane().add(BorderLayout.WEST, label);
		frame.getContentPane().add(panel);
		frame.getContentPane().add(BorderLayout.SOUTH, buttonColor);
		frame.getContentPane().add(BorderLayout.EAST, buttonLabel);
		frame.repaint();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300, 300);
		frame.setVisible(true);		
	}
	
	class LabelListener implements ActionListener{
		public void actionPerformed(ActionEvent event){
			label.setText("hey");
		}
	}
	
	class ColorListener implements ActionListener{
		public void actionPerformed(ActionEvent event){
			frame.repaint();
		}
	}
	
	
	
		
		
}

