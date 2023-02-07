#include <iostream>
#include <string>

using std::string;


int main() {

	std::cout << "Enter string: ";

	string text;
	std::getline(std::cin, text);

	string leetedString = "";

	for (char& c : text) {
		switch (c) {
			case 'e':
			case 'E':
				leetedString += "3";
				break;
			case 'l':
			case 'L':
				leetedString += "1";
				break;
			case 's':
			case 'S':
				leetedString += "5";
				break;
			default:
				leetedString += c;
		}
	}
	std::cout << "Leet version: " << leetedString << std::endl;


	return 0;
}