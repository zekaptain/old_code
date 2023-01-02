/**
 * SlidingPuzzleState Class
 * 
 * This is a class for representing an n by m sliding puzzle with an
 * "empty" space that can be moved around the board, with the goal
 * of reaching some canonical arrangement.
 * 
 * This will be used to explore search strategies in CS 143
 * 
 * @author Eric D. Manley
 * 
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class SlidingPuzzleState 
{
	private int[][] board; //each tile has a number 1 to n, the blank is represented as 0
	private int rows; //number of rows on the board
	private int cols; //number of columns on the board
	private int blankRow; //the index of the row containing the blank
	private int blankCol; //the index of the column containing the blank

	/**
	 * Constructor for creating a board in the solved position with given dimensions
	 * 
	 * @param w - the board width, number of columns
	 * @param h - the board height, number of rows
	 */
	public SlidingPuzzleState(int w, int h)
	{
		if(w*h < 2 || w < 0 || h < 0)
		{
			System.out.println("Must have at least 2 squares");
			System.exit(0);
		}
		rows = h;
		cols = w;
		board = new int[rows][cols];
		initialize();
	}

	/**
	 * Constructor for reading in a board from a file.
	 * 
	 * @param filename - the file containing the board, the format is straightforward, see the examples
	 */
	public SlidingPuzzleState(String filename)
	{
		Scanner inFile;
		try 
		{
			inFile = new Scanner(new File(filename));

			rows = inFile.nextInt();
			cols = inFile.nextInt();
			if(cols*rows < 2 || cols < 0 || rows < 0)
			{
				System.out.println("Must have at least 2 squares");
				System.exit(0);
			}
			board = new int[rows][cols];
			for(int r = 0; r < rows; r++)
			{
				for(int c = 0; c < cols; c++)
				{
					board[r][c] = inFile.nextInt();
					if(board[r][c] == 0)
					{
						blankRow = r;
						blankCol = c;
					}
				}
			}
		} catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		}
	}

	/**
	 * Copy constructor for creating a deep copy of another board.
	 * 
	 * @param other - the state to make a copy of
	 */
	public SlidingPuzzleState(SlidingPuzzleState other)
	{
		rows = other.rows;
		cols = other.cols;
		blankRow = other.blankRow;
		blankCol = other.blankCol;
		board = new int[rows][cols];
		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				board[r][c] = other.board[r][c];
			}
		}
	}

	/**
	 * Puts numbers in the 2-D board array in order. This puts the tiles in a solved arrangement.
	 */
	public void initialize()
	{
		int i = 1;
		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				board[r][c] = i;
				i++;
			}
		}
		board[rows-1][cols-1] = 0; //space
		blankRow = rows-1;
		blankCol = cols-1;
	}

	/**
	 * For determining if this state is a goal state.
	 * 
	 * @return true if the tiles are in the solved arrangement, false otherwise
	 */
	public boolean isGoal()
	{
		int numberToExpect = 0;
		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				if(r == rows - 1 && c == cols - 1 )
				{
					numberToExpect = 0;
				}
				else
				{
					numberToExpect++;
				}
				
				if(board[r][c] != numberToExpect)
				{
					return false;
				}
			}
		}
		
		return true;
	}
	
	/**
	 * Use for making moves. The blank tile is swapped with another tile.
	 * This method will allow you to swap the blank with any other tile, but
	 * to respect the rules of the n-puzzle, you should only swap with an
	 * adjacent tile, so this is a private method for internal use only.
	 * 
	 * @param r - index of the row of the tile to be swapped with the blank
	 * @param c - index of the column of the tile to be swapped with the blank
	 */
 	private void swapWithBlank(int r, int c)
	{
		board[blankRow][blankCol] = board[r][c];
		board[r][c] = 0;
		blankRow = r;
		blankCol = c;
	}

 	/**
 	 * Makes random moves on the board.
 	 * 
 	 * This version simply calls the other shuffle with a default number of moves to make. 
 	 */
	public void shuffle()
	{
		shuffle(1000*rows*cols);
	}

	/**
	 * Makes random moves on the board.
	 * 
	 * @param moves - number of random moves to make
	 */
	public void shuffle(int moves)
	{
		double moveDir;
		int moveRow;
		int moveCol;
		boolean madeMove;
		for(int i = 0; i < moves; i++)
		{
			madeMove = false;
			//we might try to move in an illegal direction, so keep going until you get a legal one
			while(!madeMove) 
			{
				moveDir = Math.random()*4;
				if(moveDir < 1) //up
				{
					moveRow = blankRow - 1;
					moveCol = blankCol;
				}
				else if(moveDir < 2) //right
				{
					moveRow = blankRow;
					moveCol = blankCol + 1;
				}
				else if(moveDir < 3) //down
				{
					moveRow = blankRow + 1;
					moveCol = blankCol;
				}
				else //left
				{
					moveRow = blankRow;
					moveCol = blankCol - 1;
				}
				if(moveRow >= 0 && moveRow < rows && moveCol >= 0 && moveCol < cols)
				{
					//found a legal move
					swapWithBlank(moveRow,moveCol);
					madeMove = true;
				}
			}
		}
	}

	/**
	 * generates the successor states for use in search
	 * 
	 * @return a list of all the states that can be obtained from this state in 1 move
	 */
	public ArrayList<SlidingPuzzleState> generateSuccessors()
	{
		ArrayList<SlidingPuzzleState> childrenStates = new ArrayList<SlidingPuzzleState>();
		
		if(blankRow - 1 >= 0) //we can do an up move
		{
			SlidingPuzzleState up = new SlidingPuzzleState(this);
			up.swapWithBlank(blankRow-1, blankCol);
			childrenStates.add(up);
		}
		
		if(blankRow + 1 < rows) //we can do an down move
		{
			SlidingPuzzleState down = new SlidingPuzzleState(this);
			down.swapWithBlank(blankRow+1, blankCol);
			childrenStates.add(down);
		}
		
		if(blankCol - 1 >= 0) //we can do a left move
		{
			SlidingPuzzleState left = new SlidingPuzzleState(this);
			left.swapWithBlank(blankRow, blankCol-1);
			childrenStates.add(left);
		}
		
		if(blankCol + 1 < cols) //we can do a right move
		{
			SlidingPuzzleState right = new SlidingPuzzleState(this);
			right.swapWithBlank(blankRow, blankCol+1);
			childrenStates.add(right);
		}
		
		return childrenStates;
	}

	/**
	 * Overrides the toString() method in Object. This allows you to throw a SlidingPuzzleState
	 * object into a print statement and have it print a nice representation of the puzzle.
	 * 
	 * This code is kind of ugly and complicated, but it works for puzzles with fewer than 1000 tiles.
	 * Don't bother with trying to edit this code unless you really know what you're doing.
	 * 
	 * @return a string with a nice display of the puzzle
	 */
	public String toString()
	{
		String pad1 = ""; //for padding 1-digit numbers
		String pad2 = ""; //for padding 2-digit numbers
		String displayString = ""; //the string we'll build up
		int size = rows*cols; //number of tiles
		int digits = 0; //max number of digits in a number tile

		if(size >= 1000)
		{
			return "Puzzle is too big to display";
		}
		else if(size >= 100)
		{
			pad1 = "  ";
			pad2 = " ";
			digits = 3;
		}
		else if(size >= 10)
		{
			pad1 = " ";
			pad2 = "";
			digits = 2;
		}
		else
		{
			pad1 = "";
			digits = 1;
		}

		//top bar
		for(int c = 0; c < cols; c++)
		{
			for(int i = 0; i < digits+3; i++)
			{
				displayString += "-";
			}
		}
		displayString += "-\n";


		for(int r = 0; r < rows; r++)
		{
			displayString += "|";
			for(int c = 0; c < cols; c++)
			{
				if(board[r][c] == 0)
				{
					displayString += " "+pad1+"  |";
				}
				else if(board[r][c] < 10)
				{
					displayString += " "+pad1+board[r][c]+" |";
				}
				else if(board[r][c] < 100)
				{
					displayString += " "+pad2+board[r][c]+" |";
				}
				else
				{
					displayString += " "+board[r][c]+" |";
				}
			}
			//a horizontal bar
			displayString += "\n";
			for(int c = 0; c < cols; c++)
			{
				for(int i = 0; i < digits+3; i++)
				{
					displayString += "-";
				}
			}
			displayString += "-\n";
		}


		return displayString;
	}

	/**
	 * Use this to determine if two states are the same. Since they each
	 * occupy different places in memory, we have to check tile by tile
	 * that the numbers all match
	 * 
	 * @param other - the other state to compare with
	 * @return true if the two states represent the same puzzle, false otherwise
	 */
	public boolean isSame(SlidingPuzzleState other)
	{
		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				if(board[r][c] != other.board[r][c])
				{
					return false; //allows us to exit quickly in most comparisons
				}
			}
		}
		
		return true;
	}
}
