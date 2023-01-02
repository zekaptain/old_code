/**
 * The Class Quadromino. Instances of this class represent a single quadromino in the
 * number-tile-sequence search problem discussed in class. Each has four numbers
 * referred to as a, b, c, and d.
 * 
 * @author Eric D. Manley
 */
public class Quadromino 
{
	/** the first of the four values on the quadromino tile */
	private double a;
	/** the second of the four values on the quadromino tile */
	private double b;
	/** the third of the four values on the quadromino tile */
	private double c;
	/** the fourth of the four values on the quadromino tile */
	private double d;
	
	/**
	 * Instantiates a new quadromino.
	 *
	 * @param ia the first value for this quadromino
	 * @param ib the second value for this quadromino
	 * @param ic the third value for this quadromino
	 * @param id the fourth value for this quadromino
	 */
	public Quadromino(double ia, double ib, double ic, double id)
	{
		a = ia;
		b = ib;
		c = ic;
		d = id;
	}
	
	/**
	 * getter method for a
	 * 
	 * @return the a value
	 */
	public double getA(){ return a; }
	
	/**
	 * getter method for b
	 * 
	 * @return the b value
	 */
	public double getB(){ return b; }
	
	/**
	 * getter method for c
	 * 
	 * @return the c value
	 */
	public double getC(){ return c; }
	
	/**
	 * getter method for d
	 * 
	 * @return the d value
	 */
	public double getD(){ return d; }
	
	
	/**
	 * Calculates the cost of this quadromino being placed after another given quadromino.
	 * The cost is the difference between this quadromino's a and the previous quadromino's
	 * c plus the difference between this quadromino's b and the previous quadromino's d.
	 * 
	 * @param another quadromino
	 * @return the cost of this quadromino if it is placed after the given quadromino
	 */
	public double penaltyIfPrevQuadromino(Quadromino other)
	{	
		return Math.abs(a-other.c)+Math.abs(b-other.d);
	}
	
	/**
	 * Calculates the cost of this quadromino being placed before another given quadromino.
	 * The cost is the difference between this quadromino's c and the next quadromino's
	 * a plus the difference between this quadromino's d and the next quadromino's b.
	 * 
	 * @param another quadromino
	 * @return the cost of this quadromino if it is placed after the given quadromino
	 */
	public double penaltyIfNextQuadromino(Quadromino other)
	{
		return Math.abs(other.a-c)+Math.abs(other.b-d);
	}
	
	/**
	 * For pretty printing the quadromino.
	 * 
	 * @return a string used for pretty printing the quadromino
	 */
	public String toString()
	{
		return "-------------------------\n|\t"+a+"\t"+b+"\t|\n|\t"+c+"\t"+d+"\t|\n-------------------------\n";
	}


}
