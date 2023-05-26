#include<string>
/*
    Name: Millan and Jerry
    Date: Spring 2023
    Purpose: Implement a pointer-based binary search tree whose content is
        of data type long int. Implement height-balancing using node 
        rotations.
*/

/* @brief Class to represent one node of a binary search tree. */
class Node {
    friend class Tree;
    public:
        // Pointers to left and right child nodes.
        Node* left;
        Node* right;

        Node* parent;
        // The actual content of this node.
        long content;
        // height and height balance of each node
        long height;
        long heightBalance;

        // Default constructor, assigns 0 as its content.
        Node();
        // Deconstructor, recursively deconstructs all children.
        void deconstructorRecursive();
        // Constructor with content.
        Node(long content);
        // Constructor with content and parent.
        Node(long content, Node* parent);

        // returns true if the tree contains the content (recursive)
        bool contains(long content);

        // returns true if the node has no children
        bool isLeaf();

        // delete a node with the given content (silently ignore if not found)
        void delete_node(long content);

        // recusively subtracts 1 from the height of the node and its children
        void shiftUp();

        // dump in order
        void dump();
        /* prints the content of the node and its children in a tree-like format
            with the parent on the left and it's childern on the right */
        void prettyDump(int height);
    private:
        /* Methods to add a child node directly to this node.  Intended to 
            be called by Tree::add_node(). */
        void add_left(long content);
        void add_right(long content);
};

/* @brief Class to represent a binary search tree. */
class Tree {
    friend class Node;
    public:
        // Pointer to the first node of binary search tree.
        Node* head;
        // Default constructor.  Assigns head to be a null pointer.
        Tree();
        // Deconstructor, recursively deconstructs all children using Node::deconstructorRecursive()
        ~Tree();
        /* Add content in the appropriate location, where every Node to its
            left has content smaller than this content, everything to the 
            right has larger content.  Silently ignore duplicated content. */
        void add_node(long content);

        // returns true if the tree contains the content
        bool contains(long content);

        // delete a node with the given content (silently ignore if not found)
        void delete_node(long content);

        // dump in order
        void dump();
        /* prints the content of the node and its children in a tree-like format
            with the head on the left and childern on the right
            Does not need queue because it goes left to right */
        void prettyDump();
};