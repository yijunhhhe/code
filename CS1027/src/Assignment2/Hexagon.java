import java.awt.Color;

/**
 * This class represents a pointed-top Hexagon tile used to make up a <code>Maze</code> object.
 * <p>
 * Each tile has a type.  It can be a Wall, Start, End, Unvisited, Visited or Pushed tile.
 * Each tile type will be a different colour: black, green, red, cyan, blue and magenta respectively.
 * <p>
 * Hexagon tiles know about their neighbors (if set using setNeighbor method).
 * <p>
 * The neighbors of a tile are accessed by an index 0-5 inclusive.
 * <ul>
 *        <li> The hexagons are pointed-top in orientation, the 0 index is the upper-right side</li>
 *        <li> Indexes for the sides progress incrementally clockwise from the 0 index, to 5 on the upper-left side</>
 * </ul>
 * Eg.<p>
 *<code>    5 /  \ 0</code><p>
 *<code>    4 |  | 1</code><p>
 *<code>    3 \  / 2</code><p>
 * @author CS1027
 *
 */
public class Hexagon extends HexComponent
{
	// constants
	private static final Color WALL_COLOR = Color.BLACK;
	private static final Color START_COLOR = Color.GREEN;
	private static final Color END_COLOR = Color.YELLOW;
	private static final Color UNVISITED_COLOR = Color.CYAN;
	private static final Color PROCESSED_COLOR = Color.BLUE;
	private static final Color PUSHED_COLOR = Color.MAGENTA;
	private static final Color END_PROCESSED_COLOR = Color.RED;
	private static final Color START_PROCESSED_COLOR = Color.PINK;

	//enum to represent available hexagon types
	public static enum HexType{WALL, START, END, UNVISITED, PROCESSED, PUSHED, END_PROCESSED, START_PROCESSED};
	
	
	// Attributes	
	private HexType type;    // Stores the type of Hexagon this currently is  
	private boolean isStart;  // Is this the start?
	private boolean isEnd;    // Is this the end?
	private Hexagon[] neighbors; // Stores the hexagons which surround this one on each of 6 sides

	
/**
 * Create a Hexagon tile of the specified type 
 * @param t the HexType to create
 */
	public Hexagon(HexType t){
		this.type = t;
		this.isStart = t==HexType.START;
		this.isEnd = t==HexType.END;
		
		//set the initial color based on the initial type
		this.setColor(this.type);
		//allocate space for the neighbor array
		this.neighbors = new Hexagon[6];
	}

	/**
	 * Set the neighbor for this hexagon using the neighbor index.
	 * 
	 * The index for the neighbor indicates which side of the hexagon
	 * this new neighbor is on.  0-5 inclusive.
	 * 
	 * @param neighbor The new Hexagon neighbor
	 * @param i The index specifying which side this neighbor is on (0-5 inclusive)
	 * @throws InvalidNeighborIndexException When an index is specified that is not 0-5 inclusive.
	 */
	public void setNeighbour(Hexagon neighbor, int i) throws InvalidNeighbourIndexException{
		if (0<=i && i <=5)
			this.neighbors[i] = neighbor;
		else 
			throw new InvalidNeighbourIndexException(i);
	}
	
	/**
	 * Returns the neighbor for this hexagon using the neighbor index
	 * 
	 * The index for the neighbor indicates which side of the hexagon
	 * the neighbor to get is on.  0-5 inclusive.
	 * 
	 * @param i The index indicating the side of the hexagon this neighbor is on
	 * @return The hexagon the is on the i-th side of the current hexagon, or null if no neighbor
	 * @throws InvalidNeighbourIndexException When an index is specified that is not 0-5 inclusive.
	 */
	public Hexagon getNeighbour(int i) throws InvalidNeighbourIndexException{
		if (0<=i && i <=5)
			return this.neighbors[i];
		else 
			throw new InvalidNeighbourIndexException(i);
	}

	/**
	 * This method checks if the current hexagon is a Wall tile.
	 * @return true if this is a Wall tile, false otherwise.
	 */
	public boolean isWall(){
		return type == HexType.WALL;
	}
	/**
	 * This method checks if the current hexagon is a Visited tile.
	 * @return true if this is a Visited tile, false otherwise.
	 */
	public boolean isProcessed(){
		return type == HexType.PROCESSED;
	}
	/**
	 * This method checks if the current hexagon is an Unvisited tile.
	 * @return true if this is an Unvisited tile, false otherwise.
	 */
	public boolean isUnvisited(){
		return type == HexType.UNVISITED || (this.isEnd() && type==HexType.END);
	}
	/**
	 * This method checks if the current hexagon is a Start tile.
	 * @return true if this is a Start tile, false otherwise.
	 */
	public boolean isStart(){
		return this.isStart;
	}
	/**
	 * This method checks if the current hexagon is an End tile.
	 * @return true if this is an End tile, false otherwise.
	 */
	public boolean isEnd(){
		return this.isEnd;
	}

	/**
	 * This method sets the tile to be a Pushed tile
	 * and updates the tile's colour
	 */
	public void setPushed(){
		this.type = HexType.PUSHED;
		this.setColor(this.type);
	}
	
	/**
	 * This method set the tile to be a Visited tile
	 * and updates the tile's colour
	 */
	public void setProcessed(){
		this.type = HexType.PROCESSED;
		if (isEnd){
			this.type = HexType.END_PROCESSED;
		}
		if (isStart){
			this.type = HexType.START_PROCESSED;
		}
			
		this.setColor(this.type);
	}
	
	
	/**
	 * Helper method to set the current tile color based on the 
	 * type of tile.
	 * @param t The type to use to set the color
	 */
	private void setColor(HexType t){
		switch(t){
		case WALL:
			this.setBackground(WALL_COLOR);
			break;
		case START:
			this.setBackground(START_COLOR);
			break;
		case END:
			this.setBackground(END_COLOR);
			break;
		case UNVISITED:
			this.setBackground(UNVISITED_COLOR);
			break;
		case PROCESSED:
			this.setBackground(PROCESSED_COLOR);
			break;
		case PUSHED:
			this.setBackground(PUSHED_COLOR);
			break;
		case END_PROCESSED:
			this.setBackground(END_PROCESSED_COLOR);
			break;
		case START_PROCESSED:
			this.setBackground(START_PROCESSED_COLOR);
			break;
		default:
			this.setBackground(WALL_COLOR);
			break;
		}
		this.setForeground(Color.BLACK);
	}

}