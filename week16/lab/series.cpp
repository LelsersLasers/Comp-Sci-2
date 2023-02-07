#include <iostream>
#include <cmath>


int main() {

	std::cout << "denominator ratio (k): ";
	float k;
	std::cin >> k;

	std::cout << "number of terms (n): ";
	int n;
	std::cin >> n;

	float sum = 0;
	for (int i = 1; i < n; i++) {
		sum += 1 / powf(k, i);
	}

	std::cout << "sum: " << sum << std::endl;


	return 0;
}