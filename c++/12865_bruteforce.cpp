#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solution(int N, int K,vector<int> box1, vector<int>box2, int start) {
	vector<int> value;
	int weight = 0;
	int val = 0;
	int max;
		for (int z = start; z < N; z++) {
			weight = box1[z];
			if (weight <= K) {
				val = box2[z];
				value.push_back(val);
				weight = 0;
			}
		}
		for (int b = start; b < N; b++) {
			for (int d = b + 1; d < N; d++) {
				weight = box1[b] + box1[d];
				if (weight <= K) {
					val = box2[b]+box2[d];
					value.push_back(val);
					weight = 0;
					}
				}
			} // 3, 4 개 뽑는경우 반복 작성하면 됨
		max = *max_element(value.begin(), value.end());
		cout << max;
		}

int main() {
	int N, K, W, V;
	int start = 0;
	
	cin >> N >> K;
	vector<int> box1;
	vector<int> box2;
	for (int i = 0; i < N; i++) {
		cin >> W >> V;
		box1.push_back(W);
		box2.push_back(V);
	}
	for (int q = 0; q < box1.size(); q++) {
		cout << box1[q] << endl;
		cout << box2[q] << endl;
		cout << "------------------" << endl;
	}

	solution(N, K, box1, box2, start);
}