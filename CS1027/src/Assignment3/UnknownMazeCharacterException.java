/**
 * This exception is thrown by Maze a character is encountered 
 * during Maze building that the Maze cannot recognize.
 * 
 * @author CS1027
 * 
 */
public class UnknownMazeCharacterException extends RuntimeException{
  
	/**
	   * Sets up this exception with an appropriate message.
	   * @param c char that was used while building maze which was unknown
	   */
	  public UnknownMazeCharacterException (char c)
	  {
	    super ("Unknown character: " + c);
	  }
}
