/* Name: Ali Jandal
 * Date: 4-5-13
 * Description: This program recommends books to the user after showing what the most popular and least popular one is.
 * Points: I am going for the full 30 out of 30 points.
 */


import java.util.Scanner;
import java.io.*;

public class AssignmentSeven {

	public static void main(String[] args) throws IOException{
		//declare variables
		int[][] ratingsMatrix = new int[86][55];
		int bookRating = 0;
		int highRating = Integer.MIN_VALUE;
		int highBook = 0;
		int lowBook = 0;
		int lowRating = Integer.MAX_VALUE;
		String[] bookNames = new String[55];
		int[] myRatingsM = new int[55];
		int comScore = 0;
		int bestMatch = Integer.MIN_VALUE;
		int bestMatchUser = 0;
		String[] UserNames = new String[86];

		//initalizing input file.
		System.out.println("Reading File");
		File inFile = new File("bookRatings.txt");
		Scanner inputFile = new Scanner(inFile);

		// Enter data into array
		for (int p = 0; p < 86; p++){
			for (int b = 0; b <55; b++){
				ratingsMatrix[p][b] = inputFile.nextInt();
			}
		}

		// Reading in book data
		inFile = new File("books.txt");
		inputFile = new Scanner(inFile);
		for (int b = 0; b < 55; b++){
			bookNames[b] = inputFile.nextLine();
		}


		System.out.println("ratingsMatrix data stored");
		// Add up all data for each book
		for (int b = 0; b < 55; b++){
			bookRating = 0;
			for (int p = 0; p <86; p++){
				bookRating = bookRating + ratingsMatrix[p][b];
			}
			//Find and print highest and lowest ratings
			if (bookRating > highRating){
				highRating = bookRating;
				highBook = b;
			}
			if (bookRating < lowRating){
				lowRating = bookRating;
				lowBook = b;
			}
		}
		System.out.println("Highest rated book is number " +highBook + " which is "  + bookNames[highBook]);
		System.out.println("Lowest rated book is number " + lowBook + " which is "  + bookNames[lowBook]);

		// Entering my personal ratings
		inFile = new File("ZekeBooks.txt");
		inputFile = new Scanner(inFile);
		for (int b = 0; b <55 ; b++){
			myRatingsM[b] = inputFile.nextInt();
		}

		//Getting String of users
		inFile = new File("names.txt");
		inputFile = new Scanner(inFile);
		for (int p = 0; p < 86; p++){
			UserNames[p] = inputFile.nextLine(); 
		}

		for (int p = 0; p <86; p++){
			for(int b = 0; b < 55; b++){
				comScore = comScore + (myRatingsM[b] * ratingsMatrix[p][b]);	
			}
			if (comScore > bestMatch ){
				bestMatch = comScore;
				bestMatchUser = p;
			}
		}
		System.out.println("Best match is: " + UserNames[bestMatchUser] + " with a score of " + comScore);

		//Recommend books
		System.out.println("You may like some of these books:");
		for (int b = 0; b < 55; b++){
			if ((myRatingsM[b] == 0) && (ratingsMatrix[66][b] >= 1)){
				System.out.println(bookNames[b]);
			}
		}



	}//end main  method 

}// end class
