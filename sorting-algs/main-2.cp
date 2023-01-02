
// HashTable.cpp

// Code to demonstrate using a hash table to
// implement an associative array

// Author: M. Q. Rieck
// Date: September 2013

#include <iostream>
#include <string>

using namespace std;

void testHashTable();

// EXECUTION STARTS HERE

int main() {
    
    testHashTable();
    return 0;
}

// Hash a 9 digit character string into a small integer
int computeIndex(string fullName) {
    string name;
    long length;
    int index;
    name = fullName;
    char ch;
    index = 0;
    length = name.length();
    for (int i=0; i<length; i++){
        ch = name[i];
        index += (int)ch;
    }
    index = index % 1000;
    return index;
    /*
    int first  = 100*(id[0]-'0') + 10*(id[1]-'0') + (id[2]-'0');
    int second = 100*(id[3]-'0') + 10*(id[4]-'0') + (id[5]-'0');
    int third  = 100*(id[6]-'0') + 10*(id[7]-'0') + (id[8]-'0');
    return (first + second + third) % 1000;
     */
}

// See if IDs are okay and equal
bool compareIDs(string id1, string id2) {
    if (id1.length() != 9 || id2.length() != 9) return false;
    for (int i=0; i<9; i++)
        if (id1[i] != id2[i] || id1[i]<'0' || id1[i]>'9') return false;
    return true;
}

// An object from this class is a student record
class Student
{
private:
    
    string id;
    string lastName;
    string firstName;
    //string fullName;
    double gpa;
    
public:
    
    Student(string _id, string last, string first, double g) {
        id = _id;
        lastName = last;
        firstName = first;
        gpa = g;
        
    }
    
    string getID() { return id; }
    string getLastName() { return lastName; }
    string getFirstName() { return firstName; }
    
    string getFullName() { return firstName+lastName;}
/*
    string getFullName() {
        char str[80];
        strcat(str, firstName.c_str());
        strcat(str, lastName.c_str());
        string fullName(str);
        return fullName;
    }
 */
     
    double getGPA() { return gpa; }
    void displayAll() {
        cout << "ID = " << id << endl;
        cout << "Name = " << firstName << " " << lastName << endl;
        cout << "GPA = " << gpa << endl;
    }
};

// Objects in this class are nodes in the linked list
class StudentNode
{
private:
    
    Student *student;
    StudentNode *next, *prev;
    
public:
    
    StudentNode(Student *s) {
        student = s;
        next = prev = NULL;
    }
    
    Student* getStudent() { return student; }
    StudentNode* getNext() { return next; }
    StudentNode* getPrev() { return prev; }
    void setNext(StudentNode *n) { next = n; }
    void setPrev(StudentNode *n) { prev = n; }
};

// Previously developed linked list code, but tailored here
// to maintain a linked list of Student objects
class LinkedList
{
private:
    
    int size;
    StudentNode *first, *last;
    
public:
    
    LinkedList() {
        size = 0;
        first = last = NULL;
    }
    
    int getSize() { return size; }
    
    void insertStudent(Student* student) {
        if (size == 0) {
            first = last = new StudentNode(student);
            size = 1;
        } else {
            last->setNext(new StudentNode(student));
            last->getNext()->setPrev(last);
            last = last->getNext();
            size++;
        }
    }
    
    // Search the linked list for a particular student, and if
    // not found, return NULL pointer. But if found,
    // then return pointer to found Student object.
    Student* getStudent(string id) {
        int i;
        StudentNode* node = first;
        for (i=0; i<size; i++) {
            // If student found, break out of loop
            if (compareIDs(node->getStudent()->getID(), id)) break;
            // Otherwise, go on to the next node
            node = node->getNext();
        }
        if (i == size)
            return NULL;
        else
            return node->getStudent();
    }
    
    // Search the linked list for a particular student, and if
    // found, then displaying information about that student.
    void findAndDisplayStudent(string fullName) {
        int i;
        StudentNode* node = first;
        for (i=0; i<size; i++) {
            // If student found, break out of loop
            if (fullName == node->getStudent()->getFullName()) break;
            //if (compareIDs(node->getStudent()->getFullName(), fullName)) break;
            // Otherwise, go on to the next node
            node = node->getNext();
        }
        if (i == size)
            cout << "NOT FOUND" << endl;
        else
            node->getStudent()->displayAll();
    }
};

// An object from this class represents a whole hash table
class HashTable
{
private:
    
    // An array of pointers to linked lists
    LinkedList** theArray;
    
public:
    
    // Default constructor
    HashTable() {
        theArray = new LinkedList*[1000];
        for (int i=0; i<1000; i++)
            theArray[i] = new LinkedList();
    }
    
    void insertStudent(Student* student) {
//        string id = student->getID();
//        int index = computeIndex(id);

        string fullname = student->getFullName();
        int index = computeIndex(fullname);
        
        theArray[index]->insertStudent(student);
    }
    
    Student* getStudent(string id) {
        int index = computeIndex(id);
        return theArray[index]->getStudent(id);
    }
    
    void findAndDisplayStudent(string fullName) {
        int index = computeIndex(fullName);
        theArray[index]->findAndDisplayStudent(fullName);
    }
    
    void displayLinkedListSizes() {
        for (int i=0; i<1000; i++) {
            int size = theArray[i]->getSize();
            if (size > 0) cout << size << " ";
        }
        cout << endl;
    }
};


void testHashTable() {
    HashTable* theHashTable = new HashTable();
    int choice;
    string fullName, id, lastName, firstName;
    double gpa;
    Student* student;
    
    do {
        cout << "1. Add a new student" << endl;
        cout << "2. Look up a student" << endl;
        cout << "3. Display nonempty linked list sizes" << endl;
        cout << "4. Quit" << endl;
        cout << "Choice: " << endl;
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "9-digit ID: ";
                cin >> id;
                cout << "Last name: ";
                cin >> lastName;
                cout << "First name: ";
                cin >> firstName;
                cout << "GPA: ";
                cin >> gpa;
                student =
                new Student(id, lastName, firstName, gpa);
                theHashTable->insertStudent(student);
                break;
            case 2:
                cout << "Enter Full Name: ";
                cin >> fullName;
                theHashTable->findAndDisplayStudent(fullName);
                break;
            case 3:
                theHashTable->displayLinkedListSizes();
                break;
            case 4:
                cout << "Bye! Thanks for playing!" << endl;
        }
    } while (choice != 4);
}

