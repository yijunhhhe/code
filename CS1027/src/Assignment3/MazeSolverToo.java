/**
 * class represents how a hexagon go from the start to the end
 * @author Yijun He
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
		
		/*
		 * create a maze
		 */
		Maze maze = new Maze(mazeFileName);
		
		/*
		 * create a start hexagon
		 */
		Hexagon start = maze.getStart();
		
		/*
		 * create a priority queue for hexagon
		 */
		LinkedPriorityQueue<Hexagon> priorityQueue = new LinkedPriorityQueue<Hexagon>();
		
		/*
		 * create a dequeue variable storing dequeued hexagon
		 */
		Hexagon dequeue = null;
		
		/*
		 * create a neighbor variable storing hexagon's neighbor
		 */
		Hexagon neighbor = null;
		
		/*
		 * store each hexagon's priority
		 */
		double priority = 0;
		
		/*
		 * keep track of number of step
		 */
		int numberOfStep = 0;
		
		/*
		 * keep track of hexagonOnQueue
		 */
		int hexagonOnQueue = 1;
		
		/*
		 * variable for a hexagon's distance to the end
		 */
		double distanceToEnd = 0;
		
		/*
		 * enqueue start hexagon in the queue
		 */
		priorityQueue.enqueue(start);
		double stepToMe = 0;
		while(!priorityQueue.isEmpty()){
			dequeue = priorityQueue.dequeue();
			dequeue.setDequeued();
			//stepToMe++;
			numberOfStep++;
			hexagonOnQueue--;
			// if dequeued hexagon is the end exit the while loop
			if(dequeue.isEnd()){
				dequeue.setFinished();
				break;
			}else {
				// for each neighbor 
				for(int i = 0; i < 6; i++){
					neighbor = dequeue.getNeighbour(i);
					// if neighbor meet the requirement, calculate the priority and enqueue it in the queue
					if(neighbor != null && !neighbor.isWall() && !neighbor.isEnqueued() && !neighbor.isDequeued() && !neighbor.isStart()){
						//stepToMe = start.distanceToEnd(maze) - neighbor.distanceToEnd(maze);
						neighbor.setSteps(dequeue.getSteps()+1);
						
						//neighbor.setSteps(stepToMe);	
						//stepToMe = neighbor.getSteps();
						distanceToEnd = neighbor.distanceToEnd(maze);
						priority = neighbor.getSteps() + neighbor.distanceToEnd(maze);
						priorityQueue.enqueue(neighbor, priority);	
						neighbor.setEnqueued();
						hexagonOnQueue++;
						stepToMe = neighbor.getSteps();
						//System.out.println("step to me: " + neighbor.getSteps() + "HexagonOnQueue" + hexagonOnQueue + "  distance to end: "+  distanceToEnd +"  priority: "+ priority);
					}
				}
			}
			//dequeue.setEnqueued();
			System.out.println("step to me: " + stepToMe + "Number of Step: "+ numberOfStep + " HexagonOnQueue" + hexagonOnQueue + "  distance to end: "+  distanceToEnd +"  priority: "+ priority);
			// repaint the maze
			maze.repaint();			
		}
		// whether the dequeued hexagon is the end or not, print the result
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
