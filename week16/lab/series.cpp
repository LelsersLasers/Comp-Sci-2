#include <iostream>
#include <cmath>


int main() {

	std::cout << "denominator ratio (k): ";
	double k;
	std::cin >> k;

	std::cout << "number of terms (n): ";
	int n;
	std::cin >> n;

	double sum = 0;
	for (int i = 0; i < n; i++) {
		sum += 1 / pow(k, i);
	}

	std::cout << "sum: " << sum << std::endl;


	return 0;
}