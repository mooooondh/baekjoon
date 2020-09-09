#include<iostream>
using namespace std;

int main() {
	float snack[6];
	float s = 0;
	float n = 0;
	float u = 0;
	char max;

	for (int i = 0; i <= 5; i++) {
		cin >> snack[i];
		if (i == 1) {
			if (snack[0] * 10 >= 5000) {
				snack[0] = (snack[0] * 10) - 500;
			}
			else {
				snack[0] *= 10;
			}
			s = (snack[1] * 10) / snack[0];
		}
		else if (i == 3) {
			if (snack[2] * 10 >= 5000) {
				snack[2] = (snack[2] * 10) - 500;
			}
			else {
				snack[2] *= 10;
			}
			n = (snack[3] * 10) / snack[2];
		}
		else if (i == 5) {
			if (snack[4] * 10 >= 5000) {
				snack[4] = (snack[4] * 10) - 500;
			}
			else {
				snack[4] *= 10;
			}
			u = (snack[5] * 10) / snack[4];
		}
	}

	if (s > n) {
		if (s > u) {
			max = 'S';
		}
		else {
			max = 'U';
		}
	}
	else {
		if (n > u) {
			max = 'N';
		}
		else {
			max = 'U';
		}
	}

	cout << max << endl;

	return 0;
}