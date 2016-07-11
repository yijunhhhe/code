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
		int stepCounter = 0, hexagonOnStack = 0;
		ArrayStack<Hexagon> stack = new ArrayStack<Hexagon>();
		stack.push(maze.getStart());
		hexagonOnStack++;		
		Hexagon popHexagon = null;
		Hexagon neighbor;
		while(!stack.isEmpty()){
			popHexagon = stack.pop();
			stepCounter++;
			hexagonOnStack--;
			if (popHexagon.isEnd()){
				popHexagon.setProcessed();
				break;
			}else{
				for(int i = 0; i < 6; i++){
					neighbor = popHexagon.getNeighbour(i);
					if (neighbor == null){
						continue;
					} else if (!neighbor.isWall() && neighbor.isUnvisited()){
						stack.push(neighbor);
						neighbor.setPushed();
						hexagonOnStack++;
						System.out.println(neighbor);
					}
				}
			}
			popHexagon.setProcessed();
			maze.repaint();
		}
		if(popHexagon.isEnd()){
			System.out.println("Number of steps that it took to finish: " + stepCounter);
			System.out.println("Number of tiles still on the stack: " + hexagonOnStack);
		}
			
	}

	
	
}
