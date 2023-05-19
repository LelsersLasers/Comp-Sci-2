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
	int height;


	Node() {
		content = T();
		left = nullptr;
		right = nullptr;

		heightBalance = T();
		height = 0;
	}

	Node(T content) {
		this->content = content;
		left = nullptr;
		right = nullptr;

		heightBalance = T();
		height = 0;
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

	void updateHeights() {
		// updates the height of the node and its children
		if (left != nullptr) {
			left->updateHeights();
		}

		if (right != nullptr) {
			right->updateHeights();
		}

		if (isLeaf()) {
			height = 0;
		} else if (left == nullptr) {
			height = right->height + 1;
		} else if (right == nullptr) {
			height = left->height + 1;
		} else {
			height = std::max(left->height, right->height) + 1;
		}

		heightBalance = height;
		// heightBalance = (right == nullptr ? 0 : right->height) - (left == nullptr ? 0 : left->height);
	}
};

class BinaryTree {
// Ordered and balanced binary tree

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
			root->updateHeights();
		}
	}

	bool contains(T content) {
		// returns true if the tree contains the given content
		if (this->isEmpty()) {
			return false;
		} else {
			Node* current = root;
			while (true) {
				if (content == current->content) {
					return true;
				} else if (content < current->content) {
					if (current->left == nullptr) {
						return false;
					} else {
						current = current->left;
					}
				} else {
					if (current->right == nullptr) {
						return false;
					} else {
						current = current->right;
					}
				}
			}
		}
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
		// prints the content of the tree in a tree-like format (where root is on the left)

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

		// while (true) {
		// 	int number = randomNumber();
		// 	if (tree.contains(number)) {
		// 		std::cout << "Found " << number << std::endl;
		// 		break;
		// 	} else {
		// 		tree.insert(number);
		// 	}
		// }

		for (int i = 0; i < 4; i++) {
			tree.insert(randomNumber());
		}

		tree.dump();

		tree.prettyDump();
	}
}