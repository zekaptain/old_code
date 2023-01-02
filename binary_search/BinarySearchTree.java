
/**
 * BinarySearchTree
 * 
 * Author: M. Q. Rieck
 * Date: June 2013
 * 
 */

// Code to demonstrate binary search trees


// An object from this class is an entire binary search tree 
// (with generic key and other data)
class BinarySearchTree<Key extends Comparable<Key>, Data>
{ 
    // EXECUTION STARTS HERE 
    
    public static void main(String[] args) {
        testBinarySearchTree();
    }

    // must keep track of the root node
    private BSTNode<Key,Data> root; 
    // will also keep track of tree size and depth
    private int size, depth;

    public BinarySearchTree() 
    { 
        root = null;
        size = depth = 0;
    }

    public int getSize() { return size; }
    public int getDepth() { return depth; }
    
    // If tree contains key k, then get the node for this key
    public BSTNode<Key,Data> findNode(Key k)
    {
        if (root == null) return null;
        //root is variable that belongs to binarysearchtree object
        //an instance variable in java, member data in c++
        //also known generally as an attribute
        return root.searchThisBSTNodeAndBelow(k);
    }

    // If tree contains key k, then return associated data
    //call find, pass in Key parameter data type.
    //Key is a template parameter (known as Key in java)
    //returns data of type Data
    //find is acting on an object from class BinarySearchTree
    public Data find(Key k)
    {
        //this method returns a node by reference (in java)
        //this is different in c++ but only significant difference
        BSTNode<Key,Data> node = findNode(k);
        if (node == null) return null;
        if (node.getKey().compareTo(k) == 0)
            return node.getData();
            else return null;
    }
    
    // Insert new BSTNode with specified key and data, 
    // unless a node with this key exists already
    public boolean insert(Key k, Data d)
    {
        BSTNode<Key,Data> p, q;        
        if (root != null) {
            //find gets data, and if it doesn't find it, returns null
            //thus, use findNode, because we want to find the node that was the
            //last one examined in the search, which will become parent of new node
            p = findNode(k);
            if (p != null && p.getKey().compareTo(k) == 0) return false;
            q = new BSTNode<Key,Data>(k, d, 1 + p.getLevel());
            if (p.getKey().compareTo(k) < 0)
                p.setRight(q); 
            else
                p.setLeft(q);
            if (q.getLevel() > depth) depth = q.getLevel();
            size++;
            return true; 
        } else { 
            root = new BSTNode<Key,Data>(k, d, 1);
            size = depth = 1; 
            return true; 
        }
    }

    // Display the keys in the tree in sorted order
    public void displayKeysSorted()
    {
        if (root != null) root.displayThisBSTNodeAndBelowSorted();
    }
    
    // Display the keys in the tree in a tree form
    // (one line per tree level)
    public void displayKeysAsTree()
    {
        if (root != null) 
        for (int i=0; i<depth; i++) {
           root.displayLevelBelow(i);
           System.out.println();
        }
    }

    // Compute the tree size the hard way (to show technique)
    public int treeSize() 
    {
        if (root != null) return root.countBSTNodesInSubtree();
        else return 0; 
    }

    // Test code for binary search trees
    public static void testBinarySearchTree() 
    {
        BinarySearchTree<String,String> scrabbleWords = new BinarySearchTree<String,String>();
        
        
        /*
        BinarySearchTree<String, String> noises = 
            new BinarySearchTree<String, String>();
        // Insert data in an arbitrary order
        noises.insert("moo", "cow"); 
        noises.insert("meow", "cat"); 
        noises.insert("quack", "duck"); 
        noises.insert("oink", "pig"); 
        noises.insert("honk", "goose"); 
        noises.insert("neigh", "horse");
        noises.insert("chirp", "bird");
        noises.insert("baa", "sheep");
        noises.insert("croak", "toad");
        noises.insert("squeak", "mouse");
        noises.insert("zzz", "human");
        noises.insert("whoop", "hyena");
        noises.insert("yelp", "human");
        if (noises.insert("bark", "dog")) 
            System.out.println("YES");
        else 
            System.out.println("NO"); 
        if (noises.insert("bark", "dog")) 
            System.out.println("YES"); 
        else 
            System.out.println("NO"); 
        System.out.println("Node count = " + noises.treeSize());
        System.out.println("Size = " + noises.getSize());
        System.out.println("Depth = " + noises.getDepth());
        System.out.println();

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

           System.out.println();
        System.out.println("Tree levels (keys only):");
        noises.displayKeysAsTree(); 
        System.out.println();
        System.out.print("Sorted noises (keys): "); 
        noises.displayKeysSorted(); 
        System.out.println();
         
        */
    }
}


// Objects from this class are BSTNodes in a binary search tree 
// (with generic key and other data)
class BSTNode<Key extends Comparable<Key>, Data>
{
    private Key key;
    private Data data;
    private int level;
    private BSTNode<Key,Data> left;
    private BSTNode<Key,Data> right;

    public BSTNode(Key k, Data d, int l)
    {
        key = k; 
        data = d;
        level = l;
        left = right = null;
    }

    public Key getKey() { return key; }
    public Data getData() { return data; }
    public int getLevel() { return level; }
    public BSTNode<Key,Data> getLeft() { return left; }
    public BSTNode<Key,Data> getRight() { return right; }
    public void setData(Data d) { data = d; } 
    public void setLevel(int l) { level = l; }
    public void setLeft(BSTNode<Key,Data> n) { left = n; } 
    public void setRight(BSTNode<Key,Data> n) { right = n; }  

    // Find a key in this BSTNode or one of its descendants, and
    // return (the address of) the BSTNode containing it, OR else
    // return the address of the last BSTNode examined (if not found)
    public BSTNode<Key,Data> searchThisBSTNodeAndBelow(Key k)
    {
        //"this" is a key word that means this instance of this object in java
        //in c++, "this" is the pointer that points to that node its acting on
        //java hides the fact that it uses pointers -- programmer can't access them
        if (k.compare(key) == 0) return this;
        if (k.compareTo(key) < 0) {
            //no left child
            if (left == null) return this;
            //if there is a left child
            //object-oriented recursive call on left child of current node
            else return left.searchThisBSTNodeAndBelow(k);
        } else if (k.compareTo(key) > 0) {
            //same as above but with right child
            if (right == null) return this;
            else return right.searchThisBSTNodeAndBelow(k);
        } else return this;
    }

    // Display keys of this BSTNode and its descendants in order 
    public void displayThisBSTNodeAndBelowSorted() 
    { 
        if (left != null) left.displayThisBSTNodeAndBelowSorted(); 
        System.out.println(key + " ");
        if (right != null) right.displayThisBSTNodeAndBelowSorted(); 
    }   

    // Display 2^j hyphens
    public void displayHyphens(int j) 
    {
        if (j == 0) System.out.print("- ");
        else {
            displayHyphens(j-1);
            displayHyphens(j-1);
        }
    }

    // Display data j levels below this with filler hyphens 
    // for missing BSTNodes 
    public void displayLevelBelow(int j)
    {
        if (j == 0) System.out.print(key + " "); 
        else { 
          if (left != null) left.displayLevelBelow(j-1);
            else displayHyphens(j-1);
          if (right != null) right.displayLevelBelow(j-1); 
            else displayHyphens(j-1);
        }
    }    

    // Determine number of BSTNodes below this BSTNode, plus this BSTNode
    public int countBSTNodesInSubtree()
    {
        if (left != null && right != null)          
            return 1 + left.countBSTNodesInSubtree() + right.countBSTNodesInSubtree();
        else if (left != null && right == null)         
            return 1 + left.countBSTNodesInSubtree();
        else if (left == null && right != null)         
            return 1 + right.countBSTNodesInSubtree();
        else return 1;
    }   
}
