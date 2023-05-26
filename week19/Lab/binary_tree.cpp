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

void Node::deconstructorRecursive() {
	// I don't actually know if this works the way I think it does

	if (this->left != nullptr) {
		this->left->deconstructorRecursive();
	}
	if (this->right != nullptr) {
		this->right->deconstructorRecursive();
	}

	// do after children are deleted
	delete this;
}

void Node::add_left(long content) {
	if (this->left == nullptr) {
		this->left = new Node(content, this);
	} else if (content < this->left->content) {
		this->left->add_left(content);
	} else if (content > this->left->content) {
		this->left->add_right(content);
	}
	
}
void Node::add_right(long content) {
	if (this->right == nullptr) {
		this->right = new Node(content, this);
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

bool Node::isLeaf() {
	return (this->left == nullptr && this->right == nullptr);
}

void Node::delete_node(long content) {
	if (content == this->content) {
		if (this->isLeaf()) {
			if (this->parent->left == this) {
				this->parent->left = nullptr;
			}
			else if (this->parent->right == this) {
				this->parent->right = nullptr;
			}
			delete this;
		}
		else if (this->right == nullptr) { // left is not nullptr
			if (this->parent->left == this) {
				this->parent->left = this->left;
				this->parent->left->shiftUp();
			}
			else if (this->parent->right == this) {
				this->parent->right = this->left;
				this->parent->right->shiftUp();
			}
			delete this;
		}
		else if (this->left == nullptr) { // right is not nullptr
			if (this->parent->left == this) {
				this->parent->left = this->right;
				this->parent->left->shiftUp();
			}
			else if (this->parent->right == this) {
				this->parent->right = this->right;
				this->parent->right->shiftUp();
			}
			delete this;
		}
		else { // both left and right are not nullptr
			Node* current = this->right;
			while (current->left != nullptr) {
				current = current->left;
			}
			this->content = current->content;
			current->delete_node(current->content);
		}
	}
	else if (content < this->content) {
		if (this->left != nullptr) {
			this->left->delete_node(content);
		}
	}
	else if (content > this->content) {
		if (this->right != nullptr) {
			this->right->delete_node(content);
		}
	}
}

void Node::shiftUp() {
	this->height--;
	if (this->left != nullptr) {
		this->left->shiftUp();
	}
	if (this->right != nullptr) {
		this->right->shiftUp();
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
	
	// Uses spaces to line things up, so padding is needed
	// Assumes that the content will never be more than 3 digits
	std::string contentPadded = std::to_string(this->content);
	while (contentPadded.length() < 3) {
		contentPadded += " ";
	}
	std::cout << contentPadded << std::endl;

	if (this->left != nullptr) {
		this->left->prettyDump(height + 1);
	}
}
//----------------------------------------------------------------------------//


//----------------------------------------------------------------------------//
Tree::Tree() {
	this->head = nullptr;
}
Tree::~Tree() {
	if (this->head != nullptr) {
		this->head->deconstructorRecursive();
	}
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

void Tree::delete_node(long content) {
	if (this->head == nullptr) return;

	
	if (content == this->head->content) {
		if (this->head->isLeaf()) {
			delete this->head;
			this->head = nullptr;
		}
		else if (this->head->left == nullptr) { // right is not nullptr
			Node* temp = this->head;
			this->head = this->head->right;
			this->head->parent = nullptr;
			delete temp;

			this->head->shiftUp();
		}
		else if (this->head->right == nullptr) { // left is not nullptr
			Node* temp = this->head;
			this->head = this->head->left;
			this->head->parent = nullptr;
			delete temp;

			this->head->shiftUp();
		}
		else { // both are not nullptr
			Node* temp = this->head->right; // choose right to be moved up
			while (temp->left != nullptr) {
				temp = temp->left;
			}
			this->head->content = temp->content;
			temp->parent->left = nullptr;
			delete temp;

			this->head->shiftUp();
		}
	}
	else if (content < this->head->content) {
		this->head->left->delete_node(content);
	}
	else if (content > this->head->content) {
		this->head->right->delete_node(content);
	}
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