// 셀프 넘버
#include <iostream>

using namespace std;

int main() {
	int ttt;
	int num[10000] = { 1, };

	for (int i = 0; i < 10000; i++) {
		if (i < 10) { // 1�� �ڸ�
			num[i + i % 10] = 1;
		}
		else if (i >= 10 && i < 100) { // 10�� �ڸ�
			num[i + (i / 10) + (i % 10)] = 1;
		}
		else if (i >= 100 && i < 1000) { // 100�� �ڸ�
			num[i + (i / 100) + ((i % 100) / 10) + (i % 10)] = 1;
		}
		else if (i >= 1000 && i < 10000) {  // 1000�� �ڸ�
			ttt = i + (i / 1000) + ((i % 1000) / 100) + ((i % 100) / 10) + (i % 10);
			if (ttt < 10000) {
				num[ttt] = 1;
			}
		}
	}
	for (int j = 0; j < 10000; j++) {
		if (!num[j]) {
			cout << j << endl;
		}
	}
}