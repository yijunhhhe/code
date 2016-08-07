import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.event.*;

public class SimpleGui1B  {
	JButton labelButton, Colorbutton;
	JFrame frame;
	JLabel label;
	public static void main(String[] args){
		SimpleGui1B gui = new SimpleGui1B();
		gui.go();
	}
	
	public void go(){
		frame = new JFrame();
		label = new JLabel("label");
		Colorbutton  = new JButton("click me");
		labelButton = new JButton("change label");
		MyDrawPanel panel = new MyDrawPanel();
	
		Colorbutton.addActionListener(new ColorListener());
		labelButton.addActionListener(new LabelListener());
		
		frame.getContentPane().add(BorderLayout.WEST, label);
		frame.getContentPane().add(panel);
		frame.getContentPane().add(BorderLayout.SOUTH, Colorbutton);
		frame.getContentPane().add(BorderLayout.EAST, labelButton);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300, 300);
		frame.setVisible(true);
		
		
		
	}

	class LabelListener implements ActionListener{
		public void actionPerformed(ActionEvent event){
			label.setText("Hey");
		}
	}
	
	class ColorListener implements ActionListener{
		public void actionPerformed(ActionEvent event){
			frame.repaint();
		}
	}
	
}
