#include <iostream>

// assert(condition) - if condition is false, the program will stop
#include <cassert>

typedef int T;

class Node {
// Node in a binary tree

public:
	T content;
	Node* left;
	Node* right;

	Node() {
		content = T();
		left = nullptr;
		right = nullptr;
	}

	Node(T content) {
		this->content = content;
		left = nullptr;
		right = nullptr;
	}

	void dump() {
		// prints the content of the node and its children
		std::cout << content << " ";
		if (left != nullptr) {
			left->dump();
		}
		if (right != nullptr) {
			right->dump();
		}
	}

};

class BinaryTree {

private:

	Node* root;
	long height;


public:

	BinaryTree() {
		root = nullptr;
		height = 0;
	}

	bool isEmpty() { return root == nullptr; }

	void insert(T content) {
		// inserts a new node in the tree
		Node* node = new Node();
		node->content = content;
		if (this->isEmpty()) {
			root = node;
		} else {
			Node* current = root;
			// while (true) {
			// 	if (content < current->content) {
			// 		if (current->left == nullptr) {
			// 			current->left = node;
			// 			break;
			// 		} else {
			// 			current = current->left;
			// 		}
			// 	} else {
			// 		if (current->right == nullptr) {
			// 			current->right = node;
			// 			break;
			// 		} else {
			// 			current = current->right;
			// 		}
			// 	}
			// }
		}
	}

	T peek() {
		// returns the content of the root
		// O(1) operation

		assert(!this->isEmpty());
		return root->content;
	}

	void dump() {
		// prints the content of the tree from top to bottom
		// O(n) operation

		if (this->isEmpty()) {
			std::cout << "Empty tree" << std::endl;
		} else {
			std::cout << "Tree: ";
			root->dump();
		}
	}
};