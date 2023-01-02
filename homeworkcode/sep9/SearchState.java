import java.util.ArrayList;

/**
 * SearchState Interface. This contains all of the necessary methods to run various
 * search algorithms on a problem. A search algorithm like breadth-first search or 
 * depth-first search can be written for a generic search problem using this type,
 * and then any class that implements this interface will work with that alogorithm.
 * 
 * @author Eric D. Manley
 *
 */
public interface SearchState 
{
	public int getDepth();
	public ArrayList<SearchState> getStateSequence();
	public boolean isGoal();
	public ArrayList<SearchState> generateSuccessors();
	public double pathCost();
}
