import java.util.ArrayList;
import java.util.Scanner;

/**
 * The SkirmishCode class contains the main method which runs the game loop 
 * and has implementations for various human and AI players.
 * 
 * @author Eric D. Manley
 *
 */
public class SkirmishCode 
{
	static Scanner keyboard = new Scanner(System.in);

	public static void main(String[] args) 
	{
		GameState g = new GameState(4); //Creates the starting state
		
		System.out.println("Current Board:\n"+g); //prints out the starting state
		
		//run the game loop until a call to terminalTest() causes us to break out
		while(true)
		{
			//uncomment exactly one of the following three lines, based on how P1 should make its move
			g = humanP1(g);
			//g = randomAIP1(g);
			//g = minimaxAIP1(g);
			
			
			System.out.println("After P1's move:\n"+g);
			
			if(g.terminalTest()) //the game is over
			{
				if(g.utility() > 0)
					System.out.println("P1 wins!");
				else
					System.out.println("P2 wins!");
				break;
			}
			
			//uncomment exactly one of the following three lines, based on how P2 should make its move
			//g = humanP2(g);
			g = randomAIP2(g);
			//g = minimaxAIP2(g);
					
			System.out.println("After P2's move:\n"+g);

			if(g.terminalTest())  //the game is over
			{
				if(g.utility() > 0)
					System.out.println("P1 wins!");
				else
					System.out.println("P2 wins!");
				break;
			}
		}
		

	}
	
	/**
	 * Given a game state, this method generates all possible boards resulting from 
	 * legal moves Player 1 can make, prints them out and asks the user to select one.
	 * 
	 * @param g - the current game state
	 * @return - the new game state selected by the user
	 */
	public static GameState humanP1(GameState g)
	{
		ArrayList<GameState> movesP1CouldMake = g.p1TurnGenerateSuccessors();
		
		System.out.println("Here's the moves P1 could make:\n");
		for(int i = 0; i < movesP1CouldMake.size(); i++)
		{
			GameState s = movesP1CouldMake.get(i);
			System.out.println(i+":\n"+s);
		}
		
		System.out.print("P1's move? ");
		int moveIndex = keyboard.nextInt();
		GameState newGameState = movesP1CouldMake.get(moveIndex);
		return newGameState;
	}
	
	/**
	 * Given a game state, this method generates all possible boards resulting from 
	 * legal moves Player 2 can make, prints them out and asks the user to select one.
	 * 
	 * @param g - the current game state
	 * @return - the new game state selected by the user
	 */
	public static GameState humanP2(GameState g)
	{
		ArrayList<GameState> movesP2CouldMake = g.p2TurnGenerateSuccessors();
		
		System.out.println("Here's the moves P2 could make:\n");
		for(int i = 0; i < movesP2CouldMake.size(); i++)
		{
			GameState s = movesP2CouldMake.get(i);
			System.out.println(i+":\n"+s);
		}
		
		System.out.print("P2's move? ");
		int moveIndex = keyboard.nextInt();
		GameState newGameState = movesP2CouldMake.get(moveIndex);
		return newGameState;
	}
	
	/**
	 * Given a game state, this method generates all possible boards resulting from 
	 * legal moves Player 1 can make and picks one at random.
	 * 
	 * @param g - the current game state
	 * @return - the new game state selected at random
	 */
	public static GameState randomAIP1(GameState g) 
	{
		ArrayList<GameState> movesP1CouldMake = g.p1TurnGenerateSuccessors();
		int moveIndex = (int)(Math.random()*movesP1CouldMake.size());
		GameState newGameState = movesP1CouldMake.get(moveIndex);
		return newGameState;
	}

	/**
	 * Given a game state, this method generates all possible boards resulting from 
	 * legal moves Player 2 can make and picks one at random.
	 * 
	 * @param g - the current game state
	 * @return - the new game state selected at random
	 */
	public static GameState randomAIP2(GameState g) 
	{
		ArrayList<GameState> movesP2CouldMake = g.p2TurnGenerateSuccessors();
		int moveIndex = (int)(Math.random()*movesP2CouldMake.size());
		GameState newGameState = movesP2CouldMake.get(moveIndex);
		return newGameState;
	}
	

	/**
	 * Uses the minimax algorithm to compute the best move for P1.
	 * 
	 * This method is the same as maxValue except it returns the GameState associated with the best move rather than the utility.
	 * 
	 * @param g - the current game state
	 * @return - the new game state selected by the minimax algorithm
	 */
	public static GameState minimaxAIP1(GameState g) 
	{
		double bestUtil = Double.NEGATIVE_INFINITY; //utility of the best child node in the minimax tree
		GameState bestState = null; //the gamestate associated with the best utility
		
		ArrayList<GameState> successors = g.p1TurnGenerateSuccessors();
		
		//P1 is max, so we're looking for the highest valued successor
		for( GameState child : successors)
		{
			//uncomment this once you have minValue correctly implemented
			/*
			double childVal = minValue(child);
			if(childVal > bestUtil)
			{
				bestUtil = childVal;
				bestState = child;
			}
			*/
		}
		
		return bestState;
	}
	
	/**
	 * Computes the minimax (utility) value of the given state
	 * 
	 * @param s - the state to find the minimax value
	 * @return the utility of s in the minimax tree
	 */
	public static double maxValue(GameState s)
	{	
		//If this is an end-game state, just return the utility based on who won
		if (s.terminalTest()) 
			return s.utility();
		
		double rVal = Double.NEGATIVE_INFINITY; //utility of the best child node in the minimax tree
		
		ArrayList<GameState> successors = s.p1TurnGenerateSuccessors();
		
		//we're at a max node, so look for the highest values successor
		for( GameState child : successors)
		{
			//uncomment this once you have minValue correctly implemented
			/*
			double childVal = minValue(child);
			if(childVal > rVal)
			{
				rVal = childVal;
			}
			*/
		}
		
		return rVal;
	}
}
