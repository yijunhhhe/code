import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * 
 * class represents how a hexagon start from starting point in a maze
 * to the ending point by pushing and popping hexagon in the stack
 * @author Yijun He
 * 
 */
public class MazeSolver {	

	public static void main(String[] args) throws IllegalArgumentException, UnknownMazeCharacterException, FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		// check if no file name then throw an exception
		try{
			if(args.length<1){
				throw new IllegalArgumentException("No Maze Provided");
		}
		/*
		 * get the maze file name 
		 */
		String mazeFileName = args[0];
		
		/*
		 * initialize a maze 
		 */
		Maze maze = new Maze(mazeFileName);
		
		/*
		 * initialize a hexagon for the starting point of the maze
		 */
		Hexagon startHexagon = maze.getStart();
		
		/*
		 * define a stepCounter and a hexagonOnstack variable
		 */
		int stepCounter = 0, hexagonOnStack = 0;
		
		/*
		 * define a popHexagon storing the value when stack pops
		 */
		Hexagon popHexagon = null;
		
		/*
		 * define a neighbor variable storing hexagon's neighbor
		 */
		Hexagon neighbor;
		
		/*
		 * define a stack storing hexagon
		 */
		ArrayStack<Hexagon> stack = new ArrayStack<Hexagon>();
		
		// push starthexagon into stack 
		stack.push(startHexagon);
		hexagonOnStack++;		
		
		while(!stack.isEmpty()){
			popHexagon = stack.pop();
			stepCounter++;
			hexagonOnStack--;
			// if popHexagon is the end then process and quit while loop
			if (popHexagon.isEnd()){
				popHexagon.setProcessed();
				break;
			}else{
				// for each neighbor
				for(int i = 0; i < 6; i++){
					neighbor = popHexagon.getNeighbour(i);
					// if neighbor is null then continue to next one
					if (neighbor == null){
						continue;
					} else if (!neighbor.isWall() && neighbor.isUnvisited()){
						stack.push(neighbor);
						neighbor.setPushed();
						hexagonOnStack++;
					}
				}
			}
			// after checking popHexagon's neighbor process the popHexagon
			popHexagon.setProcessed();
			// repaint the maze
			maze.repaint();
		}		
		// if the end is found then print information
		if(popHexagon.isEnd()){
			System.out.println("We find the end");
		} else {
			System.out.println("We didn't find the end");
		}
		// print the stepCounter and how many hexagon on the stack
		System.out.println("Number of steps that it took to finish: " + stepCounter);
		System.out.println("Number of tiles still on the stack: " + hexagonOnStack);
		}catch(IllegalArgumentException e ){  // catch the exception
			System.out.println("No Maze Provided");
		}	
	}	
}
