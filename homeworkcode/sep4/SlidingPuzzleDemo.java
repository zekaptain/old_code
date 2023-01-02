/**
 * SlidingPuzzleDemo Class
 * 
 * This is for demonstrating how to use the SlidingPuzzleState class.
 * 
 * @author Eric D. Manley
 *
 */

public class SlidingPuzzleDemo 
{

	public static void main(String[] args) 
	{
		//creating a new 4 x 4 sliding puzzle
		SlidingPuzzleState p1 = new SlidingPuzzleState(4,4);
		System.out.println("Printing the initial puzzle arrangement, notice it is in order:\n"+p1); 
		System.out.println("Is this a solved puzzle? "+p1.isGoal());
		p1.shuffle(); //making a bunch of random moves on the puzzle
		System.out.println("\nAfter shuffling, the puzzle looks like this:\n"+p1);
		System.out.println("Now is it solved? "+p1.isGoal());
		
		//using a constructor which initializes the puzzle stored in a file
		SlidingPuzzleState p2 = new SlidingPuzzleState("samplePuzzle.txt");
		System.out.println("\nHere's what p2, the puzzle from samplePuzzle.txt looks like:\n"+p2);
		System.out.println("Is p2 solved? "+p2.isGoal());
		
		
		System.out.println("\nHere are all of the successor states of p2:");
		for(SlidingPuzzleState s : p2.generateSuccessors())
		{
			System.out.println(s);
		}
	}
}
