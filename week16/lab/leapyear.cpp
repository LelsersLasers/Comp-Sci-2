#include <iostream>
#include <string>

using std::string;


int main() {

	std::cout << "Enter a year: ";

	int year;
	std::cin >> year;

	// if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
	// 	std::cout << year << " is a leap year." << std::endl;
	// } else {
	// 	std::cout << year << " is not a leap year." << std::endl;
	// }

	if (year % 400 == 0) {
		std::cout << year << " is a leap year." << std::endl;
	} else if (year % 100 == 0) {
		std::cout << year << " is not a leap year." << std::endl;
	} else if (year % 4 == 0) {
		std::cout << year << " is a leap year." << std::endl;
	} else {
		std::cout << year << " is not a leap year." << std::endl;
	}


	return 0;
}