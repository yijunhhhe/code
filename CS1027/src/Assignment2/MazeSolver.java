import java.io.FileNotFoundException;
import java.io.IOException;

public class MazeSolver {
	
	

	public static void main(String[] args) throws IllegalArgumentException, UnknownMazeCharacterException, FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		if(args.length<1){
			throw new IllegalArgumentException("No Maze Provided");
		}
		
		String mazeFileName = args[0];
		
		Maze maze = new Maze(mazeFileName);
		
		Hexagon startHexagon = new Hexagon(Hexagon.HexType.START);
		
		ArrayStack stack = new ArrayStack();
		stack.push(startHexagon);
		
		int stepCounter = 0, hexagonOnStack = 0;
		
			
	}

	
	
}
