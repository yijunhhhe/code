import java.io.FileNotFoundException;
import java.io.IOException;

public class MazeSolver1 {

	public static void main (String[]args) throws UnknownMazeCharacterException, FileNotFoundException, IOException{
		
		int stepCounter = 0;                     // bookkeeping counter
		int hexagonOnStack = 0;                  // bookkeeping counter
		
		try{
			if(args.length<1){
				throw new IllegalArgumentException ("No Maze Provided");
			}
		
		String mazeFileName = args[0]; 
		
		Maze maze = new Maze(mazeFileName);        // Creating a maze object and trying to open maze file
		
		ArrayStack<Hexagon> stack1 = new ArrayStack<Hexagon>();                // Creating a Stack
		Hexagon start = maze.getStart();           // Reference starting Hexagon from the maze
		
	
		stack1.push(start);                      // Push 
		Hexagon hexagon = null;
		Hexagon neighbour ;
		
		
		while (!stack1.isEmpty()){                       // While stack is not empty
			hexagon = stack1.pop();        // Pop
			stepCounter++;                       // Increase the step counter
			hexagonOnStack--;                    // Decrease the hex counter
			if (hexagon.isEnd()){                 // If Hexagon is end tile, we call the SetProcessed tile in order to change it's type
				hexagon.setProcessed();
				break;                       
			}
			else{
				for (int i = 0; i < 6; i++){                      // Look through each neighbour
				neighbour= hexagon.getNeighbour(i); 
				if (neighbour != null && !neighbour.isWall() && neighbour.isUnvisited()){
					stack1.push(neighbour);
					hexagonOnStack++; 
					neighbour.setPushed();
				}
				}
			}			
			hexagon.setProcessed();                           // Set current Hexagon as processed
			maze.repaint();                                   // Update maze window

		}
		
		if (hexagon.isEnd()){
			System.out.println("We found the end!");                       // Print once we find the end
		}
		
		System.out.println("The number of steps it took to finish is" + stepCounter);            // Print the number of steps it took to finish
		System.out.println("The number of tiles still on the stack is:" + hexagonOnStack);       // Print the number of tiles still on the stack

		}catch(IllegalArgumentException e ){  // catch the exception
			System.out.println("No Maze Provided");
		}	
		
	}
	
}

