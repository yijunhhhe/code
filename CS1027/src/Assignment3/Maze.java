import java.io.*;
import java.util.*;
import javax.swing.JFrame;
import javax.swing.JPanel;


/**
 * The Maze class creates a window that shows a hexagon-tile based maze.<p>
 * 
 * The Maze is built from a file with the following specifications:<p>
 * <ul>
 * <li>The first line has the number of rows and cols</li>
 * 
 * <li>Each subsequent line (there will be the same number of lines as rows)</li>
 * 
 * <i>(Note: because this maze is based on hexagons, each alternating row is 
 *        offset from the left side by half a hexagon, indicated by a space in the input file)</i>
 *        </ul>
 * 
 * @author CS1027
 *
 */
public class Maze extends JFrame { 

	// Serialization UID
	private static final long serialVersionUID = 1L;

	// Public constants
	/**
	 * Default time delay when repainting the Maze to reflect hexagon changes
	 */
	public static final int DEFAULT_TIME_DELAY = 10;

	// Attributes
	private int timeDelay = DEFAULT_TIME_DELAY;
	Hexagon start;
	Hexagon end;


	/**
	 * Constructor to build a Graphical Maze with hexagonal tiles
	 * from a file containing a Maze specification
	 * @param inFile
	 * @throws UnknownMazeCharacterException
	 * @throws FileNotFoundException
	 * @throws IOException
	 */
	public Maze(String inFile) throws UnknownMazeCharacterException, FileNotFoundException, IOException{

		// set up GUI aspects of the Maze component
		super("Maze");
		super.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel p = new JPanel();

		// set up the file reader and read the first line
		BufferedReader in;
		String line="";
		in = new BufferedReader(new FileReader(inFile));
		line = in.readLine();

		// Tokenize the first line to get the row and column
		StringTokenizer lineTokens = new StringTokenizer(line);
		// First line is the number of rows then the number of columns
		int row = Integer.parseInt(lineTokens.nextToken());
		int col = Integer.parseInt(lineTokens.nextToken());

		// To build the maze we will make temporary use of a 2D array
		// Once built, the hexagons themselves know all of their neighbors, so we 
		//      do not need the 2D array anymore.
		// Add a row and col of nulls around the "edges" of the builder matrix (+2's)
		// This will greatly simplify the neighbor building process below
		Hexagon[][] hexMazeBuilder = new Hexagon[row+2][col+2];	

		// HexLayout will arrange the Hexagons in the window
		p.setLayout(new HexLayout(row, col, 4));

		// for each row
		for (int r = 1; r<row+1; r++){
			line = in.readLine();
			lineTokens = new StringTokenizer(line);
			// for each token on the line (col in the maze)
			for(int c = 1; c< col+1; c++){

				// read the token and generate the hexagon type
				char token = lineTokens.nextToken().charAt(0);
				switch(token){
				case 'W':
					hexMazeBuilder[r][c] = new Hexagon(Hexagon.HexType.WALL);
					break;
				case 'S':
					hexMazeBuilder[r][c] = new Hexagon(Hexagon.HexType.START);
					this.start = hexMazeBuilder[r][c];
					break;
				case 'E':
					hexMazeBuilder[r][c] = new Hexagon(Hexagon.HexType.END);
					this.end = hexMazeBuilder[r][c];
					break;
				case 'U':
					hexMazeBuilder[r][c] = new Hexagon(Hexagon.HexType.UNVISITED);
					break;
				default:
					// cannot build correct Maze
					throw new UnknownMazeCharacterException(token);
				}

				// add to the GUI layout
				p.add(hexMazeBuilder[r][c]);
			}// end for cols
		}// end for rows

		//go through the 2D matrix again and build the neighbors
		int offset = 0;
		for(int r=1;r<row+1;r++){
			for(int c=1;c<col+1;c++){
				// on even rows(inset from left side) need to add one to the upper and lower neighbors
				// on odd, do not add anything (offset should be 0)
				offset = 1 - r%2;

				// set the neighbors for this hexagon in the builder
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r-1][c+offset], 0);
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r][c+1], 1);
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r+1][c+offset], 2);
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r+1][c-1+offset], 3);
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r][c-1], 4);
				hexMazeBuilder[r][c].setNeighbour(hexMazeBuilder[r-1][c-1+offset], 5);
			} // end for cols
		} // end for rows

		//close the file
		in.close();

		//set up the GUI window
		this.add(p);
		this.pack();
		this.setSize(30*row,30*col );
		this.setVisible(true);
	}


	/**
	 * Method will return a reference to the hexagon that is the
	 * start of the maze.
	 * @return A reference to the hexagon that is the start of the maze
	 */
	public Hexagon getStart(){
		return this.start;
	}
	
	/**
	 * Method will return a reference to the hexagon that is the
	 * end of the maze.
	 * @return A reference to the hexagon that is the end of the maze
	 */
	public Hexagon getEnd(){
		return this.end;
	}

	/**
	 * Get the current time delayed used when repainting the Maze to reflect changes
	 * made to the hexagon tiles
	 * @return the timeDelay
	 */
	public int getTimeDelay() {
		return timeDelay;
	}

	/**
	 * Set the amount of time to wait when repainting the Maze to reflect changes 
	 * made to the hexagon tiles
	 * @param timeDelay the timeDelay to set
	 */
	public void setTimeDelay(int timeDelay) {
		this.timeDelay = timeDelay;
	}

	@Override
	/**
	 * This method will update the maze to reflect any changes to the hexagonal 
	 * tiles it shows.  The method includes a time delay, which can be changed
	 * with the setDelay method.
	 */
	public void repaint() {
		try {
			Thread.sleep(this.timeDelay);
		}catch(Exception e){ 
			System.err.println("Error while issuing time delay\n" + e.getMessage());
		}
		super.repaint();
	}

}
