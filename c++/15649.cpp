#include <iostream>
#include <vector>
using namespace std;

void solution(int index, int number, int N, int M, vector<int>box) {
	vector<int>tmp;
	if (index == M) {
		for (int i = 0; i < M; i++) {
			cout << box[i] << " ";
		}
		cout << endl; 
		return;
	} 
	for (int j = index; j < N; j++) {
		box.push_back(number);
		vector<int> tmp = { 0 };
		tmp[0] = box[index];
		box[index] = box[j];
		box[j] = tmp[0];
		return solution(index + 1, number + 1, N, M, box);
		tmp[0] = box[index];
		box[index] = box[j];
		box[j] = tmp[0];
		

	}
}
int main() {

	int N, M;
	cin >> N >> M;
	vector <int> box;
	solution(0,1, N, M, box);

	

}