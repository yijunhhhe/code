

 
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Polygon;
import java.awt.Rectangle;
import java.awt.event.MouseEvent;

import javax.swing.Action;
import javax.swing.Icon;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JToggleButton;
import javax.swing.SwingUtilities;
 
/**
 * A six sided component. This is not guaranteed to be a perfect hexagon, it is just guaranteed to have six sides in
 * the form of a hexagon. To be a perfect hexagon the size of this component must have a height to width ratio of
 * 1 to 0.866
 *
 * @author keang
 * @date 5 Jun 2009
 *
 */

public class HexComponent extends JComponent{
	private static final long serialVersionUID = 4865976127980106774L;
	 
	private Polygon hexagon = new Polygon();
	
  
		@Override
		public boolean contains(Point p)
	    {
			return hexagon.contains(p);
	    }
	 
		@Override
		public boolean contains(int x, int y)
	    {
			return hexagon.contains(x, y);
	    }
	 
		@Override
		public void setSize(Dimension d)
	    {
			super.setSize(d);
			calculateCoords();
	    }
	 
		@Override
		public void setSize(int w, int h)
	    {
			super.setSize(w, h);
			calculateCoords();
	    }
	 
		@Override
		public void setBounds(int x, int y, int width, int height)
	    {
			super.setBounds(x, y, width, height);
			calculateCoords();
	    }
	 
		@Override
		public void setBounds(Rectangle r)
	    {
			super.setBounds(r);
			calculateCoords();
	    }
	 
		@Override
		protected void processMouseEvent(MouseEvent e)
	    {
			if ( contains(e.getPoint()) )
				super.processMouseEvent(e);
	    }
	 
		private void calculateCoords()
	    {
			int w = getWidth()-1;
			int h = getHeight()-1;
	 
			int ratio = (int)(h*.25);
			int nPoints = 6;
			int[] hexX = new int[nPoints];
			int[] hexY = new int[nPoints];
	 
		    agressiveCoords(w, h, ratio, hexX, hexY);

		    hexagon = new Polygon(hexX, hexY, nPoints);
	    }
	 
	 
		private void agressiveCoords(int w, int h, int ratio, int[] hexX, int[] hexY) {
			hexX[0] = w/2;
		    hexY[0] = 0;
	 
		    hexX[1] = w;
		    hexY[1] = ratio;
	 
		    hexX[2] = w;
		    hexY[2] = h - ratio;
	 
		    hexX[3] = w/2;
		    hexY[3] = h;
	 
		    hexX[4] = 0;
		    hexY[4] = h - ratio;
	 
		    hexX[5] = 0;
		    hexY[5] = ratio;
		}
		  
		@Override
		protected void paintComponent(Graphics g)
	    {		
			g.setColor(getBackground());
		    g.fillPolygon(hexagon);
		    g.setColor(getForeground());
		    g.drawPolygon(hexagon);
	    }
	 
		@Override
		protected void paintBorder(Graphics g)
	    {
			// do not paint a border
	    }
	 
}
