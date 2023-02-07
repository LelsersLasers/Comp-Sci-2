#include <iostream>
#include <string>

using std::string;


int main() {

	std::cout << "Enter text: ";

	string text;
	std::getline(std::cin, text);

	for (char& c : text) {
		std::cout << "-" << c;
	}
	std::cout << "-" << std::endl;


	return 0;
}