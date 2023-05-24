#include<string>
#include<iostream>

#include "binary_tree.h"


//----------------------------------------------------------------------------//
Node::Node() {
	this->content = 0;
	
	this->left = nullptr;
	this->right = nullptr;
	this->parent = nullptr;

	this->height = 0;
	this->heightBalance = 0;
}
Node::Node(long content) {
	this->content = content;

	this->left = nullptr;
	this->right = nullptr;
	this->parent = nullptr;

	this->height = 0;
	this->heightBalance = 0;
}
Node::Node(long content, Node* parent) {
	this->content = content;

	this->left = nullptr;
	this->right = nullptr;
	this->parent = parent;

	this->height = parent->height + 1;
	this->heightBalance = 0;
}

void Node::add_left(long content) {
	if (this->left == nullptr) {
		this->left = new Node(content, this);


		Node* currentParent = this;
		while (currentParent != nullptr) {

			currentParent->heightBalance--;

			if (currentParent->heightBalance == 0) {
				break;
			}

			currentParent = currentParent->parent;
		}


	} else if (content < this->left->content) {
		this->left->add_left(content);
	} else if (content > this->left->content) {
		this->left->add_right(content);
	}
	
}
void Node::add_right(long content) {
	if (this->right == nullptr) {
		this->right = new Node(content, this);

		Node* currentParent = this;
		while (currentParent != nullptr) {

			currentParent->heightBalance++;

			if (currentParent->heightBalance == 0) {
				break;
			}

			currentParent = currentParent->parent;
		}

	} else if (content < this->right->content) {
		this->right->add_left(content);
	} else if (content > this->right->content) {
		this->right->add_right(content);
	}
}

bool Node::contains(long content) {
	if (content == this->content) {
		return true;
	}
	else if (content < this->content) {
		if (this->left == nullptr) {
			return false;
		}
		else {
			return this->left->contains(content);
		}
	}
	else {
		if (this->right == nullptr) {
			return false;
		}
		else {
			return this->right->contains(content);
		}
	}
}

void Node::dump() {
	if (this->left != nullptr) {
		this->left->dump();
	}
	
	std::cout << this->content << " ";

	if (this->right != nullptr) {
		this->right->dump();
	}
}
void Node::prettyDump(int height) {
	if (this->right != nullptr) {
		this->right->prettyDump(height + 1);
	}

	for (int i = 0; i < height; i++) {
		std::cout << "|  ";
	}
	// std::cout << this->content << std::endl;
	std::cout << this->content << "(" << this->height << ")" << std::endl;

	if (this->left != nullptr) {
		this->left->prettyDump(height + 1);
	}
}
//----------------------------------------------------------------------------//


//----------------------------------------------------------------------------//
Tree::Tree() {
	this->head = nullptr;
}

void Tree::add_node(long content) {
	if (this->head == nullptr) {
		this->head = new Node(content);
	}
	else {
		if (content < this->head->content) {
			this->head->add_left(content);
		} else if (content > this->head->content) {
			this->head->add_right(content);
		} 
	}
}

bool Tree::contains(long content) {
	if (this->head == nullptr) {
		return false;
	}
	else {
		if (content == this->head->content) {
			return true;
		}
		else if (content < this->head->content) {
			return this->head->left->contains(content);
		}
		else if (content > this->head->content) {
			return this->head->right->contains(content);
		}
	}
	return false;
}

void Tree::dump() {
	if (this->head != nullptr) {
		this->head->dump();
	}
	std::cout << std::endl;
}
void Tree::prettyDump() {
	if (this->head != nullptr) {
		this->head->prettyDump(0);
	}
	std::cout << std::endl;
}
//----------------------------------------------------------------------------//