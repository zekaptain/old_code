
/**
 * BinarySearchArray
 * 
 * Author: M. Q. Rieck
 * Date: June 2013
 * 
 */

// Code to demonstrate binary search in sorted array

@SuppressWarnings({"unchecked"})

// An object from this class should contain a sorted 
// array (with generic data)
class BinarySearchArray<Key extends Comparable<Key>, Data>
{
    // EXECUTION STARTS HERE 
    
    public static void main(String[] args) {
        testBinarySearch();
    }

    private static final int MAX_SIZE = 1000;
    // Actually, two arrays will be used, one to hold
    // the key attribute, used for ordering, and the other 
    // to hold other associated data
    private Key key[]; 
    private Data data[]; 
    private int size;

    public BinarySearchArray() 
    { 
        key = (Key[]) new Comparable[MAX_SIZE];
        data = (Data[]) new Object[MAX_SIZE];
        size = 0;
    }

    public int getSize() { return size; }

    // Insert new key and data into the arrays, BUT the keys
    // must be added in order, so as to build a sorted array
    public void insert(Key k, Data d)
    {
        key[size] = k;
        data[size++] = d;
    }

    public Data find(Key k) 
    {
        int index = findIndex(k, 0, size-1);
        if (index < 0) return null;
          else return data[index];
    }

    private int findIndex(Key k, int start, int end) 
    {
        if (start > end) return -1;  // not found
        int middle = (start + end) / 2; 
        if (k == key[middle]) return middle;
        else if (k.compareTo(key[middle]) < 0) 
            return findIndex(k, start, middle-1);
        else  // k > key[middle]
            return findIndex(k, middle+1, end);
    }

    // Test the BinarySearchArray class
    public static void testBinarySearch() 
    {
        BinarySearchArray<String, String> noises = 
          new BinarySearchArray<String, String>();
        noises.insert("baa", "sheep");
        noises.insert("bark", "dog"); 
        noises.insert("chirp", "bird");
        noises.insert("croak", "toad");
        noises.insert("honk", "goose"); 
        noises.insert("moo", "cow"); 
        noises.insert("meow", "cat"); 
        noises.insert("neigh", "horse");
        noises.insert("oink", "pig"); 
        noises.insert("quack", "duck"); 
        noises.insert("squeak", "mouse");
        noises.insert("whoop", "hyena");
        noises.insert("yelp", "human");
        noises.insert("zzz", "human");
        String who; 
        who = noises.find("oink");
        if (who == null) 
           System.out.println("Noise not found.");
        else
           System.out.println("The " + who + " says \"oink.\"");        
        who = noises.find("meow");
        if (who == null) 
           System.out.println("Noise not found.");
        else
           System.out.println("The " + who + " says \"meow.\"");        
        who = noises.find("baa");
        if (who == null) 
           System.out.println("Noise not found.");
        else
           System.out.println("The " + who + " says \"baa.\"");        
        who = noises.find("grrr");
        if (who == null) 
           System.out.println("Noise not found.");
        else
           System.out.println("The " + who + " says \"grrr.\"");        
    }
}
