import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * The Class QuadrominoSequenceState. Instances of this class represent partial solutions
 * to the number-quadromino-sequence search problem discussed in class. These states are
 * determined by an ordered list of currently placed quadrominos as well as a 
 * "pile" of unplaced quadrominos. Methods are included for generating successor
 * states, checking for goal states, and determining the cost of the most
 * recently placed quadromino.
 * 
 * @author Eric D. Manley
 */
public class QuadrominoSequenceState implements SearchState
{
	/** The ordered list of placed quadrominos. The quadromino at index 0 is the top quadromino and it grows down with increasing index. */
	private ArrayList<Quadromino> placedQuadrominos;
	/** The pile of unplaced quadrominos. An ordered array list data structure is used, but it need not be ordered for the problem */
	private ArrayList<Quadromino> unplacedQuadrominos;
	/** the total cost of the entire set of placed quadrominos */
	private double pathCost;
	/** a reference to this node's parent in case traversing the tree from bottom to top is necessary */
	private QuadrominoSequenceState prevState;
	/** depth in the search tree */
	private int treeDepth;

	/**
	 * Constructor for creating a start state
	 * 
	 * @param filename - name of file containing quadrominos
	 */
	public QuadrominoSequenceState(String filename)
	{
		try
		{
			//initially empty quadromino set
			placedQuadrominos = new ArrayList<Quadromino>();
			unplacedQuadrominos = new ArrayList<Quadromino>();
			//scanner for reading input file
			Scanner inFile;

			inFile = new Scanner(new File(filename));

			//really, this should stop when it gets to  the end-of-file
			while(inFile.hasNextDouble())
			{
				//read in all four doubles on this line and call the Tile constructor
				Quadromino t = new Quadromino(inFile.nextDouble(),inFile.nextDouble(),inFile.nextDouble(),inFile.nextDouble());
				//add it to the quadromino set
				unplacedQuadrominos.add(t);
			}

			inFile.close();

			prevState = null;
			pathCost = 0.0;
			treeDepth = 0;

		} catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		}
	}

	/**
	 * Copy constructor for creating a deep copy of another state and then making a move in the new state
	 * 
	 * @param parent - the state to make a copy of
	 * @param indexOfQuadrominoToPlace - index of the quadromino to remove from the unplaced pile and put in the placed sequence
	 */
	private QuadrominoSequenceState(QuadrominoSequenceState parent, int indexOfQuadrominoToPlace)
	{
		placedQuadrominos  = new ArrayList<Quadromino>(parent.placedQuadrominos);
		unplacedQuadrominos = new ArrayList<Quadromino>(parent.unplacedQuadrominos);
		placedQuadrominos.add(unplacedQuadrominos.get(indexOfQuadrominoToPlace));
		unplacedQuadrominos.remove(indexOfQuadrominoToPlace);

		pathCost = parent.pathCost + costOfLastQuadrominoPlaced();
		prevState = parent;
		treeDepth = parent.treeDepth + 1;
	}


	/**
	 * Checks if this state is a goal state
	 * 
	 * @return a boolean indicating whether or not this is a goal state
	 */
	public boolean isGoal()
	{
		return unplacedQuadrominos.isEmpty();
	}

	/**
	 * @return the depth of this node in the search tree
	 */
	public int getDepth() 
	{
		return treeDepth;
	}

	/**
	 * Calculates the penalty incurred between the last two quadrominos in the placedQuadrominos list.
	 * 
	 * @return a double representing the cost of the last quadromino in the ArrayList placedQuadrominos
	 * 		as determined by its penalty from the second to last quadromino. If there are fewer than
	 * 		two quadrominos, there is no cost associated, so we return 0.0
	 */
	private double costOfLastQuadrominoPlaced()
	{
		double rVal = 0.0; //return value defaults to 0.0 if 1 or 0 quadrominos
		int sz = placedQuadrominos.size();
		if(sz>=2)
		{	//placedQuadrominos.get(sz-1) - last quadromino; placedQuadrominos.get(sz-2) - second to last quadromino
			rVal = placedQuadrominos.get(sz-1).penaltyIfPrevQuadromino(placedQuadrominos.get(sz-2));
		}
		return rVal;
	}

	/**
	 * Computes all successor states. Here, the actions are the choices of which quadromino
	 * to place next.
	 * 
	 * @return a list of states that can be formed by removing one quadromino from the 
	 * 		unplaced list and putting at the end of the placed list
	 */
	public ArrayList<SearchState> generateSuccessors()
	{
		//the list of child states to be returned, initially empty
		ArrayList<SearchState> children = new ArrayList<SearchState>();

		//go through all of the unplaced quadrominos and generate the successor from
		//the action of placing that quadromino
		for(int i = 0; i < unplacedQuadrominos.size(); i++)
		{
			//make a copy of this one except place the ith quadromino from the unplaced pile
			QuadrominoSequenceState child = new QuadrominoSequenceState(this,i);
			children.add(child);
		}
		return children;
	}

	/**
	 * @return an ArrayList containing the sequence of states from the 
	 * starting state until this node.
	 */
	public ArrayList<SearchState> getStateSequence() 
	{
		ArrayList<SearchState> seq = new ArrayList<SearchState>();

		QuadrominoSequenceState curr = this;
		while(curr != null)
		{
			seq.add(0, curr);
			curr = curr.prevState;
		}

		return seq;
	}

	/** 
	 * accessor method for the path cost
	 * 
	 * @return the path cost of this node
	 */
	public double pathCost() 
	{
		return pathCost;
	}

	/**
	 * A toString function for used when printing the states nicely.
	 * This merely concatenates the toString results from each of the quadrominos.
	 * 
	 * @return a string representing the list of placed quadrominos
	 */
	public String toString()
	{
		String r = "/=======================\\\n";
		for(Quadromino t : placedQuadrominos)
		{
			r += t;
		}
		r += "\\=======================/\n";
		return r;
	}

}
