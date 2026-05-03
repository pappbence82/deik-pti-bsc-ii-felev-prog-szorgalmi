#include <iostream>

struct Pair {
	int a;
	int b;
};

void BubbleSort(Pair* data, int length) {
	for (int i = 0; i < length; ++i) {
		for (int j = 0; j < length - 1; ++j) {
			if (data[j].a > data[j + 1].a) {
				Pair temp = data[j];
				data[j] = data[j + 1];
				data[j + 1] = temp;
			}
		}
	}
}

void PrintSeparatorDouble() {
	std::cout << "===" << std::endl;
}

void PrintSeparatorSingle() {
	std::cout << "---" << std::endl;
}

void PrintOutputLabel() {
	std::cout << "Output:" << std::endl;
}

void ProcessAndPrint(const Pair* data, int length) {
	for (int i = 0; i < length; ++i) {
		int a = data[i].a;
		int b = data[i].b;
		int result = 0;

		if (a % 2 == 0) {
			result = (b % 2 == 0) ? a * b : a + b;
		} else {
			result = (b % 2 == 0) ? a - b : a;
		}

		std::cout << result << std::endl;
	}
}

void Run(Pair* data, int length) {
	BubbleSort(data, length);
	PrintSeparatorDouble();
	PrintOutputLabel();
	PrintSeparatorSingle();
	ProcessAndPrint(data, length);
}

int main() {
	Pair data[5] = {
		{5, 1},
		{2, 4},
		{3, 7},
		{1, 6},
		{4, 5},
	};

	Run(data, 5);
	return 0;
}
