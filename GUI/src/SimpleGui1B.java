import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.event.*;

public class SimpleGui1B implements ActionListener {
	JButton button, button1;
	JFrame frame;
	JLabel label;
	public static void main(String[] args){
		SimpleGui1B gui = new SimpleGui1B();
		gui.go();
	}
	
	public void go(){
		frame = new JFrame();
		label = new JLabel("label");
		button  = new JButton("click me");
		button1 = new JButton("change label");
		MyDrawPanel panel = new MyDrawPanel();
		
	
		button.addActionListener(this);
		button1.addActionListener(this);
		
		frame.getContentPane().add(BorderLayout.WEST, label);
		frame.getContentPane().add(panel);
		frame.getContentPane().add(BorderLayout.SOUTH, button);
		frame.getContentPane().add(BorderLayout.EAST, button1);
		frame.repaint();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300, 300);
		frame.setVisible(true);
		
		
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == button){
		frame.repaint();
		} else{
			label.setText("suck my d");
		}
		
		
	}
}
