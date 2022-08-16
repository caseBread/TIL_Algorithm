#include<bits/stdc++.h>
#define ll long long
using namespace std;

int n, m;
int arr[1025][1025];
int x, y, xx, yy;
int s[1025][1025];


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> arr[i][j];
		}
		s[i][1] = arr[i][1];
		for (int j = 2; j <= n; j++) 
			s[i][j] = s[i][j - 1] + arr[i][j];
		
	}


	for (int i = 0; i < m; i++) {
		cin >> y >> x >> yy >> xx;
		int summ = 0;
		for (int j = y; j <= yy; j++) {
			summ += (s[j][xx] - s[j][x - 1]);
		}
		cout << summ << '\n';
	}

}