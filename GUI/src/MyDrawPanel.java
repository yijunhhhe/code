import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

public class MyDrawPanel extends JPanel {

	public void paintComponent(Graphics g){
		Graphics2D g2d = (Graphics2D)g;
		
		int red = (int)(Math.random() * 255);
		int green = (int)(Math.random() * 255);
		int blue = (int)(Math.random() * 255);
		
		Color startColor = new Color(red,green,blue);
		
		red = (int)(Math.random() * 255);
		green  = (int)(Math.random() * 255);
		blue = (int)(Math.random() * 255);
		
		Color endColor = new Color(red, green, blue);
		
		GradientPaint gradient = new GradientPaint(50, 50, startColor, 150, 150, endColor);
		g2d.setPaint(gradient);
		//g.setColor(Color.orange);
		g2d.fillRect(50, 70, 100, 100);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
