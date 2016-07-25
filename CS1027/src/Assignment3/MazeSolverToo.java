/**
 * ??
 *
 * @author 
 * @author 
 * @version
 */
 
import java.io.*;

public class MazeSolverToo {
	
	/**
	 * @param args
	 * @throws IOException 
	 * @throws FileNotFoundException 
	 * @throws UnknownMazeCharacterException 
	 */
	public static void main (String[] args) throws UnknownMazeCharacterException, FileNotFoundException, IOException {
		try{
			if(args.length<1){
				throw new IllegalArgumentException("No Maze Provided");
		}
		/*
		 * get the maze file name 
		 */
		String mazeFileName = args[0];
		Maze maze = new Maze(mazeFileName);
		Hexagon start = maze.getStart();
		LinkedPriorityQueue<Hexagon> priorityQueue = new LinkedPriorityQueue<Hexagon>();
		priorityQueue.enqueue(start);
		Hexagon dequeue = null;
		Hexagon neighbor = null;
		double stepToMe = 0;
		double priority;
		int numberOfStep = 0;
		int hexagonOnQueue = 1;
		double distanceToEnd;
		
		
		
		while(!priorityQueue.isEmpty()){
			dequeue = priorityQueue.dequeue();
			dequeue.setDequeued();
			//stepToMe++;
			numberOfStep++;
			hexagonOnQueue--;
			
			if(dequeue.isEnd()){
				dequeue.setFinished();
				break;
			}else {
				
				for(int i = 0; i < 6; i++){
					neighbor = dequeue.getNeighbour(i);
					if(neighbor != null && !neighbor.isWall() && !neighbor.isEnqueued() && !neighbor.isDequeued() && !neighbor.isStart()){
						//stepToMe = start.distanceToEnd(maze) - neighbor.distanceToEnd(maze);
						neighbor.setSteps(dequeue.getSteps()+1);
						stepToMe++;
						//neighbor.setSteps(stepToMe);	
						//stepToMe = neighbor.getSteps();
						distanceToEnd = neighbor.distanceToEnd(maze);
						priority = neighbor.getSteps() + neighbor.distanceToEnd(maze);
						System.out.println("step to me: " + neighbor.getSteps() + "  distance to end: "+  distanceToEnd +"  priority: "+ priority);
						priorityQueue.enqueue(neighbor, priority);	
						neighbor.setEnqueued();
						hexagonOnQueue++;
					}
				}
			}
			//dequeue.setEnqueued();
			maze.repaint();			
		}
		if(dequeue.isEnd()){
		System.out.format("the end is found, the number of step to finish %d\n"
				+ "tiles still in priority queue: %d \n"
				+ "Number of step taken: %f", numberOfStep, priorityQueue.size(), dequeue.getSteps()+1);
		}else {
			System.out.println("Not found, tiles still in priority queue: " + priorityQueue.size() + ", The number of step to finish: " + numberOfStep );
		}
		} catch(IllegalArgumentException e ){  // catch the exception
			System.out.println("No Maze Provided");
		}	
		
	}
}
