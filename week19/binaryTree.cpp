#include <iostream>

// assert(condition) - if condition is false, the program will stop
#include <cassert>

#include <ctime>



typedef int T;

class Node {
// Node in a binary tree

public:
	T content;

	Node* left;
	Node* right;

	int heightBalance;


	Node() {
		content = T();
		left = nullptr;
		right = nullptr;

		heightBalance = T();
	}

	Node(T content) {
		this->content = content;
		left = nullptr;
		right = nullptr;

		heightBalance = T();
	}

	void dump() {
		// prints the content of the node and its children
		if (left != nullptr) {
			left->dump();
		}
		
		std::cout << content << " ";

		if (right != nullptr) {
			right->dump();
		}
	}

	void prettyDump(int height) {
		// prints the content of the node and its children in a tree-like format

		if (right != nullptr) {
			right->prettyDump(height + 1);
		}

		for (int i = 0; i < height; i++) {
			std::cout << "|   ";
		}

		std::cout << content << "(" << heightBalance << ")" << std::endl;

		if (left != nullptr) {
			left->prettyDump(height + 1);
		}
	}

	bool isLeaf() {
		// returns true if the node is a leaf (has no children)
		return left == nullptr && right == nullptr;
	}

	int maxHeight(int height) {
		// returns the maximum height of the node and its children
		// height is the height of the node

		int leftHeight = 0;
		int rightHeight = 0;

		if (left != nullptr) {
			leftHeight = left->maxHeight(height + 1);
		}

		if (right != nullptr) {
			rightHeight = right->maxHeight(height + 1);
		}

		return std::max(height, std::max(leftHeight, rightHeight));
	}

	void updateHeightBalance(int height) {
		// updates the height balance of the node and its children
		// height is the height of the node

		int leftHeight = 0;
		int rightHeight = 0;

		if (left != nullptr) {
			left->updateHeightBalance(height + 1);
			leftHeight = left->maxHeight(0);
		}

		if (right != nullptr) {
			right->updateHeightBalance(height + 1);
			rightHeight = right->maxHeight(0);
		}


		heightBalance = rightHeight - leftHeight;
	}
};

class BinaryTree {

private:

	Node* root;


public:

	BinaryTree() {
		root = nullptr;
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
			while (true) {
				if (content < current->content) {
					if (current->left == nullptr) {
						current->left = node;
						break;
					} else {
						current = current->left;
					}
				} else {
					if (current->right == nullptr) {
						current->right = node;
						break;
					} else {
						current = current->right;
					}
				}
			}
			updateHeightBalances();
		}
	}

	void updateHeightBalances() {
		if (this->isEmpty()) {
			return;
		}

		root->updateHeightBalance(0);
	}

	T peek() {
		// returns the content of the root
		assert(!this->isEmpty());
		return root->content;
	}

	
	void dump() {
		// prints the content of the tree from top to bottom

		if (this->isEmpty()) {
			std::cout << "Empty tree" << std::endl;
		} else {
			std::cout << "Tree: ";
			root->dump();
			std::cout << std::endl;
		}
	}

	void prettyDump() {
		// prints the content of the tree in a tree-like format

		if (this->isEmpty()) {
			std::cout << "Empty tree" << std::endl;
		} else {
			std::cout << "Tree: " << std::endl;
			root->prettyDump(0);
		}
	}
};


int randomNumber() {
	// returns a random number between 10 and 99 (always 2 digits)

	return rand() % 90 + 10;
}

int main() {
	srand(time(nullptr));

	{
		BinaryTree tree;

		for (int i = 0; i < 3; i++) {
			tree.insert(randomNumber());
		}

		tree.dump();

		tree.prettyDump();
	}
}