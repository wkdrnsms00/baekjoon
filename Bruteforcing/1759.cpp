//암호 만들기
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int L, C;
char key[15];
//char candidate[15];

void dfs(int start, string str, int vowel, int consonant) {

	if (str.size() == L) {

		if (vowel >= 1 && consonant >= 2) {
			cout << str << endl;
			return;
		}

	}

	for (int i = start; i < C; i++) {
		if (key[i] == 'a' || key[i] == 'e' || key[i] == 'i' || key[i] == 'o' || key[i] == 'u')
			dfs(i + 1, str + key[i], vowel + 1, consonant);
		else
			dfs(i + 1, str + key[i], vowel, consonant + 1);
	}


}
int main() {

	//input
	cin >> L >> C;

	for (int i = 0; i < C; i++) {
		cin >> key[i];
	}

	sort(key, key + C);
	dfs(0, "", 0, 0);

	return 0;
}


