import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * The SearchDemo class includes some static methods for performing a breadth-first search,
 * depth-first search, depth-limited search, and iterative deepening search on a class
 * which implements the SearchState interface. There are also methods which demonstrate
 * how these are called on two different problems: the sliding puzzle problem and the
 * quadromino sequence problem. 
 * 
 * Various statistics are reported for any given run, with the most important being the cost
 * of the goal state that was found, the number of nodes explored, and the amount of time that
 * it took. I attempted to get some indication of how much memory was used by suggesting to the
 * JVM that it run the garbage collector before any given algorithms, and then we ask the Runtime
 * object how much memory it is using (which is not unallocated), though it doesn't seem that
 * the numbers it's giving are a reliable indication of memory usage, at least for small problems.
 * You could probably get a better number for this by doing better bookkeeping on exactly how
 * many nodes are required to be in memory at any given time (rather than the total number
 * explored in all).
 * 
 * @author Eric D. Manley
 *
 */
public class SearchDemo 
{

	/**
	 * Attempts a breadth-first search of the tree rooted at the given state.
	 * 
	 * @param s - the SearchState representing the root of a node to be used with TreeSearch
	 * @return a boolean indicating whether or not a goal state was found
	 */
	public static boolean breadthFirstSearch(SearchState s)
	{
		System.gc(); //suggest to run the garbage collector so we can get fresh measurement on memory
		long startTime = System.currentTimeMillis(); //for reporting statistics
		long maxMemoryUsage = 0; //for reporting statistics
		int nodesExplored = 0; //for reporting statistics
		ArrayList<SearchState> stillNeedToExploreList = new ArrayList<SearchState>(); //the frontier/fringe
		stillNeedToExploreList.add(s); //start with the root in the frontier
		while(!stillNeedToExploreList.isEmpty())
		{
			SearchState currentlyExploring = stillNeedToExploreList.remove(0); //removing from the front: FIFO
			nodesExplored++;
			if(currentlyExploring.isGoal())
			{
				reportSuccessStats(currentlyExploring, nodesExplored, startTime, maxMemoryUsage);
				return true; //success
			}
			
			stillNeedToExploreList.addAll(currentlyExploring.generateSuccessors());	//inserting into the end of the list: FIFO
			
			//a maybe bad attempt at estimating max memory usage
			Runtime rt = Runtime.getRuntime();
			long currMemoryUsage = rt.totalMemory()-rt.freeMemory();
			if(currMemoryUsage > maxMemoryUsage)
			{
				maxMemoryUsage = currMemoryUsage;
			}
			
		}
		
		reportFailureStats(nodesExplored, startTime, maxMemoryUsage);
		return false; //failure
	}
	
	
	/**
	 * Attempts an iterative-deepening search of the tree rooted at the given state. 
	 * This just involves calling the depthLimitedSearch method over and over with
	 * bigger depth limits until a goal state is found.
	 * 
	 * @param s - the SearchState representing the root of a node to be used with TreeSearch
	 * @return a boolean indicating whether or not a goal state was found
	 */
	public static boolean iterativeDeepeningSearch(SearchState s)
	{
		boolean foundSol = false;
		int depth = 1;
		while(!foundSol)
		{
			System.out.println("Iterative Deepening Search trying a depth limited search with a depth limit of "+depth);
			if(depthLimitedSearch(s,depth))
			{
				foundSol = true;
			}
			depth++;
		}
		return foundSol;
	}
	
	/**
	 * Attempts a depth-first search of the tree rooted at the given state. This is just a
	 * wrapper method. Since a depth-first search is the same as a depth-limited search
	 * with an infinite depth limit, we just call the depth-limited method.
	 * 
	 * @param s - the SearchState representing the root of a node to be used with TreeSearch
	 * @return a boolean indicating whether or not a goal state was found
	 */
	public static boolean depthFirstSearch(SearchState s)
	{
		return depthLimitedSearch(s,Double.POSITIVE_INFINITY);
	}
	
	/**
	 * Attempts a depth-limited search of the tree rooted at the given state.
	 * 
	 * @param s - the SearchState representing the root of a node to be used with TreeSearch
	 * @param depthLimit - the cutoff point for the depth-first search
	 * @return a boolean indicating whether or not a goal state was found
	 */
	public static boolean depthLimitedSearch(SearchState s, double depthLimit)
	{
		System.gc(); //suggest to run the garbage collector so we can get fresh measurement on memory
		long startTime = System.currentTimeMillis(); //for reporting statistics
		long maxMemoryUsage = 0; //for reporting statistics
		int nodesExplored = 0; //for reporting statistics
		ArrayList<SearchState> stillNeedToExploreList = new ArrayList<SearchState>(); //the frontier/fringe
		stillNeedToExploreList.add(s); //start with the root in the frontier
		while(!stillNeedToExploreList.isEmpty())
		{
			SearchState currentlyExploring = stillNeedToExploreList.remove(stillNeedToExploreList.size()-1); //removing from the end of the list: LIFO
			nodesExplored++;
			if(currentlyExploring.isGoal())
			{
				reportSuccessStats(currentlyExploring, nodesExplored, startTime, maxMemoryUsage);
				return true; //success
			}
			
			//make sure we don't go past the given depth limit
			if(currentlyExploring.getDepth() < depthLimit)
			{
				stillNeedToExploreList.addAll(currentlyExploring.generateSuccessors()); //adding to the end of the lsit: LIFO
			}
			
			Runtime rt = Runtime.getRuntime();
			long currMemoryUsage = rt.totalMemory()-rt.freeMemory();
			if(currMemoryUsage > maxMemoryUsage)
			{
				maxMemoryUsage = currMemoryUsage;
			}
		}
		
		reportFailureStats(nodesExplored, startTime, maxMemoryUsage);
		return false; //failure
	}
	
	/**
	 * For displaying statistics to the user about the performance of a given search algorithms
	 * when that algorithm resulted in success.
	 * 
	 * @param goalState - the goal state found by the algorithm
	 * @param nodesExplored - the number of nodes explored by the search algorithm
	 * @param startTime - the time that the search started (for calculating time elapsed)
	 * @param maxMemoryUsage - the maximum memory usage measured during the search
	 */
	public static void reportSuccessStats(SearchState goalState, int nodesExplored, long startTime, long maxMemoryUsage)
	{
		System.out.println("Found a goal with cost "+goalState.pathCost());
		System.out.println("Number of nodes explored: "+nodesExplored);
		System.out.println("Depth of goal node: "+goalState.getDepth());
		System.out.println("Max measured memory usage: "+(maxMemoryUsage/1000000.0)+" MB");
		System.out.println("Time elapsed: "+((System.currentTimeMillis()-startTime)/1000.0)+" seconds");
		System.out.println("Here's the move sequence: ");
		ArrayList<SearchState> seq = goalState.getStateSequence();
		for(SearchState seqs: seq)
		{
			System.out.println(seqs);
		}
	}
	
	/**
	 * For displaying statistics to the user about the performance of a given search algorithms
	 * when that algorithm resulted in failure.
	 * 
	 * @param nodesExplored - the number of nodes explored by the search algorithm
	 * @param startTime - the time that the search started (for calculating time elapsed)
	 * @param maxMemoryUsage - the maximum memory usage measured during the search
	 */
	public static void reportFailureStats(int nodesExplored, long startTime, long maxMemoryUsage)
	{
		System.out.println("Failed to find a goal state");
		System.out.println("Number of nodes explored: "+nodesExplored);
		System.out.println("Max measured memory usage: "+(maxMemoryUsage/1000000.0)+" MB");
		System.out.println("Time elapsed: "+((System.currentTimeMillis()-startTime)/1000.0)+" seconds");
	}
	
	
	
	/**
	 * An experiment for comparing performance of various versions of the search algorithms
	 * on sliding puzzles. Note that since some of these are not likely to finish in a short
	 * amount of time for any given puzzle, you may want to comment some of these lines out
	 * if you're trying to experiment with just one or two different algorithms.
	 * 
	 * @param puzzleFile - the name of the data file containing the sliding puzzle state
	 */
	public static void runSlidingPuzzleExperiment(String puzzleFile)
	{
		SlidingPuzzleState stateWithNoRepeats = new SlidingPuzzleState(puzzleFile);
		SlidingPuzzleState stateWithRepeats = new SlidingPuzzleState(puzzleFile);
		stateWithRepeats.setCheckForRepeatedStates(false);
		
		System.out.println("Breadth-First Search on "+puzzleFile+", with repeat state checking");
		breadthFirstSearch(stateWithNoRepeats);
		System.out.println("Breadth-First Search on "+puzzleFile+", no checking for repeat states");
		breadthFirstSearch(stateWithRepeats);
		System.out.println("Depth-First Search on "+puzzleFile+", with repeat state checking");
		depthFirstSearch(stateWithNoRepeats);
		System.out.println("Iterative-Deepening Search on "+puzzleFile+", no checking for repeat states");
		iterativeDeepeningSearch(stateWithRepeats);
	}
	
	/**
	 * An experiment for comparing performance of various versions of the search algorithms
	 * on quadromino sequencing problems. Note that since some of these are not likely to finish in a short
	 * amount of time for any given pile of quadrominos, you may want to comment some of these lines out
	 * if you're trying to experiment with just one or two different algorithms.
	 * 
	 * @param quadrominoFile - the name of the data file containing the quadrominos
	 */
	public static void runQuadrominoSequenceExperiment(String quadrominoFile)
	{
		QuadrominoSequenceState qss = new QuadrominoSequenceState(quadrominoFile);
	
		System.out.println("Breadth-First Search on "+quadrominoFile);
		breadthFirstSearch(qss);
		System.out.println("Depth-First Search on "+quadrominoFile);
		depthFirstSearch(qss);
		System.out.println("Iterative-Deepening Search on "+quadrominoFile);
		iterativeDeepeningSearch(qss);
	}
	
	
	
	//you can put your search code directly in here or make new static methods and call them from here
	//like in the examples below where we call methods that compare several different algorithms.
	public static void main(String[] args) 
	{
		runSlidingPuzzleExperiment("simple8Puzzle.txt");
		//runQuadrominoSequenceExperiment("quadromino1.txt");
	}

}
